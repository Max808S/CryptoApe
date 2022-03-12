from aiogram.types import Message
from aiogram import Router

from keypads.keyboards import coins_menu_inline_keyboard as ik

# Creating Router
admin_router = Router()


@admin_router.message(commands="admin")
async def cmd_test(message: Message):
    await message.answer("This is a handler for admins only")


@admin_router.message(commands='admin-test')
async def cmd_test1(message: Message) -> str:
    """
    /admin-test bot commands
    """
    test_text = (
        f'ONLY ADMINS SEE THAT ^^'
    )
    await message.answer(test_text, reply_markup=ik())