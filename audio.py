import googletrans
import speech_recognition
import gtts
import os
from playsound import playsound
audio_file_path = r'C:\\Users\\hhh\\Downloads\\SundarPichai.mp3'
recognizer = speech_recognition.Recognizer()
with speech_recognition.AudioFile(audio_file_path) as source:
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice, language="en")
translator = googletrans.Translator()
translation = translator.translate(text, dest="hi")
converted_audio = gtts.gTTS(translation.text, lang="hi")
converted_audio.save('captured_voice.mp3')
playsound('captured_voice.mp3')
os.remove('captured_voice.mp3')
translation = translator.translate(text, dest="te")
converted_audio = gtts.gTTS(translation.text, lang="te")
converted_audio.save('captured_voice.mp3')
playsound('captured_voice.mp3')
os.remove('captured_voice.mp3')
