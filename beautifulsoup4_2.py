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
        soup = BeautifulSoup(html, 'html.parser')
        with open('scrape.txt', 'a') as f:
            for tag in soup.find_all("a"):
                url = tag.get("href")
                if url is None:
                    continue
                if "html" in url:
                    print("\n" + url)
                    f.write(url + "\n")


Scraper("https://news.sina.com.cn/").scrape()




