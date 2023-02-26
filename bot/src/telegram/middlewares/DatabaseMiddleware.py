from aiogram import BaseMiddleware

from aiogram.types import Update
from sqlalchemy.exc import IntegrityError

from typing import Callable, Dict, Any


class DatabaseMiddleware(BaseMiddleware):
    async def __call__(
            self, 
            handler: Callable[[Update], Dict[str, Any]],
            event: Update,
            data: Dict[str, Any]
    ) -> Any:
        async_session = data.get('async_session')
        async with async_session() as session:
            data['session'] = session
            await handler(event, data)
            try:
                await session.commit()
            except IntegrityError:
                await session.rollback()