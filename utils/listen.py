import speech_recognition as sr


def listen_mic():
    recognize = sr.Recognizer()
    with sr.Microphone() as mic:
        recognize.adjust_for_ambient_noise(mic)
        print("Escutando...")
        audio = recognize.listen(mic)
        print("Analizando...")
        try:
            recognize.recognize_google(audio, language="pt-BR")  # type: ignore
        except sr.UnknownValueError:
            print("Não consegui entender o que você falou...")
            texto = ""
        except sr.RequestError:
            print("Erro com a conexão!")
            texto = ""
        return texto  # type: ignore
