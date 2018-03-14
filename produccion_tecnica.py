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
            elif tipo.strip() == "Producción técnica - Softwares - Multimedia":
                tipo = "72"
            elif tipo.strip() == "Producción técnica - Softwares - Otra":
                tipo = "73"
            else:
                print("ALERTA: "+tipo)
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
            elif tipo.strip() == "Producción técnica - Productos tecnológicos - Base de datos de referencia para investigacion":
                tipo = "39"
            else:
                print("ALERTA: "+tipo)
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
                print("ALERTA: "+tipo)
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
                print("ALERTA: "+tipo)
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
                print("ALERTA: "+tipo)
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
                print("ALERTA: "+tipo)
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
                print("ALERTA: "+tipo)
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
                print("ALERTA: "+tipo)
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

def ptvegetalextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
    global contptvegetal
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
        buscaptvegetal = containers[a].h3
        #print(buscaptvegetal)
        try:
            if buscaptvegetal.text == "Variedad vegetal":
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
            info_ptvegetal = cont.text
            #Tipo Otra Produccion
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Producción técnica - Variedad vegetal":
                tipo = "51"
            # elif tipo.strip() == "Producción técnica - Cartas, mapas o similares - Otra":
            #     tipo = "50"
            else:
                print("ALERTA: "+tipo)
            #Nombre Producto
            index = info_ptvegetal.find('Ciclo:')
            index = info_ptvegetal.rfind(',',0,index)
            index1 = info_ptvegetal.rfind(',',0,index) + 2
            index2 = info_ptvegetal.find(',',index1 + 1,len(info_ptvegetal))
            NombreProducto = info_ptvegetal[index1:index2]
            #Coautores
            index2 = index1
            index1 = 1
            coautores = info_ptvegetal[index1:index2]
            #Nombre Comercial
            index1 = info_ptvegetal.find('Nombre comercial:') + 18
            index2 = info_ptvegetal.find(',',index1,len(info_ptvegetal))
            NombreComercial = info_ptvegetal[index1:index2]
            #Ciclo
            index1 = info_ptvegetal.find('Ciclo:') + 6
            index2 = info_ptvegetal.find(',',index1,len(info_ptvegetal))
            Ciclo = info_ptvegetal[index1:index2]
            #Variedad
            index1 = info_ptvegetal.find('Estado de la variedad:') + 23
            index2 = info_ptvegetal.find(',',index1,len(info_ptvegetal))
            Variedad = info_ptvegetal[index1:index2]
            #Contrato / Registro
            index1 = info_ptvegetal.find('contrato/registro:') + 19
            index2 = info_ptvegetal.find(',',index1,len(info_ptvegetal))
            Registro = info_ptvegetal[index1:index2]
            #Lugar
            index1 = info_ptvegetal.find('En: ') + 4
            index2 = info_ptvegetal.find(',\xa0\r\n                    ',index1,len(info_ptvegetal))
            lugar = info_ptvegetal[index1:index2]
            if lugar == ". ":
                lugar = ""
            #Año
            index = info_ptvegetal.find("En:")
            index = info_ptvegetal.find(",",index,len(info_ptvegetal)) +1
            index1 = info_ptvegetal.find(',',index,len(info_ptvegetal)) +1
            index2 = info_ptvegetal.find(',',index1,len(info_ptvegetal))
            Anoptvegetal = info_ptvegetal[index1:index2]
            #Palabras
            index1 = info_ptvegetal.find("Palabras:")
            index2 = info_ptvegetal.find("Areas:")
            index3 = info_ptvegetal.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_ptvegetal[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_ptvegetal[index1 + 9:index3]
            else:
                palabras = info_ptvegetal[index1 + 9:len(info_ptvegetal)]
            #Areas
            index1 = info_ptvegetal.find("Areas:")
            index2 = info_ptvegetal.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_ptvegetal[index1 + 6:index2]
            else:
                areas = info_ptvegetal[index1 + 6:len(info_ptvegetal)]
            #Sectores
            index1 = info_ptvegetal.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_ptvegetal[index1 + 9:len(info_ptvegetal)]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',lugar.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Anoptvegetal.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
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
            + re.sub(' +',' ',Ciclo.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Variedad.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        print("El Docente ",name," ",last," ","no tiene Variedades Vegetales Registradas")
    contptvegetal = [COD_PRODUCTO]

def pttratecextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
    global contpttratec
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
        buscapttratec = containers[a].h3
        #print(buscapttratec)
        try:
            if buscapttratec.text == "Trabajos técnicos":
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
            info_pttratec = cont.text
            #Tipo Otra Produccion
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Servicios de proyectos de IDI":
                tipo = "52"
            elif tipo.strip() == "Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Comercialización de tecnología":
                tipo = "53"
            elif tipo.strip() == "Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Análisis de competitividad":
                tipo = "54"
            elif tipo.strip() == "Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Informe técnico":
                tipo = "55"
            elif tipo.strip() == "Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Otra":
                tipo = "56"
            elif tipo.strip() == "Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Acciones de transferencia tecnológica":
                tipo = "57"
            elif tipo.strip() == "Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Desarrollo de productos":
                tipo = "58"
            elif tipo.strip() == "Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Implementación de sistemas de análisis":
                tipo = "59"
            elif tipo.strip() == "Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Consultoría en artes,arquitectura y diseño":
                tipo = "60"
            elif tipo.strip() == "Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Servicios de Proyectos de I+D+I":
                tipo = "76"
            else:
                print("ALERTA: "+tipo)
            #Nombre Producto
            index = info_pttratec.find('Nombre comercial:')
            index = info_pttratec.rfind(',',0,index)
            index1 = info_pttratec.rfind(',',0,index) + 2
            index2 = info_pttratec.find(',',index1 + 1,len(info_pttratec))
            NombreProducto = info_pttratec[index1:index2]
            #Coautores
            index2 = index1
            index1 = 1
            coautores = info_pttratec[index1:index2]
            #Nombre Comercial
            index1 = info_pttratec.find('Nombre comercial:') + 18
            index2 = info_pttratec.find(',',index1,len(info_pttratec))
            NombreComercial = info_pttratec[index1:index2]
            #Paginas
            Paginas = ""
            #Duración
            index = info_pttratec.find('En:')
            index = info_pttratec.find(',',index,len(info_pttratec)) + 1
            index = info_pttratec.find(',',index,len(info_pttratec)) + 1
            index1 = info_pttratec.find(',',index,len(info_pttratec)) + 1
            index2 = info_pttratec.find('p.')
            Duracion = info_pttratec[index1:index2]
            #Contrato / Registro
            index1 = info_pttratec.find('contrato/registro:') + 19
            index2 = info_pttratec.find(',',index1,len(info_pttratec))
            Registro = info_pttratec[index1:index2]
            #Lugar
            index1 = info_pttratec.find('En: ') + 4
            index2 = info_pttratec.find(',\xa0\r\n                    ',index1,len(info_pttratec))
            lugar = info_pttratec[index1:index2]
            if lugar == ". ":
                lugar = ""
            #Año
            index = info_pttratec.find("En:")
            index = info_pttratec.find(",",index,len(info_pttratec)) +1
            index1 = info_pttratec.find(',',index,len(info_pttratec)) +1
            index2 = info_pttratec.find(',',index1,len(info_pttratec))
            Anopttratec = info_pttratec[index1:index2]
            #Palabras
            index1 = info_pttratec.find("Palabras:")
            index2 = info_pttratec.find("Areas:")
            index3 = info_pttratec.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_pttratec[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_pttratec[index1 + 9:index3]
            else:
                palabras = info_pttratec[index1 + 9:len(info_pttratec)]
            #Areas
            index1 = info_pttratec.find("Areas:")
            index2 = info_pttratec.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_pttratec[index1 + 6:index2]
            else:
                areas = info_pttratec[index1 + 6:len(info_pttratec)]
            #Sectores
            index1 = info_pttratec.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_pttratec[index1 + 9:len(info_pttratec)]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',lugar.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Anopttratec.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + re.sub(' +',' ',palabras.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',areas.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',sectores.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',coautores.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',Paginas.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
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
            + re.sub(' +',' ',Duracion.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        print("El Docente ",name," ",last," ","no tiene Trabajos Técnicos Registradas")
    contpttratec = [COD_PRODUCTO]

def ptnormaextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
    global contptnorma
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
        buscaptnorma = containers[a].h3
        #print(buscaptnorma)
        try:
            if buscaptnorma.text == "Normas y Regulaciones":
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
            info_ptnorma = cont.text
            #Tipo Otra Produccion
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Producción técnica - Regulación, norma, reglamento o legislación - Ambiental o de Salud":
                tipo = "61"
            elif tipo.strip() == "Producción técnica - Regulación, norma, reglamento o legislación - Educativa":
                tipo = "62"
            elif tipo.strip() == "Producción técnica - Regulación, norma, reglamento o legislación - Social":
                tipo = "63"
            elif tipo.strip() == "Producción técnica - Regulación, norma, reglamento o legislación - Técnica":
                tipo = "64"
            elif tipo.strip() == "Producción técnica - Regulación, norma, reglamento o legislación - Guía de práctica clínica":
                tipo = "65"
            elif tipo.strip() == "Producción técnica - Regulación, norma, reglamento o legislación - Proyecto de ley":
                tipo = "66"
            elif tipo.strip() == "Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Básica":
                tipo = "74"
            elif tipo.strip() == "Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Ensayo":
                tipo = "75"
            elif tipo.strip() == "Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Proceso":
                tipo = "77"
            else:
                print("ALERTA: "+tipo)
            #Nombre Producto
            index = info_ptnorma.find('Nombre comercial:')
            index = info_ptnorma.rfind(',',0,index)
            index1 = info_ptnorma.rfind(',',0,index) + 2
            index2 = info_ptnorma.find(',',index1 + 1,len(info_ptnorma))
            NombreProducto = info_ptnorma[index1:index2]
            #Coautores
            index2 = index1
            index1 = 1
            coautores = info_ptnorma[index1:index2]
            #Nombre Comercial
            index1 = info_ptnorma.find('Nombre comercial:') + 18
            index2 = info_ptnorma.find(',',index1,len(info_ptnorma))
            NombreComercial = info_ptnorma[index1:index2]
            #Paginas
            Paginas = ""
            #Duración
            Duracion = ""
            #Editorial
            Editorial = ""
            #Regulacion
            Regulacion = ""
            #Tipo Regulacion
            TipoRegulacion = ""
            #Contrato / Registro
            index1 = info_ptnorma.find('contrato/registro:') + 19
            index2 = info_ptnorma.find(',',index1,len(info_ptnorma))
            Registro = info_ptnorma[index1:index2]
            #Lugar
            index1 = info_ptnorma.find('En: ') + 4
            index2 = info_ptnorma.find(',\xa0\r\n                    ',index1,len(info_ptnorma))
            lugar = info_ptnorma[index1:index2]
            if lugar == ". ":
                lugar = ""
            #Año
            index = info_ptnorma.find("En:")
            index = info_ptnorma.find(",",index,len(info_ptnorma)) +1
            index1 = info_ptnorma.find(',',index,len(info_ptnorma)) +1
            index2 = info_ptnorma.find(',',index1,len(info_ptnorma))
            Anoptnorma = info_ptnorma[index1:index2]
            #Palabras
            index1 = info_ptnorma.find("Palabras:")
            index2 = info_ptnorma.find("Areas:")
            index3 = info_ptnorma.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_ptnorma[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_ptnorma[index1 + 9:index3]
            else:
                palabras = info_ptnorma[index1 + 9:len(info_ptnorma)]
            #Areas
            index1 = info_ptnorma.find("Areas:")
            index2 = info_ptnorma.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_ptnorma[index1 + 6:index2]
            else:
                areas = info_ptnorma[index1 + 6:len(info_ptnorma)]
            #Sectores
            index1 = info_ptnorma.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_ptnorma[index1 + 9:len(info_ptnorma)]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',lugar.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Anoptnorma.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + re.sub(' +',' ',palabras.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',areas.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',sectores.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',coautores.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + re.sub(' +',' ',Editorial.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + re.sub(' +',' ',Paginas.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
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
            + re.sub(' +',' ',Duracion.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Regulacion.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',TipoRegulacion.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        print("El Docente ",name," ",last," ","no tiene Normas o Regulaciones Asociadas")
    contptnorma = [COD_PRODUCTO]

def ptreglamentoextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
    global contptreglamento
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
        buscaptreglamento = containers[a].h3
        #print(buscaptreglamento)
        try:
            if buscaptreglamento.text == "Reglamentos":
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
            info_ptreglamento = cont.text
            #Tipo Otra Produccion
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Producción técnica - Reglamento Técnico":
                tipo = "67"
            # elif tipo.strip() == "Producción técnica - Regulación, norma, reglamento o legislación - Educativa":
            #     tipo = "62"
            else:
                print("ALERTA: "+tipo)
            #Nombre Producto
            index = info_ptreglamento.find('Nombre comercial:')
            index = info_ptreglamento.rfind(',',0,index)
            index1 = info_ptreglamento.rfind(',',0,index) + 2
            index2 = info_ptreglamento.find(',',index1 + 1,len(info_ptreglamento))
            NombreProducto = info_ptreglamento[index1:index2]
            #Coautores
            index2 = index1
            index1 = 1
            coautores = info_ptreglamento[index1:index2]
            #Nombre Comercial
            index1 = info_ptreglamento.find('Nombre comercial:') + 18
            index2 = info_ptreglamento.find(',',index1,len(info_ptreglamento))
            NombreComercial = info_ptreglamento[index1:index2]
            #Paginas
            Paginas = ""
            #Duración
            Duracion = ""
            #Editorial
            Editorial = ""
            #Regulacion
            Regulacion = ""
            #Tipo Regulacion
            TipoRegulacion = ""
            #Contrato / Registro
            index1 = info_ptreglamento.find('contrato/registro:') + 19
            index2 = info_ptreglamento.find(',',index1,len(info_ptreglamento))
            Registro = info_ptreglamento[index1:index2]
            #Lugar
            index1 = info_ptreglamento.find('En: ') + 4
            index2 = info_ptreglamento.find(',\xa0\r\n                    ',index1,len(info_ptreglamento))
            lugar = info_ptreglamento[index1:index2]
            if lugar == ". ":
                lugar = ""
            #Año
            index = info_ptreglamento.find("En:")
            index = info_ptreglamento.find(",",index,len(info_ptreglamento)) +1
            index1 = info_ptreglamento.find(',',index,len(info_ptreglamento)) +1
            index2 = info_ptreglamento.find(',',index1,len(info_ptreglamento))
            Anoptreglamento = info_ptreglamento[index1:index2]
            #Palabras
            index1 = info_ptreglamento.find("Palabras:")
            index2 = info_ptreglamento.find("Areas:")
            index3 = info_ptreglamento.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_ptreglamento[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_ptreglamento[index1 + 9:index3]
            else:
                palabras = info_ptreglamento[index1 + 9:len(info_ptreglamento)]
            #Areas
            index1 = info_ptreglamento.find("Areas:")
            index2 = info_ptreglamento.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_ptreglamento[index1 + 6:index2]
            else:
                areas = info_ptreglamento[index1 + 6:len(info_ptreglamento)]
            #Sectores
            index1 = info_ptreglamento.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_ptreglamento[index1 + 9:len(info_ptreglamento)]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',lugar.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Anoptreglamento.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + re.sub(' +',' ',palabras.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',areas.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',sectores.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',coautores.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + re.sub(' +',' ',Editorial.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + re.sub(' +',' ',Paginas.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
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
            + re.sub(' +',' ',Duracion.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Regulacion.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',TipoRegulacion.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        print("El Docente ",name," ",last," ","no tiene Reglamentos Asociados")
    contptreglamento = [COD_PRODUCTO]

def ptempresaextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
    global contptempresa
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
        buscaptempresa = containers[a].h3
        #print(buscaptempresa)
        try:
            if buscaptempresa.text == "Empresas de base tecnológica":
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
            info_ptempresa = cont.text
            #Tipo Otra Produccion
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Producción técnica - Empresa de base tecnológica - Spin-off":
                tipo = "68"
            elif tipo.strip() == "Producción técnica - Empresa de base tecnológica - Start-up":
                tipo = "69"
            else:
                print("ALERTA: "+tipo)
            #Nombre Producto
            index = info_ptempresa.find('Nit')
            index = info_ptempresa.rfind(',',0,index)
            index1 = info_ptempresa.rfind(',',0,index) + 2
            index2 = info_ptempresa.find(',',index1 + 1,len(info_ptempresa))
            NombreProducto = info_ptempresa[index1:index2]
            #Coautores
            index2 = index1
            index1 = 1
            coautores = info_ptempresa[index1:index2]
            #Nombre Comercial
            index1 = info_ptempresa.find('Nombre comercial:') + 18
            index2 = info_ptempresa.find(',',index1,len(info_ptempresa))
            NombreComercial = info_ptempresa[index1:index2]
            #Contrato / Registro
            index1 = info_ptempresa.find('Nit') + 3
            index2 = info_ptempresa.find(',',index1,len(info_ptempresa))
            Registro = info_ptempresa[index1:index2]
            #Año
            index1 = info_ptempresa.find("mara el:") + 9
            index2 = index1+4
            Anoptempresa = info_ptempresa[index1:index2]
            #Palabras
            index1 = info_ptempresa.find("Palabras:")
            index2 = info_ptempresa.find("Areas:")
            index3 = info_ptempresa.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_ptempresa[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_ptempresa[index1 + 9:index3]
            else:
                palabras = info_ptempresa[index1 + 9:len(info_ptempresa)]
            #Areas
            index1 = info_ptempresa.find("Areas:")
            index2 = info_ptempresa.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_ptempresa[index1 + 6:index2]
            else:
                areas = info_ptempresa[index1 + 6:len(info_ptempresa)]
            #Sectores
            index1 = info_ptempresa.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_ptempresa[index1 + 9:len(info_ptempresa)]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',Anoptempresa.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
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
            + "" + ";" \
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
        print("El Docente ",name," ",last," ","no tiene Empresas de Base Tecnológica Asociadas")
    contptempresa = [COD_PRODUCTO]

def demastrabajosextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
    global contdemastrabajos
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
        buscademastrabajos = containers[a].h3
        #print(buscademastrabajos)
        try:
            if buscademastrabajos.text == "Demás trabajos":
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
            info_demastrabajos = cont.text
            #Tipo Otra Produccion
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Demás trabajos - Demás trabajos":
                tipo = "70"
            # elif tipo.strip() == "Producción técnica - Empresa de base tecnológica - Start-up":
            #     tipo = "69"
            else:
                print("ALERTA: "+tipo)
            #Nombre Producto
            index = info_demastrabajos.find('En:')
            index = info_demastrabajos.rfind('.',0,index)
            index1 = info_demastrabajos.rfind(',',0,index) + 2
            index2 = info_demastrabajos.find('.',index1 + 1,len(info_demastrabajos))
            NombreProducto = info_demastrabajos[index1:index2]
            #Coautores
            index2 = index1
            index1 = 1
            coautores = info_demastrabajos[index1:index2]
            #Lugar
            index1 = info_demastrabajos.find('En: ') + 4
            index2 = info_demastrabajos.find(',\xa0\r\n                    ',index1,len(info_demastrabajos))
            lugar = info_demastrabajos[index1:index2]
            #Finalidad
            index1 = info_demastrabajos.find('finalidad: ') + 11
            if info_demastrabajos.find("Palabras:") != -1:
                index2 = info_demastrabajos.find("Palabras:")
            elif info_demastrabajos.find("Areas:") != -1:
                index2 = info_demastrabajos.find("Areas:")
            elif info_demastrabajos.find("Sectores:") != -1:
                index2 = info_demastrabajos.find("Sectores:")
            else:
                index2 = len(info_demastrabajos)
            Finalidad = info_demastrabajos[index1:index2]
            #Año
            index = info_demastrabajos.find("En:")
            index = info_demastrabajos.find(",",index,len(info_demastrabajos)) +1
            index1 = info_demastrabajos.find(',',index,len(info_demastrabajos)) +1
            index2 = info_demastrabajos.find(',',index1,len(info_demastrabajos))
            Anodemastrabajos = info_demastrabajos[index1:index2]
            #Palabras
            index1 = info_demastrabajos.find("Palabras:")
            index2 = info_demastrabajos.find("Areas:")
            index3 = info_demastrabajos.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_demastrabajos[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_demastrabajos[index1 + 9:index3]
            else:
                palabras = info_demastrabajos[index1 + 9:len(info_demastrabajos)]
            #Areas
            index1 = info_demastrabajos.find("Areas:")
            index2 = info_demastrabajos.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_demastrabajos[index1 + 6:index2]
            else:
                areas = info_demastrabajos[index1 + 6:len(info_demastrabajos)]
            #Sectores
            index1 = info_demastrabajos.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_demastrabajos[index1 + 9:len(info_demastrabajos)]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',lugar.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Anodemastrabajos.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
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
            + re.sub(' +',' ',Finalidad.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" \
            + "\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        print("El Docente ",name," ",last," ","no tiene Demás Trabajos Asociados")
    contdemastrabajos = [COD_PRODUCTO]
def ptsignosextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
    global contptsignos
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

    if all != 0:
        containerb = containers[all]
        container = containerb.findAll("blockquote")
        for x in range(0, len(container)):
            cont = container[x]
            info_ptsignos = cont.text
            #Tipo Otra Produccion
            tipo = "71"
            #Nombre Producto
            index1 = 0
            index2 = info_ptsignos.find(',')
            NombreProducto = info_ptsignos[index1:index2]
            #Contrato / Registro
            index1 = info_ptsignos.find('Registro:') + 8
            index2 = info_ptsignos.find(',',index1,len(info_ptsignos))
            Registro = info_ptsignos[index1:index2]
            #Titular
            index1 = info_ptsignos.find('Titular: ') + 9
            index2 = len(info_ptsignos)
            Titular = info_ptsignos[index1:index2]
            #Año
            index = info_ptsignos.find("Registro:")
            index1 = info_ptsignos.rfind(",",0,index) + 2
            index2 = info_ptsignos.find("Registro:")
            Anoptsignos = info_ptsignos[index1:index2]
            #Lugar
            index = info_ptsignos.find(",")
            index1 = info_ptsignos.find("En\xa0",index + 1,len(info_ptsignos)) + 3
            index2 = info_ptsignos.find(",",index1,len(info_ptsignos))
            Lugar = info_ptsignos[index1:index2]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',Lugar.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Anoptsignos.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
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
            + "" + ";" \
            + re.sub(' +',' ',Registro.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Titular.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
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
        print("El Docente ",name," ",last," ","no tiene Signos Asociados")
    contptsignos = [COD_PRODUCTO]
