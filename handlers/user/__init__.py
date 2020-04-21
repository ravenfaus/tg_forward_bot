from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import filters
from .messages import all_messages
from .start import start_message
from .answers import answer_step_1, answer_step_2, cancel_answer
from .answers import OrderAnswer


def setup(dp: Dispatcher):
    # Commands handlers
    dp.register_message_handler(start_message, commands='start')
    # Answers
    dp.register_message_handler(cancel_answer, commands='cancel', state=OrderAnswer.answer_text)
    dp.register_message_handler(answer_step_1, filters.RegexpCommandsFilter(regexp_commands=['to_([0-9]*)']), state='*')
    dp.register_message_handler(answer_step_2, state=OrderAnswer.answer_text)
    # Messages
    dp.register_message_handler(all_messages, content_types=types.ContentType.ANY, state='*')
