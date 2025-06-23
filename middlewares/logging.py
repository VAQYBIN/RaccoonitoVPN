from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
import logging

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: TelegramObject, data: dict):
        if isinstance(event, Message):
            logger.info(
                "Message from %s (%s): %s",
                event.from_user.full_name if event.from_user else "?",
                event.chat.id,
                event.text,
            )
        else:
            logger.debug("Event: %s", event)
        return await handler(event, data)
