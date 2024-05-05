from utils.speak import speak_text
from utils.listen import listen_mic

from commands.buscarWikipedia import search_wikipedia


def commands_bot(command):
    print(command)
    if "procurar" or "buscar" and "wikipédia" in command.lower():
        speak_text("O que você está procurando?: ")
        assunto = listen_mic()
        print(assunto)
        speak_text("Certo...")
        print("analizando...")
        print(search_wikipedia(assunto))
        speak_text(search_wikipedia(assunto))
        print("comando finalizado")

    speak_text("Em que eu posso ajudar? ")
    prompt = listen_mic()
    if prompt == "":
        return
    commands_bot(prompt)
