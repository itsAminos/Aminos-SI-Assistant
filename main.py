import sys
import asyncio
import logging
from app.core.config import config
from app.bot.loader import bot, dp
from app.bot.handlers import router


async def main():
    bot_name = "Aminos-SI-Assistant"
    version = "0.1.0"
    python_version = sys.version.split()[0]

    logging.basicConfig(level=logging.INFO)
    dp.include_router(router)

    # Masking the token so we don't leak it in logs (e.g., 12345:***)
    masked_token = f"{config.bot_token.split(':')[0]}:***"
    startup_log = f"🚀 Starting {bot_name} v{version} | Python {python_version}"

    # Print logs before starting the blocking polling loop
    print(startup_log)
    print(f"Loaded Bot Token: {masked_token}")
    print("Status: Initializing Telegram polling...")

    # Drops pending updates from while the bot was offline, then starts polling
    await bot.delete_webhook(drop_pending_updates=True)

    # The event loop takes over here indefinitely
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())