"""
Classes for parsing. ManageRequest, ...

"""
import parser_validators


class ManageRequest:
    """
    Create requests, generate proxy and user_agent.
    Validate Urls

    """
    def __init__(self, parsing_urls, strong=True):
        """
        if strong=True, call exception when validation failed
        if strong=False, cotinue work without broken urls

        """

        if not isinstance(strong, bool):
            raise ValueError("Argument \"strong\""
                             f"must be bool, got {type(strong)}")
        self.strong = strong
        self.urls = parsing_urls
        broken_urls = self._validate_urls()
        if broken_urls:
            self.__broken_urls = broken_urls
        else:
            self.__broken_urls = None

    def get_html(self):
        pass

    def __create_request(self, urls):
        pass

    def __generat_agent_proxy(self, len):
        pass

    def _validate_urls(self):
        """
        Validate url with djano-url-validator and check dup in sequence

        """

        if isinstance(self.urls, str):
            self.urls = [self.urls]
        url_valid = parser_validators.UrlsValirdator(['http', 'https'])
        not_valid_urls = url_valid.valid_seq(self.urls, self.strong)
        dup_urls = self.__check_dup_urls()
        if dup_urls or not_valid_urls:
            return not_valid_urls, dup_urls

    def __check_dup_urls(self):
        """
        Check duplicate urls and remove them

        """
        urls = self.urls
        dup_urls = []
        for url in urls:
            if urls.count(url) > 1:
                self.urls.remove(url)
                dup_urls.append(url)
        return dup_urls
