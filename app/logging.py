import logging
from aiogram.types import Update

class LoggingMiddleware:
    async def __call__(self, handler, event: Update, data: dict):
        logging.info(f"Update: {event}")
        return await handler(event, data)