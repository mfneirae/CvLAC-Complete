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
def ptsoftwareextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
    global contptsoftware
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
        buscaptsoftware = containers[a].h3
        #print(buscaptsoftware)
        try:
            if buscaptsoftware.text == "Softwares":
                all = a
                #print(all)
                break
        except AttributeError:
            pass

    if all != 0:
        containerb = containers[all]
        container = containerb.findAll("blockquote")
        tipotexno = containerb.findAll("li")
        for x in range(0, len(container)):
            cont = container[x]
            info_ptsoftware = cont.text
            #Tipo Otra Produccion
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Producción técnica - Softwares - Computacional":
                tipo = "35"
            # elif tipo.strip() == "Producción bibliográfica - Otra producción bibliográfica - Prólogo":
            #     tipo = "32"
            else:
                print(tipo)
            #Nombre Producto
            index = info_ptsoftware.find('Nombre comercial:')
            index = info_ptsoftware.rfind(',',0,index)
            index1 = info_ptsoftware.rfind(',',0,index) + 2
            index2 = info_ptsoftware.find(',',index1 + 1,len(info_ptsoftware))
            NombreProducto = info_ptsoftware[index1:index2]
            #Coautores
            index2 = index1
            index1 = 1
            coautores = info_ptsoftware[index1:index2]
            #Nombre Comercial
            index1 = info_ptsoftware.find('Nombre comercial:') + 18
            index2 = info_ptsoftware.find(',',index1,len(info_ptsoftware))
            NombreComercial = info_ptsoftware[index1:index2]
            #Contrato / Registro
            index1 = info_ptsoftware.find('contrato/registro:') + 19
            index2 = info_ptsoftware.find(',',index1,len(info_ptsoftware))
            Registro = info_ptsoftware[index1:index2]
            #Plataforma
            index1 = info_ptsoftware.find('plataforma:') + 12
            index2 = info_ptsoftware.find(',',index1,len(info_ptsoftware))
            Plataforma = info_ptsoftware[index1:index2]
            #Ambiente
            index1 = info_ptsoftware.find('ambiente:') + 10
            index2 = info_ptsoftware.find(',',index1,len(info_ptsoftware))
            Ambiente = info_ptsoftware[index1:index2]
            #Lugar
            index1 = info_ptsoftware.find('En: ') + 4
            index2 = info_ptsoftware.find(',\xa0\r\n                    ',index1,len(info_ptsoftware))
            lugar = info_ptsoftware[index1:index2]
            if lugar == ". ":
                lugar = ""
            #Año
            index = info_ptsoftware.find("En:")
            index = info_ptsoftware.find(",",index,len(info_ptsoftware)) +1
            index1 = info_ptsoftware.find(',',index,len(info_ptsoftware)) +1
            index2 = info_ptsoftware.find(',',index1,len(info_ptsoftware))
            Anoptsoftware = info_ptsoftware[index1:index2]
            #Palabras
            index1 = info_ptsoftware.find("Palabras:")
            index2 = info_ptsoftware.find("Areas:")
            index3 = info_ptsoftware.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_ptsoftware[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_ptsoftware[index1 + 9:index3]
            else:
                palabras = info_ptsoftware[index1 + 9:len(info_ptsoftware)]
            #Areas
            index1 = info_ptsoftware.find("Areas:")
            index2 = info_ptsoftware.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_ptsoftware[index1 + 6:index2]
            else:
                areas = info_ptsoftware[index1 + 6:len(info_ptsoftware)]
            #Sectores
            index1 = info_ptsoftware.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_ptsoftware[index1 + 9:len(info_ptsoftware)]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',lugar.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Anoptsoftware.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + re.sub(' +',' ',palabras.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',areas.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',sectores.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',coautores.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" \
            + "\n")
            init.PROD_TECNICA.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + re.sub(' +',' ',NombreComercial.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Registro.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',Plataforma.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Ambiente.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        print("El Docente ",name," ",last," ","no tiene Sofwares Asociadas")
    contptsoftware = [COD_PRODUCTO]

def ptproductoextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
    global contptproducto
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
        buscaptproducto = containers[a].h3
        #print(buscaptproducto)
        try:
            if buscaptproducto.text == "Productos tecnológicos":
                all = a
                #print(all)
                break
        except AttributeError:
            pass

    if all != 0:
        containerb = containers[all]
        container = containerb.findAll("blockquote")
        tipotexno = containerb.findAll("li")
        for x in range(0, len(container)):
            cont = container[x]
            info_ptproducto = cont.text
            #Tipo Otra Produccion
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Producción técnica - Productos tecnológicos - Gen Clonado":
                tipo = "36"
            elif tipo.strip() == "Producción técnica - Productos tecnológicos - Coleccion biologica de referencia con informacion sistematizada":
                tipo = "37"
            elif tipo.strip() == "Producción técnica - Productos tecnológicos - Otro":
                tipo = "38"
            elif tipo.strip() == "Producción técnica - Productos tecnológicos - Base de datos de referencia para investigación":
                tipo = "39"
            else:
                print(tipo)
            #Nombre Producto
            index = info_ptproducto.find('Nombre comercial:')
            index = info_ptproducto.rfind(',',0,index)
            index1 = info_ptproducto.rfind(',',0,index) + 2
            index2 = info_ptproducto.find(',',index1 + 1,len(info_ptproducto))
            NombreProducto = info_ptproducto[index1:index2]
            #Coautores
            index2 = index1
            index1 = 1
            coautores = info_ptproducto[index1:index2]
            #Nombre Comercial
            index1 = info_ptproducto.find('Nombre comercial:') + 18
            index2 = info_ptproducto.find(',',index1,len(info_ptproducto))
            NombreComercial = info_ptproducto[index1:index2]
            #Contrato / Registro
            index1 = info_ptproducto.find('contrato/registro:') + 19
            index2 = info_ptproducto.find(',',index1,len(info_ptproducto))
            Registro = info_ptproducto[index1:index2]
            #Lugar
            index1 = info_ptproducto.find('En: ') + 4
            index2 = info_ptproducto.find(',\xa0\r\n                    ',index1,len(info_ptproducto))
            lugar = info_ptproducto[index1:index2]
            if lugar == ". ":
                lugar = ""
            #Año
            index = info_ptproducto.find("En:")
            index = info_ptproducto.find(",",index,len(info_ptproducto)) +1
            index1 = info_ptproducto.find(',',index,len(info_ptproducto)) +1
            index2 = info_ptproducto.find(',',index1,len(info_ptproducto))
            Anoptproducto = info_ptproducto[index1:index2]
            #Palabras
            index1 = info_ptproducto.find("Palabras:")
            index2 = info_ptproducto.find("Areas:")
            index3 = info_ptproducto.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_ptproducto[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_ptproducto[index1 + 9:index3]
            else:
                palabras = info_ptproducto[index1 + 9:len(info_ptproducto)]
            #Areas
            index1 = info_ptproducto.find("Areas:")
            index2 = info_ptproducto.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_ptproducto[index1 + 6:index2]
            else:
                areas = info_ptproducto[index1 + 6:len(info_ptproducto)]
            #Sectores
            index1 = info_ptproducto.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_ptproducto[index1 + 9:len(info_ptproducto)]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',lugar.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Anoptproducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + re.sub(' +',' ',palabras.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',areas.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',sectores.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',coautores.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" \
            + "\n")
            init.PROD_TECNICA.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + re.sub(' +',' ',NombreComercial.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Registro.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        print("El Docente ",name," ",last," ","no tiene Producción Técnica Asociadas")
    contptproducto = [COD_PRODUCTO]
