from aiogram import BaseMiddleware
from aiogram.types import Message

from database import models

from typing import Callable, Dict, Any, Awaitable


class RegistrationMiddleware(BaseMiddleware):
    async def __call__(
            self, 
            handler: Callable[[Message], Dict[str, Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        async_session = data.get('async_session')
        async with async_session() as session:
            user = await models.User.get(session, event.from_user.id)
            if user:
                return await handler(event, data)
            await models.User.create(session, event.from_user.id)
            await session.commit()
            return await handler(event, data)
