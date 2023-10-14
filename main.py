from requests import get
from bs4 import BeautifulSoup as bs

container = '.quote default_cursor_cs'
selector = '.text default_cursor_cs'

author = '.author default_cursor_cs'
base_url = 'http://quotes.toscrape.com/'

if __name__ == "__main__":
    # r = get(base_url)
    # if not r.ok:
    #     raise ValueError(r.reason)
    # with open('website.html', 'wb') as _:
    #     _.write(r.content)

    with open('website.html', 'r') as _:
        content = _.read()

    soup = bs(content, "html.parser")
    containers = soup.select(container)
    # print(len(containers))
    for container in containers:
        author = container.select_one(author)
        quote = container.select_one(selector)

        print(
            author.text,
            quote.text,
            '',
            sep='\n'
        )


