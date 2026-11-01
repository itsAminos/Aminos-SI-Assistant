import sys
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from aiogram import types
from app.core.config import config
from app.bot.loader import bot, dp
from app.bot.handlers import router

logging.basicConfig(level=logging.INFO)
dp.include_router(router)

# Use token in path to secure the endpoint against unauthorized POSTs
WEBHOOK_PATH = f"/webhook/{config.bot_token}"
# Replace with your actual domain or ngrok URL for local testing
WEBHOOK_URL = f"https://your-domain.ngrok-free.app{WEBHOOK_PATH}"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Startup Logic ---
    bot_name = "Aminos-SI-Assistant"
    version = "0.1.0"
    python_version = sys.version.split()[0]
    masked_token = f"{config.bot_token.split(':')[0]}:***"

    print(f"🚀 Starting {bot_name} v{version} | Python {python_version}")
    print(f"Loaded Bot Token: {masked_token}")
    print(f"Status: Initializing Telegram webhook at {WEBHOOK_URL}...")

    await bot.set_webhook(
        url=WEBHOOK_URL,
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True
    )
    yield

    # --- Shutdown Logic ---
    print("Status: Shutting down and cleaning up webhooks...")
    await bot.delete_webhook()
    await bot.session.close()


app = FastAPI(lifespan=lifespan)


@app.get("/health")
async def health_check():
    return {"status": "healthy", "bot": "Aminos-SI-Assistant"}


@app.post(WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    """Event-driven endpoint receiving updates directly from Telegram."""
    update_data = await request.json()
    update = types.Update(**update_data)
    await dp.feed_update(bot=bot, update=update)
    return {"ok": True}