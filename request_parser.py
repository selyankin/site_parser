from bs4 import BeautifulSoup as bs


def _parse_tag(tag, lines):
    for post in tag:
        if post.text is not '' and post.text is not '\n':
            lines.append(post.text)
            lines.append('\n')


def _parse_href(lines, soup, url):
    a = soup.find_all('a')
    for post in a:
        if post.text is not '':
            lines.append(post.text)

        if 'href' in post.attrs and post.attrs['href'] is not '':
            if post['href'][0] == '/':
                lines.append(url + post['href'])
            else:
                lines.append(post['href'])


def parse_request(request, url, flag=True):
    soup = bs(request.content, 'lxml')

    lines = []

    p_tag = soup.find_all('p')
    h_tag = soup.find_all('h1')

    _parse_tag(h_tag, lines)
    lines.append('\n')
    _parse_tag(p_tag, lines)

    if flag:
        _parse_href(lines, soup, url)

    return lines
