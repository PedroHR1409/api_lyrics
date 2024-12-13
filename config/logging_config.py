import logging


def setup_logging():
    """
    Configura o sistema de logging para a aplicação.

    Esta função configura o logging para registrar mensagens em um arquivo 
    chamado 'app.log' localizado no diretório 'logs'. As mensagens de log 
    incluem a data e hora, o nome do logger, o nível de severidade e a mensagem.

    Formato do log:
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    Níveis de log:
    - INFO: Mensagens informativas.
    - WARNING: Avisos sobre possíveis problemas.
    - ERROR: Mensagens de erro.
    - CRITICAL: Mensagens de erro grave.
    """
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
