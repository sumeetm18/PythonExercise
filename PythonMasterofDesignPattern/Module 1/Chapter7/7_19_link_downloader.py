from collections.abc import Iterable

def get_pages(*links):
    if not isinstance(links, Iterable) or isinstance(
            links, (bytes, str)):
        links = [links]
    for link in links:
        #download the link with urllib
        print(link)

get_pages()
get_pages('http://www.google.com')
get_pages('http://www.archlinux.org','http://ccphillips.net/')