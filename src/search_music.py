import requests


def search_lyrics(band, music):
    """
    Busca a letra de uma música de uma determinada banda.

    Parameters:
    band (str): Nome da banda/artista.
    music (str): Nome da música.

    Returns:
    str: Letra da música, se encontrada. Caso contrário, retorna uma string vazia.
    """
    endpoint = f"https://api.lyrics.ovh/v1/{band}/{music}"
    response = requests.get(endpoint)

    if response.status_code == 200:
        letra = response.json()["lyrics"]
        return letra
    else:
        return ""
