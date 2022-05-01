import aiohttp

from config_reader import load_config
from misc.text_file import gas_text

from misc.logging import logger


async def gas_tracker() -> str:
    """
    Getting gwei info
    """
    async with aiohttp.ClientSession() as session:
        config = load_config()
        try:
            # free gas station plan api only: 2000 calls/mounth
            gas_station_url = (
                "https://ethgasstation.info/api/ethgasAPI.json?api-key="
                f"{config.misc.gas_staion}"
            )

            async with session.get(gas_station_url) as response:
                gas_data = await response.json()
                
                gas_fastest = gas_data['fastest']
                fastest_wait = gas_data['fastestWait']
                gas_slow = gas_data['safeLow']
                slow_wait = gas_data['safeLowWait']
                gas_avg = gas_data['average']
                avg_wait = gas_data['avgWait']

                result = (
                    f"<tg-spoiler>{gas_text}</tg-spoiler>\n\n"
                    f"Стоимость транзакций сейчас:\n"
                    f"Быстро: <b>{int(gas_fastest/10)}</b> GWEI  ~  <b>{fastest_wait}</b> мин\n"
                    f"Среднее: <b>{int(gas_avg/10)}</b> GWEI  ~  <b>{avg_wait}</b> мин\n"
                    f"Медленно: <b>{int(gas_slow/10)}</b> gwei  ~  <b>{slow_wait}</b> мин\n\n"
                    f"<b>Data by</b> <a href='https://ethgasstation.info'>Eth Gas Station</a> ⛽️"
                )
                logger.info(f"Getting GAS stats from ETH GAS STATION")
        except:
            ether_scan_url = (
                "https://api.etherscan.io/api?module=gastracker"
                f"&action=gasoracle&apikey={config.misc.etherscan}"
            )

            async with session.get(ether_scan_url) as response:
                gas_data = await response.json()

                safe_gas = gas_data["result"]["SafeGasPrice"]
                propose_gas = gas_data["result"]["ProposeGasPrice"]
                fast_gas = gas_data["result"]["FastGasPrice"]

                result = (
                    f"{gas_text}\n\n"
                    f"Стоимость транзакций сейчас:\n"
                    f"Быстро: <b>{fast_gas}</b> gwei\n"
                    f"Среднее: <b>{propose_gas}</b> gwei\n"
                    f"Медленно: <b>{safe_gas}</b> gwei\n\n"
                    f"<b>Data by</b> <a href='https://etherscan.io'>EtherScan</a> ⛽️"
                )
                logger.info(f"Getting GAS stats from ETHERSCAN")
        return result