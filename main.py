import sys
from app.core.config import config


def main():
    bot_name = "Aminos-SI-Assistant"
    version = "0.1.0"
    python_version = sys.version.split()[0]

    # Masking the token so we don't leak it in logs (e.g., 12345:***)
    masked_token = f"{config.bot_token.split(':')[0]}:***"

    startup_log = f"🚀 Starting {bot_name} v{version} | Python {python_version}"

    print(startup_log)
    print(f"Loaded Bot Token: {masked_token}")
    print("Status: Waiting for Telegram Webhook initialization...")


if __name__ == "__main__":
    main()