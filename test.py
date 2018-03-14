
re.sub(' +',' ',AQUI.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
#cvlac profe roman5690
#my_url = 'http://scienti.colciencias.gov.co:8081/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0000105260'
#mi cvlac

my_url = 'http://scienti.colciencias.gov.co:8081/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0001545295'
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
    buscareconocimientos = containers[a].h3
    #print(buscareconocimientos)
    try:
        if buscareconocimientos.text == "Reconocimientos":
            all = a
            #print(all)
            break
    except AttributeError:
        pass

#Nombre Producto
index1 = 0
index2 = info_reconocimientos.find(',')
NombreProducto = info_reconocimientos[index1:index2]
#Insitucion
index1 = info_reconocimientos.find(',') + 1
index2 = info_reconocimientos.find('-')
Institucion = info_reconocimientos[index1:index2]
#Mes
index1 = info_reconocimientos.find('-') + 2
index2 = info_reconocimientos.find('de ',index1,len(info_reconocimientos))
Mes = info_reconocimientos[index1:index2]
#Programa Académico
index1 = index2 +3
index2 = len(info_reconocimientos)
Ano = info_reconocimientos[index1:index2]
