import requests
import re


def obter_url_sem_numeros(url_base, extensao_desejada):
    # Realize uma solicitação HEAD para a URL base para verificar a validade da URL
    response = requests.head(url_base)

    # Verifique se a URL é válida e se contém a extensão desejada
    if response.status_code == 200:
        # Se a URL é válida, verifique se contém a extensão desejada
        url_path = response.url  # Obtém o caminho da URL final após redirecionamentos

        # Expressão regular para encontrar o nome do arquivo com a extensão desejada
        match = re.search(r'\/([^\/]+)\.([a-zA-Z0-9]+)$', url_path)

        if match:
            nome_encontrado = match.group(1)
            extensao_encontrada = match.group(2)

            # Remover a extensão e números do nome do arquivo
            # Encontre e remova números do nome do arquivo
            nome_do_arquivo_sem_numeros = re.sub(r'\d+$', '', nome_encontrado)

            # Substituir o nome do arquivo na URL
            url_sem_numeros_extensao = url_path.replace(f"{nome_encontrado}.{extensao_encontrada}",
                                                        nome_do_arquivo_sem_numeros)
            return url_sem_numeros_extensao
        else:
            return None  # Se a extensão desejada não for encontrada na URL
    else:
        return None  # Se a URL não for válida
