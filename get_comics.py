import sys
from bs4 import BeautifulSoup
import requests
from PIL import Image

#Will Accept 2 arguments, first is number N, second is Path
N=sys.argv[1]
path=sys.argv[2]
permanent=path
r=requests.get("https://xkcd.com")
soup=BeautifulSoup(r.text, "lxml")
url="https:"
divComic=soup.findAll('div', attrs={'id' : 'comic'})
for div in divComic:
    url=url+(div.find('img')['src'])
temp=""
for a in soup.find_all('a', {'rel' : 'prev', 'accesskey' : 'p'}):
    temp=(a['href'])
next="https://xkcd.com"
next=next+temp
path=path+url[29:]
image=Image.open(requests.get(url, stream=True).raw)
image.save(path)
i=0
n=int(N)
while i < n-1:
    r=requests.get(next)
    soup=BeautifulSoup(r.text, "lxml")
    url="https:"
    divComic=soup.findAll('div', attrs={'id' : 'comic'})
    for div in divComic:
        url=url+(div.find('img')['src'])
        #ulPrev=soup.findAll('ul', attrs={'class' : 'comicNav'})
        temp=""
    for a in soup.find_all('a', {'rel' : 'prev', 'accesskey' : 'p'}):
        temp=(a['href'])
        next="https://xkcd.com"
        next=next+temp
        path=permanent
        path=path+url[29:]
        image=Image.open(requests.get(url, stream=True).raw)
        image.save(path)
    i+=1
