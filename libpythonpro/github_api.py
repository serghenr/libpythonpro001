import requests


def buscar_avatar(usuario):

    """

    Busca o avatar de usuário no GitHub

    :param usuario: str com o nome de usuário de GitHub
    :return: str com o link do Avatar (foto)

    """

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':

    input_nome_usuario = input('Digite o nome do usuário do GitHub: ')

    print(buscar_avatar(input_nome_usuario))
