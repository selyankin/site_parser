import requests
import sys
import argparse
from request_parser import parse_request
from formatter import new_formatter
from file_writer import write_file


def argv_parser():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('url', default='', help='URL for parse')
    args_parser.add_argument('--href', default='True', help='Specify \'False\' if you don\'t want the result to\
     receive all links available by url')

    return args_parser


def parser():
    args_parser = argv_parser()
    args = args_parser.parse_args(sys.argv[1:])

    url = args.url
    flag_href = args.href in ['True', 'true']

    request = requests.get(url)

    if request.status_code is not 200:
        print('Connection error with code ' + str(request.status_code))

    lines = parse_request(request, url, flag_href)
    text = new_formatter(lines)
    write_file(url, text)


if __name__ == '__main__':
    parser()
