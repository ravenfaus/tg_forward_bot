from aiogram import types


async def start_message(message: types.Message):
    text = f'Привет, {message.from_user.full_name}. Что-то хотел узнать??'
    await message.answer(text)
