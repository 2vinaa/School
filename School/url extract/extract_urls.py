import re


def find_urls(string):
    regex = r"((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)"
    urls = re.findall(regex, string)
    return [url[0] for url in urls if url[0].startswith("http")]
