#cvlac profe roman5690
#my_url = 'http://scienti.colciencias.gov.co:8081/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0000105260'
#mi cvlac
my_url = 'http://scienti.colciencias.gov.co:8081/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0000418552'
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
    buscaEstrategias = containers[a].h3
    #print(buscaEstrategias)
    try:
        if buscaEstrategias.text == "Estrategias pedagógicas para el fomento a la CTI":
            all = a
            #print(all)
            break
    except AttributeError:
        pass

containerb = containers[all]
container = containerb.findAll("blockquote")
cont = container[0]
info_Estrategia = cont.text

index1 = info_Estrategia.find("\xa0\r\n                                Inicio en") + 44
index1 = info_Estrategia.find(" - ",index1,len(info_Estrategia)) + 3
index2 = index1 + 4
info_Estrategia[index1:index2]
