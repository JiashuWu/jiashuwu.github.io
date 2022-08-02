import requests
from bs4 import BeautifulSoup
url = 'https://jiashuwu.github.io/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
urls = ""
for link in soup.find_all('a'):
    if link.get('href') != "None" and link.get('href') is not None and link.get('href')[0:4] == "http":
        url = link.get('href').replace(" ", "%20")
        atag = "<a href=\"" + url + "\">" + url + "</a>"
        urls += atag + "\n<br>\n<br>\n"
with open("sitemap.html", "w") as sitemap_html:
    sitemap_html.write(urls)
sitemap_html.close()
