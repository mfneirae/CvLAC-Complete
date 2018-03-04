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
def redesextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import init
    import bs4
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
    global contredes
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
        buscaReds = containers[a].h3
        #print(buscaReds)
        try:
            if buscaReds.text == "Redes de conocimiento especializado":
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
            info_red = cont.text
            #Nombre de la red
            index1 = info_red.find("Nombre de la red ") + 17
            index2 = info_red.find("\xa0\r\n                                Tipo de red")
            Nombrered = info_red[index1:index2]
            # Tipo de Red
            index1 = info_red.find("Tipo de red") + 11
            index2 = info_red.find(",\xa0\r\n                                Creada el:")
            Tipored = info_red[index1:index2]
            # Lugar Red
            index1 = info_red.find("\xa0\r\n                                    en ") + 42
            index2 = info_red.find(" \xa0 \r\n")
            LugarRed = info_red[index1:index2]
            #Fecha de Realización inicio y fin
            index1 = info_red.find("Creada el:") + 10
            index2 = index1 + 4
            AnoRedini = info_red[index1:index2]
            if AnoRedini == "," or AnoRedini == ",\xa0\r\n":
                MesRedini = "-"
                AnoRedini = "-"
                FechaRedini = "-"
                MesRedfin = "-"
                AnoRedfin = "-"
                FechaRedfin = "-"
            else:
                index1 = index1 + 5
                index2 = index1 + 2
                MesRedini = info_red[index1:index2]
                index1 = info_red.find("Creada el:") + 10
                index2 = index1 + 10
                FechaRedini = info_red[index1:index2]
                index1 = info_red.find(",",index1,index1 + 58) + 40
                index2 = index1 + 4
                AnoRedfin = info_red[index1:index2]
                if AnoRedfin == "    " or AnoRedfin == ",":
                    MesRedfin = "-"
                    AnoRedfin = "-"
                    FechaRedfin = "-"
                else:
                    index1 = index1 + 5
                    index2 = index1 + 2
                    MesRedfin = info_red[index1:index2]
                    index1 = info_red.find("Creada el:") + 10
                    index1 = info_red.find(",",index1,index1 + 58) + 40
                    index2 = index1 + 10
                    FechaRedfin = info_red[index1:index2]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + "1" + ";"\
            + Nombrered.strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","") + ";" \
            + "" + ";"\
            + "" + ";"\
            + "" + ";"\
            + LugarRed.strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","") + ";" \
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
            + "" + ";"\
            + "\n")
            init.APROPIACION.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + FechaRedini.strip() + ";" \
            + AnoRedini.strip() + ";" \
            + MesRedini.strip() + ";" \
            + FechaRedfin.strip() + ";" \
            + AnoRedfin.strip() + ";" \
            + MesRedfin.strip() \
            + "\n")
            COD_PRODUCTO = COD_PRODUCTO + 1

    else:
        print("El Docente ",name," ",last," ","no tiene Redes Asociadas")
    contredes = [COD_PRODUCTO]
