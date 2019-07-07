import os
from urllib.parse import urlparse


def _get_path_url(parse):
    path = parse.path.split('.')[0]
    if path[-1] == '/':
        return path[:-1]

    return path


def write_file(url, text):
    parse = urlparse(url)
    path = _get_path_url(parse)
    name = str(parse.netloc + path)

    directory_folder = f'{os.path.dirname(os.path.realpath(__file__))}/{name}.txt'
    folder_path = os.path.dirname(directory_folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with open(directory_folder, 'w') as file:
        file.write(text)
