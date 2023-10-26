import os
import requests
from urllib.parse import urlparse

from verificacoes.verificacao_casas_decimais import verificar_casas_decimais
from verificacoes.verificacao_sistema import verificar_sistema
from verificacoes.verificacao_url import obter_url_sem_numeros

# URL base dos arquivos que você deseja baixar
url_base = input("Digite a URL base dos arquivos: ")
extensao_desejada = input("Digite a extensão desejada (por exemplo, pdf, xls, etc.): ")

url_sem_numeros = obter_url_sem_numeros(url_base, extensao_desejada)
casas_decimais = verificar_casas_decimais(url_base, extensao_desejada)

# Especifique o diretório onde você deseja salvar os arquivos
diretorio_destino = verificar_sistema()

# Loop para baixar os arquivos
for i in range(1, 30):
    numero_arquivo = f"{i:02}"  # Formate o número para dois dígitos com zero à esquerda

    url_base = url_sem_numeros
    url_arquivo = f"{url_base}{numero_arquivo}"  # Crie a URL completa do arquivo

    # Extraia a extensão do arquivo da URL de forma dinâmica
    extensao_arquivo = os.path.splitext(urlparse(url_arquivo).path)[1]

    nome_arquivo = f"arquivo{numero_arquivo}{extensao_arquivo}"  # Gere o nome do arquivo com a extensão

    caminho_local = os.path.join(diretorio_destino, nome_arquivo)

    if os.path.exists(caminho_local):  # Verifique se o arquivo já existe no diretório de destino
        os.remove(caminho_local)  # Se existir, remova o arquivo

    response = requests.get(url_arquivo)  # Faça uma solicitação GET para baixar o arquivo da URL

    if response.status_code == 200:  # Verifique se a resposta do servidor é bem-sucedida (código 200)

        with open(caminho_local, 'wb') as arquivo_local:  # Abra o arquivo local para escrita binária
            arquivo_local.write(response.content)  # Escreva o conteúdo do arquivo da resposta no arquivo local
        print(f"Arquivo {nome_arquivo} baixado com sucesso em {caminho_local}.")  # Imprima uma mensagem de sucesso
    else:
        print(
            f"Falha ao baixar o arquivo {nome_arquivo}. Código de resposta: {response.status_code}")  # Imprima uma mensagem de falha
