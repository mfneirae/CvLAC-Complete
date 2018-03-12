
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
    buscaworkp = containers[a].h3
    #print(buscaworkp)
    try:
        if buscaworkp.text == "Documentos de trabajo":
            all = a
            #print(all)
            break
    except AttributeError:
        pass

containerb = containers[all]
container = containerb.findAll("blockquote")
tipotexno = containerb.findAll("li")

cont = container[0]
info_workp = cont.text
tipotex = tipotexno[0]

#Lugar
index1 = info_workp.find('En: ') + 4
index2 = info_workp.find('\r\n                    ',index1,len(info_workp))
lugar = info_workp[index1:index2]
if lugar == ". ":
    lugar = ""

index1 = info_workp.find("Palabras:")
index2 = info_workp.find("Areas:")
index3 = info_workp.find("Sectores:")
if index1 == -1:
    palabras = ""
elif index2 != -1:
    palabras = info_workp[index1 + 9:index2]
elif index2 == -1 and index3 != -1:
    palabras = info_workp[index1 + 9:index3]
else:
    palabras = info_workp[index1 + 9:len(info_workp)]
