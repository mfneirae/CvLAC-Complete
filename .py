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
                print(tipo)
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
