import requests

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
            page = requests.get(url)
            if page.encoding:
                contet = page.content.decode(page.encoding)
            return requests.get(url).content
    except requests.exceptions.RequestException:
        return None


