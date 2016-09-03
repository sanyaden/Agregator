import chardet
import requests
import re


def get_content(url):
    """
    Get web page in bytes format by url. If something wrong return None
    >>> type(get_content(url='http://itea.ua/courses-itea/python/python-advanced/'))
    <class 'bytes'>
    >>> type(get_content('hts://pysad2asdmotw.com/3/'))
    <class 'NoneType'>
    """

    try:
        if requests.head(url).status_code == 200:
            return requests.get(url).content
        else:
            return None
    except requests.exceptions.RequestException:
        return None


def decode(data):
    """Decode raw data to unicode string."""
    try:
        charset = chardet.detect(data)['encoding']
        return data.decode(charset)
    except ValueError:
        return ''


def remove_html_tags(page):
    """Remove HTML tags and remove more one whitespace characters."""
    without_tags = re.sub('<[^<]+?>', '', page)
    return re.sub('\s+', ' ', without_tags)
