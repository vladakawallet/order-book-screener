import websockets
import asyncio
import PushDataV3ApiWrapper_pb2
import json
import requests
from logger import setup_logger
from pathlib import Path

MODULE_DIR =  Path(__file__).resolve().parent

class MexcSpotScreener:
    uri = "wss://wbs-api.mexc.com/ws"
    spot_channel = "spot@public.limit.depth.v3.api.pb"
    logger = setup_logger("mexc", MODULE_DIR)

    async def ws_connector(self, symbols: list, level: str):
        async with websockets.connect(self.uri) as ws:
            await ws.send(
                json.dumps({
                    "method": "SUBSCRIPTION", "params": [f"{self.spot_channel}@{symbol.replace("_", "", 1)}@{level}" for symbol in symbols]
                })
            )
            self.logger.info("Start listening MEXC websocket")

            async def ping():
                while True:
                    await ws.send(json.dumps({"method": "PING"}))
                    await asyncio.sleep(3)

            async def receive():
                while True:
                    response = await ws.recv()
                    if isinstance(response, bytes):
                        data = PushDataV3ApiWrapper_pb2.PushDataV3ApiWrapper()
                        data.ParseFromString(response)
                        asks = self.calculate(data.publicLimitDepths.asks)
                        bids = self.calculate(data.publicLimitDepths.bids)

                        print(f"MEXC: {data.symbol} | AVG Ask: {asks} | AVG Bid: {bids} | Level: {level}")

                    await asyncio.sleep(0.1)

            await asyncio.gather(ping(), receive())          

    def calculate(self, orders: list):
        avg = 0.0
        volumes = 0.0

        for b in orders:
            avg += float(b.price)*float(b.quantity)
            volumes += float(b.quantity)
                
        try: 
            price = avg/volumes
            if price < 0.1: price = round(price, 5)
            elif price < 1: price = round(price, 4)
            elif price < 10000: price = round(price, 2)
            else: price = round(price)
            return price
        except ZeroDivisionError as e:
            return None 

    def mexc_info(self):
        res = requests.get("https://api.mexc.com/api/v3/exchangeInfo")
        if res.status_code == 200:
            self.logger.info("Received tradable currencies from MEXC")
            return [f"{p["baseAsset"]}_{p["quoteAsset"]}" for p in res.json()["symbols"] if p["isSpotTradingAllowed"]]
        else: self.logger.warning(f"Unable to receive tradable currencies from MEXC. Status: {res.status_code}, reason: {res.reason}")

    async def main(self, symbols: list, level: str):
        symbols = [symbols[i:i+20] for i in range(0, len(symbols), 20)]
        tasks = []
        for symbol in symbols:
            tasks.append(self.ws_connector(symbol, level))

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    mexc = MexcSpotScreener()
    symbols = mexc.mexc_info()
    asyncio.run(mexc.main(symbols, "5"))