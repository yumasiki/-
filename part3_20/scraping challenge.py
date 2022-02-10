# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io.

# GOOGLE CHANGED THEIR CODE. Try using 'articles' instead of 'html'


import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request\
            .urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        with open("headline.txt", "w")as f:
            for tag in sp.find_all("a"):
                url = tag.get("href")
                if url and "html" in url:
                    print("\n" + url)
                    f.write(url + "\n")


news = "https://news.ycombinator.com/"
Scraper(news).scrape()
