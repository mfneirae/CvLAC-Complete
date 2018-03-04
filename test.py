#cvlac profe roman5690
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
        if buscaeventos.text == "Estrategias pedagógicas para el fomento a la CTI":
            all = a
            #print(all)
            break
    except AttributeError:
        pass

containerb = containers[all]
container = containerb.findAll("blockquote")
cont = container[1]
info_Estrategia = cont.text

#Fecha de Realización inicio y fin
index1 = info_Estrategia.find("\xa0\r\n                                Inicio en") + 44
index1 = info_Estrategia.find(" - ",index1,index1+10) + 3
index2 = index1 + 4
AnoEstrategiaini = info_Estrategia[index1:index2]
if AnoEstrategiaini == "," or AnoEstrategiaini == ",\xa0\r\n":
    MesEstrategiaini = "-"
    AnoEstrategiaini = "-"
    FechaEstrategiaini = "-"
    MesEstrategiafin = "-"
    AnoEstrategiafin = "-"
    FechaEstrategiafin = "-"
else:
    index1 = info_Estrategia.find("\xa0\r\n                                Inicio en") + 44
    index2 = info_Estrategia.find(" - ")
    MesEstrategiaini = info_Estrategia[index1:index2]
    index1 = info_Estrategia.find("\xa0\r\n                                Inicio en") + 44
    index2 = info_Estrategia.find(",\xa0\r\n                                Finalizó en")
    FechaEstrategiaini = info_Estrategia[index1:index2]
    index1 = info_Estrategia.find(",\xa0\r\n                                Finalizó en :") + 49
    index1 = info_Estrategia.find(" - ",index1,index1+10) + 3
    index2 = info_Estrategia.find(",\xa0                \t\t\t\r\n")
    AnoEstrategiafin = info_Estrategia[index1:index2]
    if AnoEstrategiafin == "" or AnoEstrategiafin == "-":
        MesEstrategiafin = "-"
        AnoEstrategiafin = "-"
        FechaEstrategiafin = "-"
    else:
        index1 = info_Estrategia.find(",\xa0\r\n                                Finalizó en :") + 49
        index2 = info_Estrategia.find(" - ",index1,len(info_Estrategia))
        MesEstrategiafin = info_Estrategia[index1:index2]
        index1 = info_Estrategia.find(",\xa0\r\n                                Finalizó en :") + 49
        index2 = index1 + 10
        index2 = info_Estrategia.find(",\xa0                \t\t\t\r\n")
        FechaEstrategiafin = info_Estrategia[index1:index2]
