import openai
from dotenv import load_dotenv
import os


def chatgpt_text(request_text: str):
    """
    Подключение и запрос к ChatGPT
    :param request_text:
    :return:
    """

    load_dotenv('../env')

    # Replace YOUR_API_KEY with your OpenAI API key

    openai.api_key = os.getenv('API_TOKEN_CHATGPT')
    # задаем модель
    model_engine = "text-davinci-003"

    # задаем макс кол-во слов
    max_tokens = 128

    # генерируем ответ
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=request_text,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # выводим ответ
    text = completion.choices[0].text
    return text
