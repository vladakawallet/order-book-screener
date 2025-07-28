from gateio import GateIOSpotScreener
from mexc import MexcSpotScreener
import asyncio

async def main():
    m = MexcSpotScreener()
    g = GateIOSpotScreener()

    if m and g: 
        symbols = list(set(m.mexc_info()) & set(g.gate_info()))

        tasks = [
            m.main(symbols, "5"),
            g.main(symbols, "5")
        ]
    
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())