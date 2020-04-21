from aiogram import types

from config import ADMIN_ID


async def all_messages(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer('Не выбран получатель.')
    else:
        await message.bot.send_message(ADMIN_ID, 'Поступило новое сообщение нажми сюда -> /to_{} чтобы ответить.'
                                       .format(message.from_user.id))
        await message.forward(ADMIN_ID)
        await message.answer('Информация передана.')