from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from datetime import datetime
from contextlib import suppress
from db.models import CryptoApe_DB


async def add_user(session: AsyncSession, user_id: int, username: str, full_name: str):
    """
    Adding a user to the database
    """
    new_user = CryptoApe_DB()
    new_user.user_id = user_id
    new_user.username = username
    new_user.full_name = full_name
    new_user.entry_time = datetime.utcnow()
    session.add(new_user)
    with suppress(IntegrityError):
        await session.commit()


# from sqlalchemy import selects

    # logger.info(
    #         f"USER: {full_name} USERNAME: {username} "
    #         f"ID: {user_id} already in the database"
    #         )
    # await session.execute(
    #     select(CryptoApe_DB).where(
    #         CryptoApe_DB.user_id == user_id, 
    #         CryptoApe_DB.username == username)
    # )
    # await session.commit()