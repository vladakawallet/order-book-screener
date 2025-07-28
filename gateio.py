import websockets
import asyncio
import json
import requests
import time
from logger import setup_logger
from pathlib import Path

MODULE_DIR =  Path(__file__).resolve().parent

class GateIOSpotScreener:
    uri = "wss://api.gateio.ws/ws/v4/"
    logger = setup_logger("gateio", MODULE_DIR)

    async def ws_connector(self, symbols: list, level: str):
        async with websockets.connect(self.uri) as ws:
            await ws.send(
                json.dumps({
                    "time": int(time.time()),
                    "channel": "spot.order_book",
                    "event": "subscribe",
                    "payload": [[s, level, "100ms"] for s in symbols]
                })
            )
            self.logger.info("Start listening GateIO websocket")

            async def ping():
                while True:
                    await ws.send(json.dumps({"method": "PING"}))
                    await asyncio.sleep(3)

            async def receive():
                while True:
                    res = await ws.recv()
                    res = json.loads(res)
                    if res["event"] == "update":
                        
                        bid = self.calculate(res["result"]["bids"])
                        ask = self.calculate(res["result"]["asks"])
                        
                        print(f"GateIO: {res["result"]["s"]} | AVG Bid: {bid} | AVG Ask: {ask} | Level: {level}")

                    await asyncio.sleep(0.1)
                    
            await asyncio.gather(ping(), receive())          

    def calculate(self, orders: list):
        avg = 0.0
        volumes = 0.0

        for b in orders:
            avg += float(b[0])*float(b[1])
            volumes += float(b[1])
                
        try: 
            price = avg/volumes
            if price < 0.1: price = round(price, 5)
            elif price < 1: price = round(price, 4)
            elif price < 10000: price = round(price, 2)
            else: price = round(price)
            return price
        except ZeroDivisionError as e:
            return None 

    def gate_info(self):
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

        res = requests.get("https://api.gateio.ws/api/v4/spot/currency_pairs", headers=headers)
        if res.status_code == 200: 
            self.logger.info("Received tradable currencies from GateIO")
            return [f"{c["base"]}_{c["quote"]}" for c in res.json() if c["trade_status"] == "tradable"]
        else: self.logger.warning(f"Unable to receive tradable currencies from GateIO. Status: {res.status_code}, reason: {res.reason}")

    async def main(self, symbols: list, level: str):
        symbols = [symbols[i:i+50] for i in range(0, len(symbols), 50)]
        tasks = []

        for s in symbols:
            tasks.append(self.ws_connector(s, level))

        await asyncio.gather(*tasks)


if __name__ == "__main__":
    gate = GateIOSpotScreener()
    symbols = gate.gate_info()
    symbols = [symbols[i:i+50] for i in range(0, len(symbols), 50)]
    asyncio.run(gate.main(symbols, "5"))