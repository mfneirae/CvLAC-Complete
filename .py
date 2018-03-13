def otrapbextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
    global contotrapb
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
        buscaotrapb = containers[a].h3
        #print(buscaotrapb)
        try:
            if buscaotrapb.text == "Otra producción blibliográfica":
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
            info_otrapb = cont.text
            #Tipo Otra Produccion
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Producción bibliográfica - Otra producción bibliográfica - Introducción":
                tipo = "31"
            elif tipo.strip() == "Producción bibliográfica - Otra producción bibliográfica - Prólogo":
                tipo = "32"
            elif tipo.strip() == "Producción bibliográfica - Otra producción bibliográfica - Epílogo":
                tipo = "33"
            elif tipo.strip() == "Producción bibliográfica - Otra producción bibliográfica - Otra":
                tipo = "34"
            else:
                print(tipo)
            #Coautores
            index1 = 1
            index2 = info_otrapb.find('"')
            coautores = info_otrapb[index1:index2]
            #Nombre Producto
            index1 = info_otrapb.find('"') + 1
            index2 = info_otrapb.find('"',index1,len(info_otrapb))
            NombreProducto = info_otrapb[index1:index2]
            #Lugar
            index1 = info_otrapb.find('En: ') + 4
            index2 = info_otrapb.find('\r\n                    ',index1,len(info_otrapb))
            lugar = info_otrapb[index1:index2]
            if lugar == ". ":
                lugar = ""
            #Año
            index = info_otrapb.find("En:")
            index1 = info_otrapb.find('\r\n                    ',index,len(info_otrapb)) + 22
            index2 = info_otrapb.find('.\r\n',index1,len(info_otrapb))
            Anootrapb = info_otrapb[index1:index2]
            #Volumen
            index1 = info_otrapb.find('p.') + 3
            index2 = info_otrapb.find('\n',index1,len(info_otrapb))
            paginas = info_otrapb[index1:index2]
            if paginas == ". ":
                paginas = ""
            #Palabras
            index1 = info_otrapb.find("Palabras:")
            index2 = info_otrapb.find("Areas:")
            index3 = info_otrapb.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_otrapb[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_otrapb[index1 + 9:index3]
            else:
                palabras = info_otrapb[index1 + 9:len(info_otrapb)]
            #Areas
            index1 = info_otrapb.find("Areas:")
            index2 = info_otrapb.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_otrapb[index1 + 6:index2]
            else:
                areas = info_otrapb[index1 + 6:len(info_otrapb)]
            #Sectores
            index1 = info_otrapb.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_otrapb[index1 + 9:len(info_otrapb)]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',lugar.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Anootrapb.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + re.sub(' +',' ',palabras.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',areas.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',sectores.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',coautores.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',paginas.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" \
            + "\n")
            init.PROD_BIBLIOGRAFICA.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
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
            + "\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        print("El Docente ",name," ",last," ","no tiene Otras Producciones Asociadas")
    contotrapb = [COD_PRODUCTO]
