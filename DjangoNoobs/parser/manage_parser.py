"""
This module manage logic parser

"""

from random import choice
import educ_parser


def create_test_urls():
    protocol = ['http', 'https']
    urls = []
    for i in range(20):
        urls.append(f"{choice(protocol)}://domain{i}.com?param{i}=value{i}")
    return urls


def main():
    urls = create_test_urls()
    manage_requests = educ_parser.ManageRequest()
    urls_method = {}
    urls_method['GET'] = urls
    manage_requests.add_urls(urls_method)
    manage_requests.get_html(strong=True)


if __name__ == '__main__':
    main()
