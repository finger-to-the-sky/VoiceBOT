import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from pathlib import Path
from chat.chat import chatgpt_text
from audio.voice import convert_mp3_to_wav, record_message

# from voice import record_message

load_dotenv('.env')
API_TOKEN = os.getenv('API_TOKEN_TELEGRAM')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def handle_file(file: types.File, file_name: str, path: str):
    Path(f"{path}").mkdir(parents=True, exist_ok=True)
    await bot.download_file(file_path=file.file_path, destination=f"{path}/{file_name}")


@dp.message_handler(content_types=[types.ContentType.VOICE])
async def voice_message_handler(message: types.Message):
    await message.answer('Обрабатываю ваше сообщение...')
    voice = await message.voice.get_file()
    path = "./files/voices"
    await handle_file(file=voice, file_name=f"{voice.file_id}.mp3", path=path)

    path_message = f'./files/voices/{voice.file_id}'
    convert_mp3_to_wav(f'{path_message}.mp3')

    text = record_message(f'{path_message}.wav')
    print(text)
    result_text = chatgpt_text(text)

    await message.answer(result_text)
    os.remove(f'{path_message}.mp3')
    os.remove(f'{path_message}.wav')


async def on_startup(_):
    print('Bot has been running')


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer('Welcome to ChatGPT bot')


@dp.message_handler()
async def answer_chatgpt(message: types.Message):
    await message.answer('Обрабатываю ваше сообщение...')
    text = chatgpt_text(message.text)
    print(message.text)
    await message.answer(text)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
