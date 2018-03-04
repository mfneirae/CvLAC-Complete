#cvlac profe roman
#my_url = 'http://scienti.colciencias.gov.co:8081/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0000228958'
#mi cvlac
my_url = 'http://scienti.colciencias.gov.co:8081/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0001545295'
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
all = 0
a = 0
x = 0
y = 0
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("table")
for a in range(0,len(containers)):
    buscaeventos = containers[a].h3
    #print(buscaeventos)
    try:
        if buscaeventos.text == "Redes de conocimiento especializado":
            all = a
            #print(all)
            break
    except AttributeError:
        pass

containerb = containers[all]
container = containerb.findAll("blockquote")
cont = container[1]
info_red = cont.text

index1 = info_red.find("\xa0\r\n                                    en ") + 42
index2 = info_red.find(" \xa0 \r\n")
LugarRed = info_red[index1:index2]
