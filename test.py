
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
    buscaptsignos = containers[a].h3
    #print(buscaptsignos)
    try:
        if buscaptsignos.text == "Signos distintivos":
            all = a
            #print(all)
            break
    except AttributeError:
        pass

containerb = containers[all]
container = containerb.findAll("blockquote")
cont = container[1]
info_ptsignos = cont.text

index = info_ptsignos.find(",")
index1 = info_ptsignos.find("En\xa0",index + 1,len(info_ptsignos)) + 3
index2 = info_ptsignos.find(",",index1,len(info_ptsignos))
Lugar = info_ptsignos[index1:index2]
