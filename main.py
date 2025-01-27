import asyncio
from app import create_app
from app.telegram_bot import setup_bot, run_bot
from multiprocessing import Process

def run_flask():
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

def main():
    flask_process = Process(target=run_flask)
    flask_process.start()

    bot, dp = setup_bot()
    asyncio.run(run_bot(bot, dp))

if __name__ == "__main__":
    main()
