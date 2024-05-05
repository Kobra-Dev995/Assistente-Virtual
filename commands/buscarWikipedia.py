import wikipedia


def search_wikipedia(assunto):
    wikipedia.set_lang("pt")
    search_wikipedia = wikipedia.search(assunto)
    try:
        page_wikipedia = wikipedia.page(search_wikipedia[0])
        res_url = page_wikipedia.url
        res_content = page_wikipedia.summary
        return res_content
    except Exception as e:
        print("Não encontrei esse termo")
