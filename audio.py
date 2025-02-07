import speech_recognition as sr
AUDIO_FILE = input("Enter the audio file name: ")
r=sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
try:
    print("audio file contains, " +r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech REcognition could not understand audio")
except sr.RequestError:
    print("Couldn't get the results from Google Speech Recognition")
    





