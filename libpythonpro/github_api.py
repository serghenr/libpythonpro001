import requests


def busacar_avatar(usuário):
    """
    Busca o avatar de um usuário no Github
    :param usuário: str com o nome de usuário no github
    :return: str com o link do avatar
    """

    url = f'https://api.github.com/users/{usuário}'
    resp = requests.get(url)
    return resp.json()['avatar_url']

if __name__ == '__main__':
    print(busacar_avatar('serghenr'))