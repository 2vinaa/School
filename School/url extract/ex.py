import re


def find_urls(string):
    regex = r"((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)"
    urls = re.findall(regex, string)
    return [url[0] for url in urls if url[0].startswith("http")]


if __name__ == "__main__":
    unique_urls = set()
    urls = []
    deleted_urls = 0
    number_of_urls = 0

    with open("microsoft.com.html", mode="r+", encoding="UTF-8") as microsoft_file:
        for line in microsoft_file.readlines():
            url = find_urls(line)
            if url:
                urls.append(url)

    print(f"the total number of urls is {len(urls)}")
    [unique_urls.add(url[0]) for url in urls]
    print(f"i removed {len(urls)-len(unique_urls)} duplicates")

    with open("url.txt", mode="w", encoding="UTF-8") as url_file:
        for url in unique_urls:
            url_file.write(f"{url}\n")