import re


r = r'(https|http|www)(://|.)*'


def split_lines(lines):
    words = []

    for line in lines:
        if re.fullmatch(r, line):
            words.append(line)
            continue

        w = line\
            .replace('\t', ' ')\
            .replace('\n', ' ')\
            .split(' ')

        for word in w:
            if word is not '':
                words.append(word)

        if ' ' in line:
            words.append('\n')

    return words


def get_formatted_text(words):
    formatted_lines = []

    buffer = ''
    for word in words:
        if re.fullmatch(r, word):
            if len(buffer) > 0:
                formatted_lines.append(buffer)
                buffer = ''

            formatted_lines.append(f'\n[{word}]\n\n')
            continue

        if word is '\n':
            if len(buffer) > 0:
                formatted_lines.append(buffer)
                buffer = ''

            formatted_lines.append(f'\n\n')
            continue

        if len(buffer) + len(word) > 80:
            formatted_lines.append(f'{buffer}\n')
            buffer = f'{word} '
        else:
            buffer += f'{word} '

    return ''.join(formatted_lines)


def new_formatter(lines):
    words = split_lines(lines)
    return get_formatted_text(words)
