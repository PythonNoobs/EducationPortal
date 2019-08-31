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
	educ_parser.ManageRequest(urls)


if __name__ == '__main__':
	main()