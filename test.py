import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
all = 4
a = 0
x = 0
y = 0
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("table")
containerb = containers[all]
container = containerb.findAll("table")
cont = container[1]
info_evento = cont.td.text
