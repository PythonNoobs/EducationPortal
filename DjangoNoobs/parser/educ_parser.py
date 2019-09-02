"""
Classes for parsing. ManageRequest, ...

"""
import parser_validators


class ManageRequest:
    """
    Create requests, generate proxy and user_agent.
    Validate Urls

    """

    len_urls = 0

    def add_urls(self, urls, method=None):
        """
        Add urls in attribue's instance(urls)
        Take required param "urls" and not required "method".
        Each url and param "method" must be string type
        "method" is HTTP method, by which make requests.
        If transfare param "method",
        parameter "urls" must be list with urls else
        "urls" must be dict, where key is HTTP method(GET, POST, HEAD, DELETE),
        value is urls

        """

        available_methods = ['GET', 'POST', 'HEAD', 'DELETE']
        urls_method = {}
        if method in available_methods:
            urls_method[method] = urls
        elif isinstance(urls, dict):
            for method, urls in urls.items():
                if method in available_methods:
                    break
                else:
                    method = None
            if not method:
                raise ValueError("Method not found(GET, POST, HEAD, DELETE)")
            if urls and not method:
                urls_method["GET"] = urls
            elif not urls:
                raise ValueError("Key urls not found")
            elif method in available_methods:
                urls_method[method] = urls
            else:
                raise ValueError('Error')
        else:
            raise ValueError("You need pass parametr method. "
                             "Or param urls must be dict")

        self.len_urls += len(urls_method[method])
        if not self.__dict__.get('urls'):
            self.urls = urls_method
        else:
            for value_method, urls in self.urls:
                if value_method == method:
                    self.urls[method].append(urls)
                else:
                    self.urls[method] = urls

    def del_urls(self, urls):
        """
        Delete urls from attribue's instance(urls).
        Take required param "urls"
        "urls" must be dict, where key is HTTP method(GET, POST, HEAD, DELETE)
        value is urls in string type

        """

        available_methods = ['GET', 'POST', 'HEAD', 'DELETE']
        if not isinstance(urls, dict):
            raise ValueError("Param must be dict, where key is method,"
                             " value is urls")
        for method, urls in urls.items():
            if method not in available_methods:
                raise ValueError("Method not found(GET, POST, HEAD, DELETE)")
            old_urls = self.urls[method]
            urls = urls.copy()
            for url in urls:
                if url in old_urls:
                    old_urls.remove(url)
                    self.len_urls -= 1
                else:
                    raise ValueError("Url not found")

    def get_html(self, strong=True):
        """
        ...

        """

        if not isinstance(strong, bool):
            raise ValueError("Argument \"strong\""
                             f"must be bool, got {type(strong)}")
        self.strong = strong
        broken_urls = self._validate_urls()
        warning_message = ""
        if broken_urls:
            if broken_urls[0]:
                warning_message += f"Not valid urls {len(broken_urls[0])}:"
                for url in broken_urls[0]:
                    warning_message += " " + str(url)
            if broken_urls[1]:
                warning_message += f"Duplicate urls {len(broken_urls[1])}:"
                for url in broken_urls[1]:
                    warning_message += " " + str(url)

        if self.strong and warning_message:
            raise ValueError(warning_message)
        else:
            self.__create_request()

    def __create_request(self):
        """
        ...

        """
        pass

    def __generate_agent_proxy(self, len):
        """
        ...

        """
        pass

    def __get_proxy(self, len):
        """
        ...

        """
        pass

    def _validate_urls(self):
        """
        Validate url with djano-url-validator and check dup in sequence

        """

        dup_urls = []
        not_valid_urls = []
        for urls in self.urls.values():
            if isinstance(urls, str):
                urls = [urls]
            if self.len_urls <= 0:
                raise AttributeError(f"Urls-list empty")
            try:
                urls.__iter__
            except AttributeError:
                raise ValueError('Only iterable object or string')

            url_valid = parser_validators.UrlsValirdator(['http', 'https'])
            not_valid_iter_urls = url_valid.valid_seq(urls, self.strong)
            if not_valid_iter_urls:
                not_valid_urls.append(not_valid_iter_urls)
            self.__check_dup_urls(dup_urls)

        if dup_urls or not_valid_urls:
            return not_valid_urls, dup_urls

    def __check_dup_urls(self, dup_urls):
        """
        Check duplicate urls and return remove urls from the list

        """

        for urls in self.urls.values():
            for url in urls:
                if urls.count(url) > 1:
                    urls.remove(url)
                    dup_urls.append(url)

        return dup_urls
