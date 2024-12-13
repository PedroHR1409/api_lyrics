import logging
import requests
import streamlit as st

from config.logging_config import setup_logging
from src.search_music import search_lyrics

# Configura o logging
setup_logging()

def main():
    """
    Função principal da aplicação de busca de letras de músicas.
    
    Esta função define a interface da aplicação usando Streamlit, onde o
    usuário pode inserir o nome da banda e da música, e buscar a letra
    correspondente. Se encontrada, a letra é exibida; caso contrário, uma 
    mensagem de erro é mostrada.

    Raises:
        Exception: Se não encontrar a música pesquisada.
    """
    # Exibe a imagem de cabeçalho na interface
    st.image("https://i.imgur.com/SmktDIH.png")
    # Define o título da aplicação
    st.title("Letras de músicas")

    # Campos de entrada para o nome da banda e da música
    band = st.text_input("Digite o nome da banda: ", key="banda")
    music = st.text_input("Digite o nome da música: ", key="musica")
    # Botão de pesquisa
    search = st.button("Pesquisar")

    # Executa a busca quando o botão é clicado
    if search:
        try:
            # Chama a função que busca a letra da música
            lyric = search_lyrics(band, music)
            if lyric:
                # Exibe mensagem de sucesso e a letra da música
                st.success("Encontramos a letra da sua música.")
                st.text(lyric)
                # Registra a busca bem-sucedida no log
                logging.info(f"Letras encontradas para {band} - {music}")
            else:
                # Exibe mensagem de erro caso a letra não seja encontrada
                st.error("Infelizmente não foi possível encontrar a letra dessa música.")
                # Registra o aviso no log
                logging.warning(f"Letras não encontradas para {band} - {music}")
        except Exception as e:
            # Exibe mensagem de erro em caso de exceção
            st.error("Ocorreu um erro ao buscar a letra da música.")
            # Registra o erro no log
            logging.error(f"Erro ao buscar a letra para {band} - {music}: {e}")

if __name__ == "__main__":
    main()