def workpextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
    global contworkp
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
        buscaworkp = containers[a].h3
        #print(buscaworkp)
        try:
            if buscaworkp.text == "Documentos de trabajo":
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
            info_workp = cont.text
            #Tipo Capítulos
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Producción bibliográfica - Documento de trabajo (Working Paper)":
                tipo = "27"
            else:
                print(tipo)
            #Coautores
            index1 = 1
            index2 = info_workp.find('"')
            coautores = info_workp[index1:index2]
            #Nombre Producto
            index1 = info_workp.find('"') + 1
            index2 = info_workp.find('"',index1,len(info_workp))
            NombreProducto = info_workp[index1:index2]
            #Lugar
            index1 = info_workp.find('En: ') + 4
            index2 = info_workp.find('\r\n                    ',index1,len(info_workp))
            lugar = info_workp[index1:index2]
            if lugar == ". ":
                lugar = ""
            #Año
            index = info_workp.find("En:")
            index1 = info_workp.find('\r\n                    ',index,len(info_workp)) + 22
            index2 = info_workp.find('.\r\n ',index1,len(info_workp))
            Anoworkp = info_workp[index1:index2]
            #Paginas
            index1 = info_workp.find("\r\n                    p.") + 24
            index2 = info_workp.find("Palabras:",index1,len(info_workp))
            paginas = info_workp[index1:index2]
            #Palabras
            index1 = info_workp.find("Palabras:")
            index2 = info_workp.find("Areas:")
            index3 = info_workp.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_workp[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_workp[index1 + 9:index3]
            else:
                palabras = info_workp[index1 + 9:len(info_workp)]
            #Areas
            index1 = info_workp.find("Areas:")
            index2 = info_workp.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_workp[index1 + 6:index2]
            else:
                areas = info_workp[index1 + 6:len(info_workp)]
            #Sectores
            index1 = info_workp.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_workp[index1 + 9:len(info_workp)]
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',lugar.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Anoworkp.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + re.sub(' +',' ',palabras.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',areas.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',sectores.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',coautores.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',paginas.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" \
            + "\n")
            init.PROD_BIBLIOGRAFICA.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + re.sub(' +',' ',Revista.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',ISSN.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
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
        print("El Docente ",name," ",last," ","no tiene Textos no Cientificos Asociados")
    contworkp = [COD_PRODUCTO]
