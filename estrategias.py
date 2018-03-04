#
#
# #############################################################################
#         Copyright (c) 2018 by Manuel Embus. All Rights Reserved.
#
#             This work is licensed under a Creative Commons
#       Attribution - NonCommercial - ShareAlike 4.0
#       International License.
#
#       For more information write me to jai@mfneirae.com
#       Or visit my webpage at https://mfneirae.com/
# #############################################################################
#
#
def estrategiaextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import init
    import bs4
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
    global contEstrategia
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    all = 0
    a = 0
    x = 0
    y = 0
    auto = ""
    vincula = ""
    insti = ""
    vinculain = ""
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
    if all != 0:
        containerb = containers[all]
        container = containerb.findAll("blockquote")
        for x in range(0, len(container)):
            cont = container[x]
            info_Estrategia = cont.text
            #Nombre de la Estrategia
            index1 = info_Estrategia.find("Nombre de la Estrategia ") + 26
            index2 = info_Estrategia.find("\xa0\r\n                                Inicio en")
            NombreEstrategia = info_Estrategia[index1:index2]
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

            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + "7" + ";"\
            + NombreEstrategia.strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","") + ";" \
            + "" + ";"\
            + "" + ";"\
            + "" + ";"\
            + "" + ";"\
            + AnoEstrategiaini.strip() + ";" \
            + "" + ";"\
            + "" + ";"\
            + "" + ";"\
            + "" + ";"\
            + "" + ";"\
            + "" + ";"\
            + "" + ";"\
            + "" + ";"\
            + "" + ";"\
            + "" + ";"\
            + "" + ";"\
            + "" + ";"\
            + "" + ";"\
            + "\n")
            init.APROPIACION.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + FechaEstrategiaini.strip() + ";" \
            + AnoEstrategiaini.strip() + ";" \
            + MesEstrategiaini.strip() + ";" \
            + FechaEstrategiafin.strip() + ";" \
            + AnoEstrategiafin.strip() + ";" \
            + MesEstrategiafin.strip() \
            + "\n")
            COD_PRODUCTO = COD_PRODUCTO + 1

    else:
        print("El Docente ",name," ",last," ","no tiene Estrategias Asociadas")
    contEstrategia = [COD_PRODUCTO]
