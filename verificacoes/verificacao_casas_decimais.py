import requests
import re


def verificar_casas_decimais(url_base, extensao_desejada):
    # Realize uma solicitação HEAD para a URL base para verificar a validade da URL
    response = requests.head(url_base)

    # Verifique se a URL é válida e se contém a extensão desejada
    if response.status_code == 200:
        # Se a URL é válida, verifique se contém a extensão desejada
        url_path = response.url  # Obtém o caminho da URL final após redirecionamentos

        # Expressão regular para encontrar a string da extensão no URL
        pattern = r"/([^/]+)\." + extensao_desejada + r"$"

        match = re.search(pattern, url_path)

        if match:
            extensao_encontrada = match.group(1)

            # Encontre números no nome do arquivo
            numeros_arquivo = re.findall(r'\d+\.\d+', extensao_encontrada)

            if numeros_arquivo:
                numero_decimal = numeros_arquivo[0]
                casas_decimais = len(numero_decimal.split('.')[1])
                return casas_decimais
            else:
                return 0  # Se nenhum número decimal for encontrado
        else:
            return -1  # Se a extensão desejada não for encontrada na URL
    else:
        return -2  # Se a URL não for válida

