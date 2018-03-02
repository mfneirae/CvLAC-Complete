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
def evenextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import init
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
    auto = ""
    vincula = ""
    insti = ""
    vinculain = ""
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


    if all != 0:
        containerb = containers[all]
        container = containerb.findAll("table")
        for x in range(0, len(container)):
            cont = container[x]
            info_evento = cont.td.text
            #Nombre del evento
            index1 = info_evento.find("Nombre del evento:") + 18
            index2 = info_evento.find("Tipo de evento:")
            NombreEvento = info_evento[index1:index2]
            # Tipo de Evento
            index1 = info_evento.find("Tipo de evento:") + 15
            index2 = info_evento.find("Ámbito:")
            TipoEvento = info_evento[index1:index2]
            #Ambito
            index1 = info_evento.find("\xa0\r\n                                        Ámbito: ") + 51
            index2 = info_evento.find("\xa0                \r\n                                        Realizado el:")
            Ambito = info_evento[index1:index2]
            #Fecha de Realización inicio y fin
            index1 = info_evento.find("Realizado el:") + 13
            index2 = index1 + 4
            AnoEventoini = info_evento[index1:index2]
            if AnoEventoini == "," or AnoEventoini == ",\xa0\r\n":
                MesEventoini = "-"
                AnoEventoini = "-"
                FechaEventoini = "-"
                MesEventofin = "-"
                AnoEventofin = "-"
                FechaEventofin = "-"
            else:
                index1 = index1 + 5
                index2 = index1 + 2
                MesEventoini = info_evento[index1:index2]
                index1 = info_evento.find("Realizado el:") + 13
                index2 = index1 + 10
                FechaEventoini = info_evento[index1:index2]
                index1 = info_evento.find(",",index1,index1 + 58) + 48
                index2 = index1 + 4
                AnoEventofin = info_evento[index1:index2]
                if AnoEventofin == " \xa0\r\n" or AnoEventofin == ",":
                    MesEventofin = "-"
                    AnoEventofin = "-"
                    FechaEventofin = "-"
                else:
                    index1 = index1 + 5
                    index2 = index1 + 2
                    MesEventofin = info_evento[index1:index2]
                    index1 = info_evento.find("Realizado el:") + 13
                    index1 = info_evento.find(",",index1,index1 + 58) + 48
                    index2 = index1 + 10
                    FechaEventofin = info_evento[index1:index2]
            #Lugar Evento
            index1 = info_evento.find(" \xa0\r\n                                            en ") + 51
            index2 = info_evento.find(" \xa0 -  \xa0\r\n")
            LugarEvento = info_evento[index1:index2]
            b_eventos = cont.findAll("td")
            #Autores
            autores = b_eventos[3].findAll("li")
            if len(autores) == 0:
                auto = "-";
                vincula = "-";
            else:
                for z in range(0, len(autores)):
                    autor = autores[z].text
                    index1 = autor.find("Nombre:") + 8
                    index2= autor.find("\r\n                                                Rol en el evento: ")
                    if len(auto) == 0:
                        auto = autor[index1:index2]
                    else:
                        auto = auto + ", " + autor[index1:index2]
                    index1 = autor.find("Rol en el evento: ") + 18
                    index2= autor.find("\r\n ",index1,len(autor))
                    if len(vincula) == 0:
                        vincula = autor[index1:index2]
                    else:
                        vincula = vincula + ", " + autor[index1:index2]


            #Instituciones
            Instituciones = b_eventos[2].findAll("li")
            if len(Instituciones) == 0:
                insti = "-";
                vinculain = "-";
            else:
                for z in range(0, len(Instituciones)):
                    institu = Instituciones[z].text
                    index1 = institu.find("Nombre de la institución:") + 25
                    index2= institu.find("\r\n                                                Tipo de vinculación")
                    if len(insti) == 0:
                        insti = institu[index1:index2]
                    else:
                        insti = insti + ", " + institu[index1:index2]
                    index1 = institu.find("Tipo de vinculación") + 19
                    index2 = institu.find("'",index1,len(institu))
                    if len(vinculain) == 0:
                        vinculain = institu[index1:index2]
                    else:
                        vinculain = vinculain + ", " + institu[index1:index2]


            #Productos Asociados
            productos = b_eventos[1].findAll("li")
            if len(productos) == 0:
                init.RE_PERSONA_PRODUCTO.append(RH + ";"\
                + str(COD_PRODUCTO) + ";"\
                + "" + ";"\
                + "" + ";"\
                + NombreEvento.strip().replace(";" , "|").replace("\r\n","") + ";" \
                + "" + ";" \
                + LugarEvento.strip().replace(";" , "|").replace("\r\n","") + ";" \
                + AnoEventoini.strip() + ";" \
                + Ambito.strip().replace(";" , "|").replace("\r\n","") + ";"
                + "" + ";" \
                + "" + ";" \
                + "" + ";" \
                + auto.strip().replace(";" , "|").replace("\r\n","") + ";" \
                + vincula.strip().replace(";" , "|").replace("\r\n","") + ";" \
                + "" + ";" \
                + "" + ";" \
                + "" + ";" \
                + "" + ";" \
                + "" + ";" \
                + insti.strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")  + ";" \
                + vinculain.strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","") \
                + "\n")
                init.APROPIACION.append(RH + ";"\
                + str(COD_PRODUCTO) + ";"\
                + TipoEvento.strip() + ";" \
                + "" + ";" \
                + FechaEventoini.strip() + ";" \
                + AnoEventoini.strip() + ";" \
                + MesEventoini.strip() + ";" \
                + FechaEventofin.strip() + ";" \
                + AnoEventofin.strip() + ";" \
                + MesEventofin.strip() \
                + "\n")
                COD_PRODUCTO = COD_PRODUCTO + 1
            else:
                for y in range(0, len(productos)):
                    prod = productos[y].text
                    index1 = prod.find("Nombre del producto:") + 20
                    index2 = prod.find("Tipo de producto:")
                    NombreProducto = prod[index1:index2]
                    index1 = prod.find("Tipo de producto:") + 17
                    index2 = prod.find("\r\n",index1,len(prod))
                    Tipopub = prod[index1:index2]
                    init.RE_PERSONA_PRODUCTO.append(RH + ";"\
                    + str(COD_PRODUCTO) + ";"\
                    + Tipopub.strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","") + ";" \
                    + NombreProducto.strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","") + ";" \
                    + NombreEvento.strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")  + ";" \
                    + "" + ";" \
                    + LugarEvento.strip().replace(";" , "|").replace("\r\n","") + ";" \
                    + AnoEventofin.strip() + ";" \
                    + Ambito.strip().replace(";" , "|").replace("\r\n","") + ";" \
                    + "" + ";" \
                    + "" + ";" \
                    + "" + ";" \
                    + auto.strip().replace(";" , "|").replace("\r\n","") + ";" \
                    + vincula.strip().replace(";" , "|").replace("\r\n","") + ";" \
                    + "" + ";" \
                    + "" + ";" \
                    + "" + ";" \
                    + "" + ";" \
                    + "" + ";" \
                    + insti.strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")  + ";" \
                    + vinculain.strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","") \
                    + "\n")
                    init.APROPIACION.append(RH + ";"\
                    + str(COD_PRODUCTO) + ";"\
                    + TipoEvento.strip() + ";" \
                    + "" + ";" \
                    + FechaEventoini.strip() + ";" \
                    + AnoEventoini.strip() + ";" \
                    + MesEventoini.strip() + ";" \
                    + FechaEventofin.strip() + ";" \
                    + AnoEventofin.strip() + ";" \
                    + MesEventofin.strip() \
                    + "\n")
                    COD_PRODUCTO = COD_PRODUCTO + 1

                    
            auto = ""
            vincula = ""
            insti = ""
            vinculain = ""


    else:
        print("El Docente ",name," ",last," ","no tiene Eventos Asociados")
