
re.sub(' +',' ',AQUI.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
#cvlac profe roman5690
#my_url = 'http://scienti.colciencias.gov.co:8081/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0000105260'
#mi cvlac
my_url = 'http://scienti.colciencias.gov.co:8081/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0000218430'
import bs4
import re
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
        if buscaeventos.text == "Libros":
            all = a
            #print(all)
            break
    except AttributeError:
        pass


containerb = containers[all]
container = containerb.findAll("blockquote")
tipolib = containerb.findAll("li")

tipoli = tipolib[x]
tipo = tipoli.text
cont = container[2]
info_libro = cont.text

index1 = info_libro.find('"\r\n                    En:') + 27
index2 = info_libro.find('\r\n                    ',index1,len(info_libro))
lugar = info_libro[index1:index2]
