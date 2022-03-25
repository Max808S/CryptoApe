from aiogram.types import Message
from aiogram import Router, F
from typing import Match

admin_router = Router(name=__name__)


@admin_router.message(commands="admin")
async def cmd_admin(message: Message):
    """
    Admins only handler
    Use: /admin
    """
    # admin_text = f"Admin {message.from_user.first_name} 😈"
    await message.answer("💫")


@admin_router.message(F.text.regexp(r"admin (\d+)").as_("text_match"))
async def test_balance(message: Message, text_match: Match) -> None:
    """
    Use: admin 420
    """
    result = f"Matched: {text_match.group(1)!r}"
    await message.answer(result)