import os
import urllib.request
from bs4 import BeautifulSoup



class Scraper:
    def __init__(self,
                 site):
        self.site = site


    def scrape(self):
        response = urllib.request.urlopen(self.site)
        html = response.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)
                with open('scrape.txt', 'a') as f:
                    f = f.write("\n" + url + "\n")


news = "https://news.sina.com.cn/"
Scraper(news).scrape()




