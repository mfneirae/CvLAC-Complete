#cvlac profe roman
my_url = 'http://scienti.colciencias.gov.co:8081/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0000228958'
#mi cvlac
#my_url = 'http://scienti.colciencias.gov.co:8081/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0001545295'
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
        if buscaeventos.text == "Eventos científicos":
            all = a
            #print(all)
            break
    except AttributeError:
        pass


containerb = containers[all]
container = containerb.findAll("table")
cont = container[11]
info_evento = cont.td.text
b_eventos = cont.findAll("td")
autores = b_eventos[3].findAll("li")
index1 = info_evento.find("Realizado el:") + 13
index2 = index1 + 4
AnoEventoini = info_evento[index1:index2]
