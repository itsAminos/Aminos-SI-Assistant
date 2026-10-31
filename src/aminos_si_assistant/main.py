import sys


def main():
    bot_name = "Aminos-SI-Assistant"
    version = "0.1.0"
    python_version = sys.version.split()[0]

    # F-string executing variables directly into the string at runtime
    startup_log = f"🚀 Starting {bot_name} v{version} | Python {python_version}"

    print(startup_log)
    print("Status: Waiting for Telegram Webhook initialization...")

if __name__ == "__main__":
    main()

