my_url = "http://scienti.colciencias.gov.co:8081/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0001545295"
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
    buscareconocimientos = containers[a].h3
    #print(buscareconocimientos)
    try:
        if buscareconocimientos.text == "Idiomas":
            all = a
            #print(all)
            break
    except AttributeError:
        pass

containerb = containers[all]
container = containerb.findAll("tr")
cont = container[2]
info_idiomas = cont.text

index1 = info_idiomas.find('\xa0') + 1
index2 = info_idiomas.find('\n',index1,len(info_idiomas))
idioma = info_idiomas[index1:index2]
index1 = index2 + 1
index2 = info_idiomas.find('\n',index1,len(info_idiomas))
habla = info_idiomas[index1:index2]
index1 = index2 + 1
index2 = info_idiomas.find('\n',index1,len(info_idiomas))
escribe = info_idiomas[index1:index2]
index1 = index2 + 1
index2 = info_idiomas.find('\n',index1,len(info_idiomas))
lee = info_idiomas[index1:index2]
index1 = index2 + 1
index2 = info_idiomas.find('\n',index1,len(info_idiomas))
entiende = info_idiomas[index1:index2]
