import soundfile as sf
import speech_recognition


recognizer = speech_recognition.Recognizer()


def convert_mp3_to_wav(mp3_file):
    audio, sr = sf.read(mp3_file)
    sf.write(f'{mp3_file[:-4]}.wav', audio, sr)


def record_message(filename: str):
    with speech_recognition.AudioFile(filename) as source:
        audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio,
                                               language="ru-RU")
            return text
        except speech_recognition.UnknownValueError:
            print("Не удалось распознать речь")
        except speech_recognition.RequestError as e:
            print(f"Ошибка сервиса распознавания речи: {e}")