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

def ptdiseñoextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
    global contptdiseño
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
        buscaptdiseño = containers[a].h3
        #print(buscaptdiseño)
        try:
            if buscaptdiseño.text == "Diseño industrial":
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
            info_ptdiseño = cont.text
            #Tipo Otra Produccion
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Producción técnica - Diseño Industrial":
                tipo = "40"
            # elif tipo.strip() == "Producción técnica - Productos tecnológicos - Coleccion biologica de referencia con informacion sistematizada":
            #     tipo = "37"
            else:
                print(tipo)
            #Nombre Producto
            index = info_ptdiseño.find('Nombre comercial:')
            index = info_ptdiseño.rfind(',',0,index)
            index1 = info_ptdiseño.rfind(',',0,index) + 2
            index2 = info_ptdiseño.find(',',index1 + 1,len(info_ptdiseño))
            NombreProducto = info_ptdiseño[index1:index2]
            #Coautores
            index2 = index1
            index1 = 1
            coautores = info_ptdiseño[index1:index2]
            #Nombre Comercial
            index1 = info_ptdiseño.find('Nombre comercial:') + 18
            index2 = info_ptdiseño.find(',',index1,len(info_ptdiseño))
            NombreComercial = info_ptdiseño[index1:index2]
            #Contrato / Registro
            index1 = info_ptdiseño.find('contrato/registro:') + 19
            index2 = info_ptdiseño.find(',',index1,len(info_ptdiseño))
            Registro = info_ptdiseño[index1:index2]
            #Lugar
            index1 = info_ptdiseño.find('En: ') + 4
            index2 = info_ptdiseño.find(',\xa0\r\n                    ',index1,len(info_ptdiseño))
            lugar = info_ptdiseño[index1:index2]
            if lugar == ". ":
                lugar = ""
            #Año
            index = info_ptdiseño.find("En:")
            index = info_ptdiseño.find(",",index,len(info_ptdiseño)) +1
            index1 = info_ptdiseño.find(',',index,len(info_ptdiseño)) +1
            index2 = info_ptdiseño.find(',',index1,len(info_ptdiseño))
            Anoptdiseño = info_ptdiseño[index1:index2]
            #Palabras
            index1 = info_ptdiseño.find("Palabras:")
            index2 = info_ptdiseño.find("Areas:")
            index3 = info_ptdiseño.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_ptdiseño[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_ptdiseño[index1 + 9:index3]
            else:
                palabras = info_ptdiseño[index1 + 9:len(info_ptdiseño)]
            #Areas
            index1 = info_ptdiseño.find("Areas:")
            index2 = info_ptdiseño.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_ptdiseño[index1 + 6:index2]
            else:
                areas = info_ptdiseño[index1 + 6:len(info_ptdiseño)]
            #Sectores
            index1 = info_ptdiseño.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_ptdiseño[index1 + 9:len(info_ptdiseño)]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',lugar.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Anoptdiseño.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
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
        print("El Docente ",name," ",last," ","no tiene Diseños Industriales Asociados")
    contptdiseño = [COD_PRODUCTO]

def ptcircuitosextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
    global contptcircuitos
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
        buscaptcircuitos = containers[a].h3
        #print(buscaptcircuitos)
        try:
            if buscaptcircuitos.text == "Esquemas de trazado de circuitos integrados":
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
            info_ptcircuitos = cont.text
            #Tipo Otra Produccion
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Producción técnica - Esquema de circuito integrado":
                tipo = "41"
            # elif tipo.strip() == "Producción técnica - Productos tecnológicos - Coleccion biologica de referencia con informacion sistematizada":
            #     tipo = "37"
            else:
                print(tipo)
            #Nombre Producto
            index = info_ptcircuitos.find('Nombre comercial:')
            index = info_ptcircuitos.rfind(',',0,index)
            index1 = info_ptcircuitos.rfind(',',0,index) + 2
            index2 = info_ptcircuitos.find(',',index1 + 1,len(info_ptcircuitos))
            NombreProducto = info_ptcircuitos[index1:index2]
            #Coautores
            index2 = index1
            index1 = 1
            coautores = info_ptcircuitos[index1:index2]
            #Nombre Comercial
            index1 = info_ptcircuitos.find('Nombre comercial:') + 18
            index2 = info_ptcircuitos.find(',',index1,len(info_ptcircuitos))
            NombreComercial = info_ptcircuitos[index1:index2]
            #Contrato / Registro
            index1 = info_ptcircuitos.find('contrato/registro:') + 19
            index2 = info_ptcircuitos.find(',',index1,len(info_ptcircuitos))
            Registro = info_ptcircuitos[index1:index2]
            #Lugar
            index1 = info_ptcircuitos.find('En: ') + 4
            index2 = info_ptcircuitos.find(',\xa0\r\n                    ',index1,len(info_ptcircuitos))
            lugar = info_ptcircuitos[index1:index2]
            if lugar == ". ":
                lugar = ""
            #Año
            index = info_ptcircuitos.find("En:")
            index = info_ptcircuitos.find(",",index,len(info_ptcircuitos)) +1
            index1 = info_ptcircuitos.find(',',index,len(info_ptcircuitos)) +1
            index2 = info_ptcircuitos.find(',',index1,len(info_ptcircuitos))
            Anoptcircuitos = info_ptcircuitos[index1:index2]
            #Palabras
            index1 = info_ptcircuitos.find("Palabras:")
            index2 = info_ptcircuitos.find("Areas:")
            index3 = info_ptcircuitos.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_ptcircuitos[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_ptcircuitos[index1 + 9:index3]
            else:
                palabras = info_ptcircuitos[index1 + 9:len(info_ptcircuitos)]
            #Areas
            index1 = info_ptcircuitos.find("Areas:")
            index2 = info_ptcircuitos.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_ptcircuitos[index1 + 6:index2]
            else:
                areas = info_ptcircuitos[index1 + 6:len(info_ptcircuitos)]
            #Sectores
            index1 = info_ptcircuitos.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_ptcircuitos[index1 + 9:len(info_ptcircuitos)]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',lugar.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Anoptcircuitos.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
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
        print("El Docente ",name," ",last," ","no tiene Esquemas de Circuitos Asociados")
    contptcircuitos = [COD_PRODUCTO]

def ptinnovaextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
    global contptinnova
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
        buscaptinnova = containers[a].h3
        #print(buscaptinnova)
        try:
            if buscaptinnova.text == "Innovación generada en la gestión empresarial":
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
            info_ptinnova = cont.text
            #Tipo Otra Produccion
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Producción técnica - Innovaciones generadas de producción empresarial - Organizacional":
                tipo = "42"
            elif tipo.strip() == "Producción técnica - Innovaciones generadas de producción empresarial - Empresarial":
                tipo = "43"
            else:
                print(tipo)
            #Nombre Producto
            index = info_ptinnova.find('Nombre comercial:')
            index = info_ptinnova.rfind(',',0,index)
            index1 = info_ptinnova.rfind(',',0,index) + 2
            index2 = info_ptinnova.find(',',index1 + 1,len(info_ptinnova))
            NombreProducto = info_ptinnova[index1:index2]
            #Coautores
            index2 = index1
            index1 = 1
            coautores = info_ptinnova[index1:index2]
            #Nombre Comercial
            index1 = info_ptinnova.find('Nombre comercial:') + 18
            index2 = info_ptinnova.find(',',index1,len(info_ptinnova))
            NombreComercial = info_ptinnova[index1:index2]
            #Contrato / Registro
            index1 = info_ptinnova.find('contrato/registro:') + 19
            index2 = info_ptinnova.find(',',index1,len(info_ptinnova))
            Registro = info_ptinnova[index1:index2]
            #Lugar
            index1 = info_ptinnova.find('En: ') + 4
            index2 = info_ptinnova.find(',\xa0\r\n                    ',index1,len(info_ptinnova))
            lugar = info_ptinnova[index1:index2]
            if lugar == ". ":
                lugar = ""
            #Año
            index = info_ptinnova.find("En:")
            index = info_ptinnova.find(",",index,len(info_ptinnova)) +1
            index1 = info_ptinnova.find(',',index,len(info_ptinnova)) +1
            index2 = info_ptinnova.find(',',index1,len(info_ptinnova))
            Anoptinnova = info_ptinnova[index1:index2]
            #Palabras
            index1 = info_ptinnova.find("Palabras:")
            index2 = info_ptinnova.find("Areas:")
            index3 = info_ptinnova.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_ptinnova[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_ptinnova[index1 + 9:index3]
            else:
                palabras = info_ptinnova[index1 + 9:len(info_ptinnova)]
            #Areas
            index1 = info_ptinnova.find("Areas:")
            index2 = info_ptinnova.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_ptinnova[index1 + 6:index2]
            else:
                areas = info_ptinnova[index1 + 6:len(info_ptinnova)]
            #Sectores
            index1 = info_ptinnova.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_ptinnova[index1 + 9:len(info_ptinnova)]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',lugar.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Anoptinnova.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
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
        print("El Docente ",name," ",last," ","no tiene Innovaciones en Empresas Asociadas")
    contptinnova = [COD_PRODUCTO]

def ptvaranimalextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
    global contptvaranimal
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
        buscaptvaranimal = containers[a].h3
        #print(buscaptvaranimal)
        try:
            if buscaptvaranimal.text == "Variedad animal":
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
            info_ptvaranimal = cont.text
            #Tipo Otra Produccion
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Producción técnica - Variedad animal":
                tipo = "44"
            # elif tipo.strip() == "Producción técnica - Innovaciones generadas de producción empresarial - Empresarial":
            #     tipo = "43"
            else:
                print(tipo)
            #Nombre Producto
            index = info_ptvaranimal.find('Nombre comercial:')
            index = info_ptvaranimal.rfind(',',0,index)
            index1 = info_ptvaranimal.rfind(',',0,index) + 2
            index2 = info_ptvaranimal.find(',',index1 + 1,len(info_ptvaranimal))
            NombreProducto = info_ptvaranimal[index1:index2]
            #Coautores
            index2 = index1
            index1 = 1
            coautores = info_ptvaranimal[index1:index2]
            #Nombre Comercial
            index1 = info_ptvaranimal.find('Nombre comercial:') + 18
            index2 = info_ptvaranimal.find(',',index1,len(info_ptvaranimal))
            NombreComercial = info_ptvaranimal[index1:index2]
            #Contrato / Registro
            index1 = info_ptvaranimal.find('contrato/registro:') + 19
            index2 = info_ptvaranimal.find(',',index1,len(info_ptvaranimal))
            Registro = info_ptvaranimal[index1:index2]
            #Lugar
            index1 = info_ptvaranimal.find('En: ') + 4
            index2 = info_ptvaranimal.find(',\xa0\r\n                    ',index1,len(info_ptvaranimal))
            lugar = info_ptvaranimal[index1:index2]
            if lugar == ". ":
                lugar = ""
            #Año
            index = info_ptvaranimal.find("En:")
            index = info_ptvaranimal.find(",",index,len(info_ptvaranimal)) +1
            index1 = info_ptvaranimal.find(',',index,len(info_ptvaranimal)) +1
            index2 = info_ptvaranimal.find(',',index1,len(info_ptvaranimal))
            Anoptvaranimal = info_ptvaranimal[index1:index2]
            #Palabras
            index1 = info_ptvaranimal.find("Palabras:")
            index2 = info_ptvaranimal.find("Areas:")
            index3 = info_ptvaranimal.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_ptvaranimal[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_ptvaranimal[index1 + 9:index3]
            else:
                palabras = info_ptvaranimal[index1 + 9:len(info_ptvaranimal)]
            #Areas
            index1 = info_ptvaranimal.find("Areas:")
            index2 = info_ptvaranimal.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_ptvaranimal[index1 + 6:index2]
            else:
                areas = info_ptvaranimal[index1 + 6:len(info_ptvaranimal)]
            #Sectores
            index1 = info_ptvaranimal.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_ptvaranimal[index1 + 9:len(info_ptvaranimal)]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',lugar.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Anoptvaranimal.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
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
        print("El Docente ",name," ",last," ","no tiene Variedades Animales Registradas")
    contptvaranimal = [COD_PRODUCTO]

def ptprocesoextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
    global contptproceso
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
        buscaptproceso = containers[a].h3
        #print(buscaptproceso)
        try:
            if buscaptproceso.text == "Innovación de proceso o procedimiento":
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
            info_ptproceso = cont.text
            #Tipo Otra Produccion
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Producción técnica - Innovación de proceso o procedimiento":
                tipo = "45"
            # elif tipo.strip() == "Producción técnica - Innovaciones generadas de producción empresarial - Empresarial":
            #     tipo = "43"
            else:
                print(tipo)
            #Nombre Producto
            index = info_ptproceso.find('Nombre comercial:')
            index = info_ptproceso.rfind(',',0,index)
            index1 = info_ptproceso.rfind(',',0,index) + 2
            index2 = info_ptproceso.find(',',index1 + 1,len(info_ptproceso))
            NombreProducto = info_ptproceso[index1:index2]
            #Coautores
            index2 = index1
            index1 = 1
            coautores = info_ptproceso[index1:index2]
            #Nombre Comercial
            index1 = info_ptproceso.find('Nombre comercial:') + 18
            index2 = info_ptproceso.find(',',index1,len(info_ptproceso))
            NombreComercial = info_ptproceso[index1:index2]
            #Contrato / Registro
            index1 = info_ptproceso.find('contrato/registro:') + 19
            index2 = info_ptproceso.find(',',index1,len(info_ptproceso))
            Registro = info_ptproceso[index1:index2]
            #Lugar
            index1 = info_ptproceso.find('En: ') + 4
            index2 = info_ptproceso.find(',\xa0\r\n                    ',index1,len(info_ptproceso))
            lugar = info_ptproceso[index1:index2]
            if lugar == ". ":
                lugar = ""
            #Año
            index = info_ptproceso.find("En:")
            index = info_ptproceso.find(",",index,len(info_ptproceso)) +1
            index1 = info_ptproceso.find(',',index,len(info_ptproceso)) +1
            index2 = info_ptproceso.find(',',index1,len(info_ptproceso))
            Anoptproceso = info_ptproceso[index1:index2]
            #Palabras
            index1 = info_ptproceso.find("Palabras:")
            index2 = info_ptproceso.find("Areas:")
            index3 = info_ptproceso.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_ptproceso[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_ptproceso[index1 + 9:index3]
            else:
                palabras = info_ptproceso[index1 + 9:len(info_ptproceso)]
            #Areas
            index1 = info_ptproceso.find("Areas:")
            index2 = info_ptproceso.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_ptproceso[index1 + 6:index2]
            else:
                areas = info_ptproceso[index1 + 6:len(info_ptproceso)]
            #Sectores
            index1 = info_ptproceso.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_ptproceso[index1 + 9:len(info_ptproceso)]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',lugar.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Anoptproceso.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
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
        print("El Docente ",name," ",last," ","no tiene Innovaciones en Procesos Registradas")
    contptproceso = [COD_PRODUCTO]

def ptcartasextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
    global contptcartas
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
        buscaptcartas = containers[a].h3
        #print(buscaptcartas)
        try:
            if buscaptcartas.text == "Cartas, mapas y similares":
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
            info_ptcartas = cont.text
            #Tipo Otra Produccion
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Producción técnica - Cartas, mapas o similares - Aerofotograma":
                tipo = "46"
            elif tipo.strip() == "Producción técnica - Cartas, mapas o similares - Carta":
                tipo = "47"
            elif tipo.strip() == "Producción técnica - Cartas, mapas o similares - Fotograma":
                tipo = "48"
            elif tipo.strip() == "Producción técnica - Cartas, mapas o similares - Mapa":
                tipo = "49"
            elif tipo.strip() == "Producción técnica - Cartas, mapas o similares - Otra":
                tipo = "50"
            else:
                print(tipo)
            #Nombre Producto
            index = info_ptcartas.find('Nombre comercial:')
            index = info_ptcartas.rfind(',',0,index)
            index1 = info_ptcartas.rfind(',',0,index) + 2
            index2 = info_ptcartas.find(',',index1 + 1,len(info_ptcartas))
            NombreProducto = info_ptcartas[index1:index2]
            #Coautores
            index2 = index1
            index1 = 1
            coautores = info_ptcartas[index1:index2]
            #Nombre Comercial
            index1 = info_ptcartas.find('Nombre comercial:') + 18
            index2 = info_ptcartas.find(',',index1,len(info_ptcartas))
            NombreComercial = info_ptcartas[index1:index2]
            #Contrato / Registro
            index1 = info_ptcartas.find('contrato/registro:') + 19
            index2 = info_ptcartas.find(',',index1,len(info_ptcartas))
            Registro = info_ptcartas[index1:index2]
            #Lugar
            index1 = info_ptcartas.find('En: ') + 4
            index2 = info_ptcartas.find(',\xa0\r\n                    ',index1,len(info_ptcartas))
            lugar = info_ptcartas[index1:index2]
            if lugar == ". ":
                lugar = ""
            #Año
            index = info_ptcartas.find("En:")
            index = info_ptcartas.find(",",index,len(info_ptcartas)) +1
            index1 = info_ptcartas.find(',',index,len(info_ptcartas)) +1
            index2 = info_ptcartas.find(',',index1,len(info_ptcartas))
            Anoptcartas = info_ptcartas[index1:index2]
            #Palabras
            index1 = info_ptcartas.find("Palabras:")
            index2 = info_ptcartas.find("Areas:")
            index3 = info_ptcartas.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_ptcartas[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_ptcartas[index1 + 9:index3]
            else:
                palabras = info_ptcartas[index1 + 9:len(info_ptcartas)]
            #Areas
            index1 = info_ptcartas.find("Areas:")
            index2 = info_ptcartas.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_ptcartas[index1 + 6:index2]
            else:
                areas = info_ptcartas[index1 + 6:len(info_ptcartas)]
            #Sectores
            index1 = info_ptcartas.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_ptcartas[index1 + 9:len(info_ptcartas)]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',lugar.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Anoptcartas.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
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
        print("El Docente ",name," ",last," ","no tiene Cartas o Mapas Registrados")
    contptcartas = [COD_PRODUCTO]
