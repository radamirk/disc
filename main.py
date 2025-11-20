import asyncio

from modules.helpers.utils import choose_mode
from modules.core.trading_manager import TradingManager


async def run_mode(mode: str):
    manager = TradingManager()
    if mode == "futures_trading":
        await manager.start_trading()
    elif mode == "close_positions":
        await manager.close_all_positions()
    elif mode == "parse_accounts_data":
        await manager.parse_accounts_data(manager.accounts, True)


if __name__ == '__main__':
    selected_mode = choose_mode()
    if selected_mode:
        asyncio.run(run_mode(selected_mode))
