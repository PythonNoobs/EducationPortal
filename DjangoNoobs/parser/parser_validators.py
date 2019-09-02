"""
Help module. Extended django-validators from module django.core.validators,
or new validators.

"""
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class UrlsValirdator(URLValidator):
    """
    Extended for django url-validtor(django.core.validators).
    Add validation list-url

    """

    def valid_seq(self, urls, strong):
        """
        Check urls in sequence and remove those that not valid if strong False.
        If strong True, call exception
        Return list not valid urls.

        """
        removed_urls = []
        for url in urls:
            if not isinstance(url, str):
                urls.remove(url)
                removed_urls.append(url)
                continue
            try:
                self.__call__(url)
            except ValidationError:
                if strong:
                    raise ValidationError(
                        "Error validate url '%(not_valid_url)s'. "
                        "You can set argument strong=False",
                        params={'not_valid_url': url}
                    )
                else:
                    urls.remove(url)
                    removed_urls.append(url)
        return removed_urls
