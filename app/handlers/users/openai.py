import markdownify 
from aiogram.types import Message
from aiogram.enums import ChatAction, ParseMode

from app.routers import user_router as router
from loader import openai_client, bot, _
from utils import logger


@router.message(lambda message: message.text.startswith("!"))
async def openai_chat(message: Message):
    _message = await message.answer(reply_to_message_id=message.message_id, text=_("It will take a few seconds"))
    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    try:
        response = await openai_client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "user", "content": message.text[1:]}
            ],
            temperature=0,
        )
        answ = response.choices[0].message.content
        ques = f'{message.text[1:45]}...' if len(message.text) > 50 else message.text[1:]
        await bot.edit_message_text(chat_id=_message.chat.id, message_id=_message.message_id, text=f'`{ques}\n\n`{markdownify.markdownify(answ)}', parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        logger.error(e)
        await bot.edit_message_text(chat_id=_message.chat.id, message_id=_message.message_id, text=_("Looks like I got an error, it will be fixed soon"), parse_mode=ParseMode.MARKDOWN)
