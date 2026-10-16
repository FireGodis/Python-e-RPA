# Fila assíncrona e workers em Python

Eu uso uma fila `asyncio.Queue` para separar a entrada de trabalhos do processamento. O worker simula integração sem chamar serviços externos. Execute com `python worker.py`.
