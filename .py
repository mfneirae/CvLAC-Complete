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
