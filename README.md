# Letras de Músicas 🎶

Bem-vindo ao projeto **Letras de Músicas**! Este projeto usa Streamlit para criar uma interface web que permite buscar letras de músicas de diferentes bandas e artistas.

## Funcionalidades 👷

- Busca de letras de músicas através da API [lyrics.ovh](https://lyrics.ovh/).
- Interface amigável criada com Streamlit.
- Registro de logs para monitoramento de atividades e erros.

## Estrutura do Projeto 🗂️

```plaintext
Letras-de-Musicas/
│
├───.gitignore
├───api_lyrics.py
├───LICENSE
├───poetry.lock
├───pyproject.toml
├───README.md
│
├───config/
│   ├───logging_config.py
│   └───__init__.py
│
├───logs/
│   └───app.log
│
└───src/
    ├───search_music.py
    └───__init__.py
```

## Instalação 🛠️

1. Clone o repositório
    ```sh
    git clone https://github.com/PedroHR1409/api_lyrics.git
    cd api_lyrics.git
    ```

2. Instale as dependências usando poetry:
    ```sh
    poetry install
    ```

3. Configure o ambiente virtual
    ```sh
    poetry shell
    ```

4. Instale as bibliotecas necessárias:
    ```sh
    pip install -r requirements.txt
    ```

5. Adicione uma pasta chamada ```logs```

5. Adicione um arquivo chamado ```app.log``` dentro da pasta ```logs```

## Uso 💻

1. Para iniciar a aplicação, execute:
    ```
    streamlit run api_lyrics.py
    ```

2. Acesse a aplicação no navegador em http://localhost:8501.

3. Digite o nome da banda e da música, e clique em "Pesquisar" para buscar a letra.

## Contribuição 🤝
1. Faça um fork do projeto.
2. Crie uma nova branch: ```git checkout -b minha-nova-feature```
3. Faça suas alterações e faça commit: ```git commit -m 'Adicionar nova feature'```
4. Envie para o repositório remoto: ```git push origin minha-nova-feature```
5. Abra um Pull Request.

## Licença 📜
Este projeto está licenciado sob a **Licença MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.