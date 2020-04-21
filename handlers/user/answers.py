from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class OrderAnswer(StatesGroup):
    answer_text = State()


async def answer_step_1(message: types.Message, regexp_command, state: FSMContext):
    print(regexp_command)
    await state.update_data(reply_id=regexp_command.group(1))
    await OrderAnswer.answer_text.set()
    await message.answer('Введи текст для ответа. Или нажми /cancel для отмены.')


async def answer_step_2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.bot.send_message(data['reply_id'], message.text)
    await message.answer('Ответ отправлен.')
    await state.finish()


async def cancel_answer(message: types.Message, state: FSMContext):
    await message.answer('Действие отменено')
    await state.finish()
