import pyttsx3


def speak_text(text):
    speaker = pyttsx3.init()
    voices = speaker.getProperty("voices")
    speaker.setProperty("voice", voices[1].id)
    speaker.setProperty("rate", 180)
    speaker.say(text)
    speaker.runAndWait()
