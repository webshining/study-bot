import re

from aiogram.enums import ChatAction, ParseMode
from aiogram.types import Message

from app.routers import user_router as router
from loader import _, bot, openai_client
from utils import logger


@router.message(lambda message: message.text and message.text.startswith("!"))
async def openai_chat(message: Message):
    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    text = await _get_openai_data(message.text[1:])
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN_V2)


async def _get_openai_data(question: str) -> str:
    ques = question
    ques = f'{ques[:45]}...' if len(ques) > 50 else ques
    ques = re.sub(r'[\_\*[\]()~>#\+\-=|{}\.!]', r'\\\g<0>', ques)
    ques = '\n'.join([f'>{i}' for i in ques.split("\n")])
    try:
        response = await openai_client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": "Yout should use markdown to answer."},
                {"role": "user", "content": question}
            ],
        )
        answ = response.choices[0].message.content
        answ = re.sub(r'[\_\*[\]()~>#\+\-=|{}\.!]', r'\\\g<0>', answ)
        return f'{ques}\n{answ}'
    except Exception as e:
        logger.error(e)
        return _("Looks like I got an error, it will be fixed soon")
