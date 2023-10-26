import os
import platform


# Verifique qual sistema operacional está sendo usado
def verificar_sistema():
    sistema = platform.system()

    # Defina o caminho da pasta de downloads com base no sistema operacional
    if sistema == 'Windows':
        diretorio_destino = os.path.expanduser('~\\Downloads')  # Caminho padrão no Windows
        print("Sistema Windows")
    elif sistema == 'Darwin':
        diretorio_destino = os.path.expanduser('~/Downloads')  # Caminho padrão no macOS (Darwin)\
        print("Sistema macOS")
    else:
        diretorio_destino = os.path.expanduser('~/Downloads')  # Caminho padrão no Linux
        print("Sistema Linux")

    # Verifique se o diretório de destino existe
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    return diretorio_destino  # Retorna o caminho da pasta de downloads

