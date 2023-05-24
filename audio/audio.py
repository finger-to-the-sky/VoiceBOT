from gtts import gTTS
from mutagen.mp3 import MP3
import time
import pygame
import os


def loading_audio(text: str, file: str):
    """
    Загрузка аудиофайла
    :param text:
    :param file:
    :return:
    """
    tts = gTTS(text=text, lang='ru')
    tts.save(file)  # Сохранить речь в аудиофайл


def play_audio(filename: str):
    """
    Воспроизведение аудио
    :param filename:
    :return:
    """
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(0)

    f = MP3(filename)
    file_length = f.info.length
    time.sleep(file_length)

    os.remove(filename)
