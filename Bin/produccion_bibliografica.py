#
#
# #############################################################################
#       Copyright (c) 2018 Universidad Nacional de Colombia All Rights Reserved.
#
#             This work was made as a development to improve data collection
#       for self-assessment and accreditation processes in the Vicedeanship
#       of academic affairs in the Engineering Faculty of the Universidad
#       Nacional de Colombia and is licensed under a Creative Commons
#       Attribution-NonCommercial - ShareAlike 4.0 International License
#       and MIT Licence.
#
#       by Manuel Embus.
#
#       For more information write me to jai@mfneirae.com
#       Or visit my webpage at https://mfneirae.com/
# #############################################################################
#
#

def artiextract():
    from settings import my_url, name, doc, last, RH, COD_PRODUCTO
    import init, bs4, logging, sys, re
    global contarticulo
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
        buscaeventos = containers[a].h3
        #print(buscaeventos)
        try:
            if buscaeventos.text == "Artículos":
                all = a
                #print(all)
                break
        except AttributeError:
            pass

    if all != 0:
        containerb = containers[all]
        container = containerb.findAll("blockquote")
        tipoart = containerb.findAll("li")
        for x in range(0, len(container)):
            cont = container[x]
            tipoar = tipoart[x]
            tipo = tipoar.text
            info_articulo = cont.text
            #Nombre Articulo
            index1 = info_articulo.find('\r\n                    "') + 23
            index2 = info_articulo.find('"\r\n                    . En:')
            NombreProducto = info_articulo[index1:index2]
            #Tipo Artículo
            if tipo.strip() == "Producción bibliográfica - Artículo - Publicado en revista especializada":
                tipo = "8"
            elif tipo.strip() == "Producción bibliográfica - Artículo - Corto (Resumen)":
                tipo = "9"
            elif tipo.strip() == "Producción bibliográfica - Artículo - Revisión (Survey)":
                tipo = "10"
            elif tipo.strip() == "Producción bibliográfica - Artículo - Caso clínico":
                tipo = "11"
            else:
                logging.critical('Añadir: ' + tipo)
                print ("ALERTA: Revisar el archivo Artículos.log")
            #Coautores
            index1 = info_articulo.find("  \r\n                                        \r\n                    ") + 66
            index2 = info_articulo.find('"')
            coautores = info_articulo[index1:index2]
            #Lugar
            index1 = info_articulo.find('"\r\n                    . En: ') + 29
            index2 = info_articulo.find('\xa0\r\n                    ')
            lugar = info_articulo[index1:index2]
            #Editorial
            index1 = info_articulo.find("\xa0\r\n                    ed:\xa0") + 27
            index2 = info_articulo.find("v.",index1,len(info_articulo))
            editorial = info_articulo[index1:index2]
            #DOI
            index1 = info_articulo.find("\xa0DOI:\xa0") + 6
            index2 = info_articulo.find("\n",index1,len(info_articulo))
            doi = info_articulo[index1:index2]
            #ISSN
            index1 = info_articulo.find("ISSN:") + 6
            index2 = index1 + 9
            ISSN = info_articulo[index1:index2]
            #Nombre Revista
            index1 = info_articulo.find("\xa0\r\n                    ") + 23
            index2 = info_articulo.find("\xa0\r\n                    ISSN:")
            Revista = info_articulo[index1:index2]
            #Año
            index1 = info_articulo.find("\r\n                    ,") + 23
            index2 = info_articulo.find(",\r\n                    \xa0")
            AnoEvento = info_articulo[index1:index2]
            #Volumen
            index1 = info_articulo.find("\nv.") + 3
            index2 = info_articulo.find("fasc.")
            Volumen = info_articulo[index1:index2]
            #Fasciculo
            index1 = info_articulo.find("fasc.") + 5
            index2 = info_articulo.find("p.")
            fasciculo = info_articulo[index1:index2]
            #Páginas
            index1 = info_articulo.find("\r\n                    p.") + 24
            index2 = info_articulo.find("\r\n                    ",index1,len(info_articulo))
            Pagini = info_articulo[index1:index2]
            index1 = info_articulo.find("\r\n                    p.") + 24
            index1 = info_articulo.find("\r\n                    -",index1,len(info_articulo)) + 24
            index2 = info_articulo.find("\r\n                    ,",index1,len(info_articulo))
            Pagfin = info_articulo[index1:index2]
            init.rel_persona_producto_colciencias.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',tipo.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "0" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',AnoEvento.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',coautores.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',editorial.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Volumen.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',doi.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" \
            + "\n")
            init.inrel_personas_producto_colciencias.append( \
            "REPLACE INTO `uapa_db`.`rel_personas_producto_colciencias`(`cod_rel_per_prod_col`,`cod_producto`,`cod_rh`,`cod_tipo_producto`,`nombre_producto`,`evento_asociado`,`datos_complementarios`,`lugar`,`ano`,`ambito`,`palabras_clave`,`areas`,`sectores`,`coautores`,`vincula_coautores`,`editorial`,`volumen`,`paginas`,`doi`,`finalidad`,`instituciones_asociadas`,`tipo_vinculacion_institucion`) VALUES"
            + "('"+ str(RH) + str(COD_PRODUCTO) + "'," \
            + str(COD_PRODUCTO) + ","\
            + "'" + str(RH) + "',"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',tipo.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',AnoEvento.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',coautores.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',editorial.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Volumen.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',doi.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ");\n")
            init.colciencias_prod_bibliografica.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Revista.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',ISSN.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',fasciculo.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Pagini.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Pagfin.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "\n")
            init.incolciencias_prod_bibliografica.append( \
            "REPLACE INTO `uapa_db`.`colciencias_prod_bibliografica`(`cod_colciencias_prod_bibliografica`,`cod_rh`,`cod_rel_per_prod_col`,`revista`,`issn/isbn`,`libro/revista_original_trad`,`nombre_libro/revista_trad`,`nombre_autor_original_trad`,`idioma_original`,`idioma_traduccion`,`nombre_capitulo`,`fasciculo`,`pagina_inicial`,`pagina_final`) VALUES"
            + "('" + str(COD_PRODUCTO) + "',"\
            + "'" + str(RH) + "',"\
            + "'" + str(RH) + str(COD_PRODUCTO) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Revista.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',ISSN.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',fasciculo.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Pagini.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Pagfin.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "'"\
            + ");\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        logging.info(' El Docente ' + name + ' ' + last + ' no tiene Artículos Asociados')

    contarticulo = [COD_PRODUCTO]

def libextract():
    from settings import my_url, name, doc, last, RH, COD_PRODUCTO
    import init, bs4, logging, sys, re
    global contlibro
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
    LOG_FILENAME = './Logs/Libros.log'
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}
    if len(sys.argv) > 1:
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)
        logging.basicConfig(level=level)
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
        buscalibros = containers[a].h3
        #print(buscalibros)
        try:
            if buscalibros.text == "Libros":
                all = a
                #print(all)
                break
        except AttributeError:
            pass

    if all != 0:
        containerb = containers[all]
        container = containerb.findAll("blockquote")
        tipolib = containerb.findAll("li")
        for x in range(0, len(container)):
            tipoli = tipolib[x]
            tipo = tipoli.text
            if tipo.strip() == "Producción bibliográfica - Libro - Libro resultado de investigación":
                tipo = "17"
            elif tipo.strip() == "Producción bibliográfica - Libro - Otro libro publicado":
                tipo = "18"
            elif tipo.strip() == "Producción bibliográfica - Libro - Libro pedagógico y/o de divulgación":
                tipo = "19"
            else:
                logging.critical('Añadir: ' + tipo)
                print ("ALERTA: Revisar el archivo Libros.log")
            cont = container[x]
            info_libro = cont.text
            #Coautores
            index1 = info_libro.find("  \r\n                                        \r\n                    ") + 66
            index2 = info_libro.find('"')
            coautores = info_libro[index1:index2]
            #Nombre Producto
            index1 = info_libro.find(',                    \r\n                    \r\n                    "') + 66
            index2 = info_libro.find('"\r\n                    En:')
            NombreProducto = info_libro[index1:index2]
            #ISBN
            index1 = info_libro.find("ISBN:") + 6
            index2 = info_libro.find("\xa0\r\n                    v.")
            ISBN = info_libro[index1:index2]
            #Año
            index = info_libro.find('"\r\n                    En:') + 25
            index1 = info_libro.find('\r\n                    ', index , len(info_libro)) + 22
            index2 = info_libro.find(".\xa0\r\n                    ed:")
            Anolibro = info_libro[index1:index2]
            #Editorial
            index1 = info_libro.find("\xa0\r\n                    ed:") + 26
            index2 = info_libro.find("\xa0\r\n                    ISBN:")
            Editorial = info_libro[index1:index2]
            #Volumen
            index1 = info_libro.find("v.") + 3
            index2 = info_libro.find("pags.")
            Volumen = info_libro[index1:index2]
            #Lugar
            index1 = info_libro.find('"\r\n                    En:') + 27
            index2 = info_libro.find('\r\n                    ',index1,len(info_libro))
            lugar = info_libro[index1:index2]
            #Páginas
            index1 = info_libro.find("pags.") + 6
            index2 = info_libro.find("\r\n",index1,len(info_libro))
            paginas = info_libro[index1:index2]
            #Palabras
            index1 = info_libro.find("Palabras:")
            index2 = info_libro.find("Areas:")
            index3 = info_libro.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_libro[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_libro[index1 + 9:index3]
            else:
                palabras = info_libro[index1 + 9:len(info_libro)]
            #Areas
            index1 = info_libro.find("Areas:")
            index2 = info_libro.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_libro[index1 + 6:index2]
            else:
                areas = info_libro[index1 + 6:len(info_libro)]
            #Sectores
            index1 = info_libro.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_libro[index1 + 9:len(info_libro)]
            init.rel_persona_producto_colciencias.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',tipo.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "0" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Anolibro.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',palabras.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',areas.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',sectores.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',coautores.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Editorial.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Volumen.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',paginas.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" \
            + "\n")
            init.inrel_personas_producto_colciencias.append( \
            "REPLACE INTO `uapa_db`.`rel_personas_producto_colciencias`(`cod_rel_per_prod_col`,`cod_producto`,`cod_rh`,`cod_tipo_producto`,`nombre_producto`,`evento_asociado`,`datos_complementarios`,`lugar`,`ano`,`ambito`,`palabras_clave`,`areas`,`sectores`,`coautores`,`vincula_coautores`,`editorial`,`volumen`,`paginas`,`doi`,`finalidad`,`instituciones_asociadas`,`tipo_vinculacion_institucion`) VALUES"            + "('"+ str(RH) + str(COD_PRODUCTO) + "'," \
            + str(COD_PRODUCTO) + ","\
            + "'" + str(RH) + "',"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',tipo.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Anolibro.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',palabras.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',areas.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',sectores.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',coautores.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Editorial.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Volumen.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',paginas.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ");\n")
            init.colciencias_prod_bibliografica.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',ISBN.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
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
            init.incolciencias_prod_bibliografica.append( \
            "REPLACE INTO `uapa_db`.`colciencias_prod_bibliografica`(`cod_colciencias_prod_bibliografica`,`cod_rh`,`cod_rel_per_prod_col`,`revista`,`issn/isbn`,`libro/revista_original_trad`,`nombre_libro/revista_trad`,`nombre_autor_original_trad`,`idioma_original`,`idioma_traduccion`,`nombre_capitulo`,`fasciculo`,`pagina_inicial`,`pagina_final`) VALUES"
            + "('" + str(COD_PRODUCTO) + "',"\
            + "'" + str(RH) + "',"\
            + "'" + str(RH) + str(COD_PRODUCTO) + "',"\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',ISBN.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" \
            + ");\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        logging.info(' El Docente ' + name + ' ' + last + ' no tiene Libros Asociados')
    contlibro = [COD_PRODUCTO]

def caplibroextract():
    from settings import my_url, name, doc, last, RH, COD_PRODUCTO
    import init, bs4, logging, sys, re
    global contcaplibro
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
    LOG_FILENAME = './Logs/Capítulos Libros.log'
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}
    if len(sys.argv) > 1:
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)
        logging.basicConfig(level=level)
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
        buscacaplibros = containers[a].h3
        #print(buscacaplibros)
        try:
            if buscacaplibros.text == "Capitulos de libro":
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
            info_caplibro = cont.text
            #Tipo Capítulos
            index1 = info_caplibro.find('Tipo:') + 6
            index2 = info_caplibro.find('\r\n                            ',index1,len(info_caplibro))
            Tipo = info_caplibro[index1:index2]
            #Coautores
            remthis = "Tipo: "+ Tipo
            index1 = info_caplibro.find('Tipo:')
            index2 = info_caplibro.find('\n                            "')
            coautores = info_caplibro[index1:index2]
            coautores = coautores.replace(remthis,"")
            if Tipo == "Capítulo de libro":
                Tipo = "21"
            elif Tipo == "Otro capítulo de libro publicado":
                Tipo = "20"
            else:
                logging.critical('Añadir: ' + tipo)
                print ("ALERTA: Revisar el archivo Capítulos Libros.log")
            #Nombre Producto
            index1 = info_caplibro.find(',                    \r\n                            \r\n\r\n                            "') + 84
            index2 = info_caplibro.find('"\r\n                            ')
            NombreProducto = info_caplibro[index1:index2]
            #Nombre Libro
            index = info_caplibro.find(',                    \r\n                            \r\n\r\n                            "') + 84
            index1 = info_caplibro.find('\r\n                    ', index , len(info_caplibro)) + 30
            index2 = info_caplibro.find('\r\n                            . En:')
            Libro = info_caplibro[index1:index2]
            #Lugar
            index1 = info_caplibro.find('En: ') + 4
            index2 = info_caplibro.find('\xa0\r\n                    ',index1,len(info_caplibro))
            lugar = info_caplibro[index1:index2]
            #Editorial
            index1 = info_caplibro.find("ed:\xa0") + 4
            index2 = info_caplibro.find(", v.",index1,len(info_caplibro))
            Editorial = info_caplibro[index1:index2]
            #Año
            index1 = info_caplibro.find('\xa0\r\n                            \r\n                            ,') + 62
            index2 = index1 + 4
            Anocaplibro = info_caplibro[index1:index2]
            if Anocaplibro == '\n   ':
                index1 = info_caplibro.find('\xa0\r\n                            1\r\n                            ,') + 63
                index2 = index1 + 4
                Anocaplibro = info_caplibro[index1:index2]
            #Páginas
            index1 = info_caplibro.find(", p.") + 4
            index2 = info_caplibro.find("\r\n                            -",index1,len(info_caplibro))
            Pagini = info_caplibro[index1:index2]
            index1 = info_caplibro.find("-",index1,len(info_caplibro)) + 2
            index2 = info_caplibro.find("\xa0",index1,len(info_caplibro))
            Pagfin = info_caplibro[index1:index2]
            paginas = Pagini + " - " + Pagfin
            #Palabras
            index1 = info_caplibro.find("Palabras:")
            index2 = info_caplibro.find("Areas:")
            index3 = info_caplibro.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_caplibro[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_caplibro[index1 + 9:index3]
            else:
                palabras = info_caplibro[index1 + 9:len(info_caplibro)]
            #Areas
            index1 = info_caplibro.find("Areas:")
            index2 = info_caplibro.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_caplibro[index1 + 6:index2]
            else:
                areas = info_caplibro[index1 + 6:len(info_caplibro)]
            #Sectores
            index1 = info_caplibro.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_caplibro[index1 + 9:len(info_caplibro)]
            #Volumen
            index1 = info_caplibro.find(", v.") + 4
            index2 = info_caplibro.find(", p.")
            Volumen = info_caplibro[index1:index2]
            init.rel_persona_producto_colciencias.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + Tipo + ";"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Libro.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "0" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Anocaplibro.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',palabras.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',areas.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',sectores.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',coautores.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Editorial.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Volumen.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',paginas.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" \
            + "\n")
            init.inrel_personas_producto_colciencias.append( \
            "REPLACE INTO `uapa_db`.`rel_personas_producto_colciencias`(`cod_rel_per_prod_col`,`cod_producto`,`cod_rh`,`cod_tipo_producto`,`nombre_producto`,`evento_asociado`,`datos_complementarios`,`lugar`,`ano`,`ambito`,`palabras_clave`,`areas`,`sectores`,`coautores`,`vincula_coautores`,`editorial`,`volumen`,`paginas`,`doi`,`finalidad`,`instituciones_asociadas`,`tipo_vinculacion_institucion`) VALUES"            + "('"+ str(RH) + str(COD_PRODUCTO) + "'," \
            + str(COD_PRODUCTO) + ","\
            + "'" + str(RH) + "',"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Tipo.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Libro.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Anocaplibro.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',palabras.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',areas.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',sectores.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',coautores.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Editorial.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Volumen.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',paginas.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ");\n")
            init.colciencias_prod_bibliografica.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Pagini.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Pagfin.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "\n")
            init.incolciencias_prod_bibliografica.append( \
            "REPLACE INTO `uapa_db`.`colciencias_prod_bibliografica`(`cod_colciencias_prod_bibliografica`,`cod_rh`,`cod_rel_per_prod_col`,`revista`,`issn/isbn`,`libro/revista_original_trad`,`nombre_libro/revista_trad`,`nombre_autor_original_trad`,`idioma_original`,`idioma_traduccion`,`nombre_capitulo`,`fasciculo`,`pagina_inicial`,`pagina_final`) VALUES"
            + "('" + str(COD_PRODUCTO) + "',"\
            + "'" + str(RH) + "',"\
            + "'" + str(RH) + str(COD_PRODUCTO) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Pagini.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Pagfin.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "'"\
            + ");\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        logging.info(' El Docente ' + name + ' ' + last + ' no tiene Capítulos de Libro Asociados')

    contcaplibro = [COD_PRODUCTO]

def texnocienextract():
    from settings import my_url, name, doc, last, RH, COD_PRODUCTO
    import init, bs4, logging, sys, re
    global conttexnocien
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
    LOG_FILENAME = './Logs/Textos No Cientificos.log'
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}
    if len(sys.argv) > 1:
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)
        logging.basicConfig(level=level)
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
        buscatexnocien = containers[a].h3
        #print(buscatexnocien)
        try:
            if buscatexnocien.text == "Textos en publicaciones no científicas":
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
            info_texnocien = cont.text
            #Tipo Capítulos
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Producción bibliográfica - Otro artículo publicado - Periódico de noticias":
                tipo = "22"
            elif tipo.strip() == "Producción bibliográfica - Otro artículo publicado - Revista de divulgación":
                tipo = "23"
            elif tipo.strip() == "Producción bibliográfica - Otro artículo publicado - Carta al editor":
                tipo = "24"
            elif tipo.strip() == "Producción bibliográfica - Otro artículo publicado - Reseñas de libros":
                tipo = "25"
            elif tipo.strip() == "Producción bibliográfica - Otro artículo publicado - Columna de opinión":
                tipo = "26"
            elif tipo.strip() == "Producción bibliográfica - Otro artículo publicado - Columna de opinión":
                tipo = "126"
            else:
                logging.critical('Añadir: ' + tipo)
                print ("ALERTA: Revisar el archivo Textos No Cientificos.log")


            #Coautores
            index1 = 1
            index2 = info_texnocien.find('"')
            coautores = info_texnocien[index1:index2]
            #Nombre Producto
            index1 = info_texnocien.find('"') + 1
            index2 = info_texnocien.find('"',index1,len(info_texnocien))
            NombreProducto = info_texnocien[index1:index2]
            #Nombre Revista
            index = info_texnocien.find("En:")
            index1 = info_texnocien.find(".\r\n                    ") + 23
            index2 = info_texnocien.find("ISSN:")
            Revista = info_texnocien[index1:index2]
            #Lugar
            index1 = info_texnocien.find('En: ') + 4
            index2 = info_texnocien.find('\r\n                    ',index1,len(info_texnocien))
            lugar = info_texnocien[index1:index2]
            #Año
            index = info_texnocien.find("En:")
            index1 = info_texnocien.find('\r\n                    ',index,len(info_texnocien)) + 22
            index2 = info_texnocien.find('.\r\n ',index1,len(info_texnocien))
            Anotexnocien = info_texnocien[index1:index2]
            #ISSN
            index1 = info_texnocien.find("ISSN:") + 6
            index2 = info_texnocien.find("\r\n                    p.")
            ISSN = info_texnocien[index1:index2]
            #Paginas
            index1 = info_texnocien.find("\r\n                    p.") + 24
            index2 = info_texnocien.find(" \r\n                    - ",index1,len(info_texnocien))
            Pagini = info_texnocien[index1:index2]
            index1 = info_texnocien.find("- ",index1,len(info_texnocien)) + 2
            index2 = info_texnocien.find("\r\n",index1,len(info_texnocien))
            Pagfin = info_texnocien[index1:index2]
            paginas = Pagini + " - " + Pagfin
            #Palabras
            index1 = info_texnocien.find("Palabras:")
            index2 = info_texnocien.find("Areas:")
            index3 = info_texnocien.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_texnocien[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_texnocien[index1 + 9:index3]
            else:
                palabras = info_texnocien[index1 + 9:len(info_texnocien)]
            #Areas
            index1 = info_texnocien.find("Areas:")
            index2 = info_texnocien.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_texnocien[index1 + 6:index2]
            else:
                areas = info_texnocien[index1 + 6:len(info_texnocien)]
            #Sectores
            index1 = info_texnocien.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_texnocien[index1 + 9:len(info_texnocien)]
            #Volumen
            index1 = info_texnocien.find("\r\n                    v.") + 24
            index2 = info_texnocien.find("\r\n",index1,len(info_texnocien))
            Volumen = info_texnocien[index1:index2]
            init.rel_persona_producto_colciencias.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Anotexnocien.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',palabras.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',areas.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',sectores.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',coautores.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Volumen.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',paginas.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" \
            + "\n")
            init.inrel_personas_producto_colciencias.append( \
            "REPLACE INTO `uapa_db`.`rel_personas_producto_colciencias`(`cod_rel_per_prod_col`,`cod_producto`,`cod_rh`,`cod_tipo_producto`,`nombre_producto`,`evento_asociado`,`datos_complementarios`,`lugar`,`ano`,`ambito`,`palabras_clave`,`areas`,`sectores`,`coautores`,`vincula_coautores`,`editorial`,`volumen`,`paginas`,`doi`,`finalidad`,`instituciones_asociadas`,`tipo_vinculacion_institucion`) VALUES"            + "('"+ str(RH) + str(COD_PRODUCTO) + "'," \
            + str(COD_PRODUCTO) + ","\
            + "'" + str(RH) + "',"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',tipo.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Anotexnocien.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',palabras.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',areas.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',sectores.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',coautores.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Volumen.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',paginas.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ");\n")
            init.colciencias_prod_bibliografica.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Revista.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',ISSN.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Pagini.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Pagfin.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "\n")
            init.incolciencias_prod_bibliografica.append( \
            "REPLACE INTO `uapa_db`.`colciencias_prod_bibliografica`(`cod_colciencias_prod_bibliografica`,`cod_rh`,`cod_rel_per_prod_col`,`revista`,`issn/isbn`,`libro/revista_original_trad`,`nombre_libro/revista_trad`,`nombre_autor_original_trad`,`idioma_original`,`idioma_traduccion`,`nombre_capitulo`,`fasciculo`,`pagina_inicial`,`pagina_final`) VALUES"
            + "('" + str(COD_PRODUCTO) + "',"\
            + "'" + str(RH) + "',"\
            + "'" + str(RH) + str(COD_PRODUCTO) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Revista.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',ISSN.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Pagini.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Pagfin.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "'"\
            + ");\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        logging.info(' El Docente ' + name + ' ' + last + ' no tiene Textos no Cientificos Asociados')
    conttexnocien = [COD_PRODUCTO]

def workpextract():
    from settings import my_url, name, doc, last, RH, COD_PRODUCTO
    import init, bs4, logging, sys, re
    global contworkp
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
    LOG_FILENAME = './Logs/Documentos.log'
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}
    if len(sys.argv) > 1:
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)
        logging.basicConfig(level=level)
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
                logging.critical('Añadir: ' + tipo)
                print ("ALERTA: Revisar el archivo Documentos.log")
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
            init.rel_persona_producto_colciencias.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Anoworkp.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',palabras.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',areas.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',sectores.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',coautores.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',paginas.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" \
            + "\n")
            init.inrel_personas_producto_colciencias.append( \
            "REPLACE INTO `uapa_db`.`rel_personas_producto_colciencias`(`cod_rel_per_prod_col`,`cod_producto`,`cod_rh`,`cod_tipo_producto`,`nombre_producto`,`evento_asociado`,`datos_complementarios`,`lugar`,`ano`,`ambito`,`palabras_clave`,`areas`,`sectores`,`coautores`,`vincula_coautores`,`editorial`,`volumen`,`paginas`,`doi`,`finalidad`,`instituciones_asociadas`,`tipo_vinculacion_institucion`) VALUES"            + "('"+ str(RH) + str(COD_PRODUCTO) + "'," \
            + str(COD_PRODUCTO) + ","\
            + "'" + str(RH) + "',"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',tipo.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Anoworkp.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',palabras.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',areas.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',sectores.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',coautores.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',paginas.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ");\n")
            init.colciencias_prod_bibliografica.append(RH + ";"\
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
            init.incolciencias_prod_bibliografica.append( \
            "REPLACE INTO `uapa_db`.`colciencias_prod_bibliografica`(`cod_colciencias_prod_bibliografica`,`cod_rh`,`cod_rel_per_prod_col`,`revista`,`issn/isbn`,`libro/revista_original_trad`,`nombre_libro/revista_trad`,`nombre_autor_original_trad`,`idioma_original`,`idioma_traduccion`,`nombre_capitulo`,`fasciculo`,`pagina_inicial`,`pagina_final`) VALUES"
            + "('" + str(COD_PRODUCTO) + "',"\
            + "'" + str(RH) + "',"\
            + "'" + str(RH) + str(COD_PRODUCTO) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null"\
            + ");\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        logging.info(' El Docente ' + name + ' ' + last + ' no tiene Documentos de Trabajo Asociados')
    contworkp = [COD_PRODUCTO]

def traduccionextract():
    from settings import my_url, name, doc, last, RH, COD_PRODUCTO
    import init, bs4, logging, sys, re
    global conttraduccion
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
        buscatraduccion = containers[a].h3
        #print(buscatraduccion)
        try:
            if buscatraduccion.text == "Traducciones":
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
            info_traduccion = cont.text
            #Tipo Capítulos
            tipotex = tipotexno[x]
            tipo = tipotex.text
            if tipo.strip() == "Producción bibliográfica - Traducciones - Artículo":
                tipo = "28"
            elif tipo.strip() == "Producción bibliográfica - Traducciones - Libro":
                tipo = "29"
            elif tipo.strip() == "Producción bibliográfica - Traducciones - Otra":
                tipo = "30"
            else:
                logging.critical('Añadir: ' + tipo)
                print ("ALERTA: Revisar el archivo Eventos.log")
            #Coautores
            index1 = 1
            index2 = info_traduccion.find('"')
            coautores = info_traduccion[index1:index2]
            #Nombre Producto
            index1 = info_traduccion.find('"') + 1
            index2 = info_traduccion.find('"',index1,len(info_traduccion))
            NombreProducto = info_traduccion[index1:index2]
            #Lugar
            index1 = info_traduccion.find('En: ') + 4
            index2 = info_traduccion.find('\r\n                    ',index1,len(info_traduccion))
            lugar = info_traduccion[index1:index2]
            if lugar == ". ":
                lugar = ""
            #Año
            index = info_traduccion.find("En:")
            index1 = info_traduccion.find('\r\n                    ',index,len(info_traduccion)) + 22
            index2 = info_traduccion.find('.               \r\n',index1,len(info_traduccion))
            Anotraduccion = info_traduccion[index1:index2]
            #Nombre Original
            index1 = info_traduccion.find("Nombre original:") + 17
            index2 = info_traduccion.find("fasc.")
            NombreOriginal = info_traduccion[index1:index2]
            #Autor Original
            index1 = info_traduccion.find("Autor:") + 7
            index2 = info_traduccion.find("Nombre original:")
            AutorOriginal = info_traduccion[index1:index2]
            #Idioma Original
            index1 = info_traduccion.find("Idioma original:") + 16
            index2 = info_traduccion.find("\r\n",index1,len(info_traduccion))
            IdiomaOriginal = info_traduccion[index1:index2]
            #Idioma Traducción
            index1 = info_traduccion.find("Idioma traducción:") + 18
            index2 = info_traduccion.find("\r\n",index1,len(info_traduccion))
            IdiomaTraduccion = info_traduccion[index1:index2]
            #Volumen
            index1 = info_traduccion.find('v.') + 3
            index2 = info_traduccion.find('\r\n',index1,len(info_traduccion))
            volumen = info_traduccion[index1:index2]
            if volumen == ". ":
                volumen = ""
            #Fasciculo
            index1 = info_traduccion.find('fasc.') + 5
            index2 = info_traduccion.find('\r\n',index1,len(info_traduccion))
            fasciculo = info_traduccion[index1:index2]
            if fasciculo == " .":
                fasciculo = ""
            #Palabras
            index1 = info_traduccion.find("Palabras:")
            index2 = info_traduccion.find("Areas:")
            index3 = info_traduccion.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_traduccion[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_traduccion[index1 + 9:index3]
            else:
                palabras = info_traduccion[index1 + 9:len(info_traduccion)]
            #Areas
            index1 = info_traduccion.find("Areas:")
            index2 = info_traduccion.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_traduccion[index1 + 6:index2]
            else:
                areas = info_traduccion[index1 + 6:len(info_traduccion)]
            #Sectores
            index1 = info_traduccion.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_traduccion[index1 + 9:len(info_traduccion)]
            init.rel_persona_producto_colciencias.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Anotraduccion.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',palabras.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',areas.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',sectores.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',coautores.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',volumen.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" \
            + "\n")
            init.inrel_personas_producto_colciencias.append( \
            "REPLACE INTO `uapa_db`.`rel_personas_producto_colciencias`(`cod_rel_per_prod_col`,`cod_producto`,`cod_rh`,`cod_tipo_producto`,`nombre_producto`,`evento_asociado`,`datos_complementarios`,`lugar`,`ano`,`ambito`,`palabras_clave`,`areas`,`sectores`,`coautores`,`vincula_coautores`,`editorial`,`volumen`,`paginas`,`doi`,`finalidad`,`instituciones_asociadas`,`tipo_vinculacion_institucion`) VALUES"            + "('"+ str(RH) + str(COD_PRODUCTO) + "'," \
            + str(COD_PRODUCTO) + ","\
            + "'" + str(RH) + "',"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',tipo.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Anotraduccion.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',palabras.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',areas.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',sectores.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',coautores.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',volumen.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ");\n")
            init.colciencias_prod_bibliografica.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreOriginal.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',AutorOriginal.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',IdiomaOriginal.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',IdiomaTraduccion.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',fasciculo.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "\n")
            init.incolciencias_prod_bibliografica.append( \
            "REPLACE INTO `uapa_db`.`colciencias_prod_bibliografica`(`cod_colciencias_prod_bibliografica`,`cod_rh`,`cod_rel_per_prod_col`,`revista`,`issn/isbn`,`libro/revista_original_trad`,`nombre_libro/revista_trad`,`nombre_autor_original_trad`,`idioma_original`,`idioma_traduccion`,`nombre_capitulo`,`fasciculo`,`pagina_inicial`,`pagina_final`) VALUES"
            + "('" + str(COD_PRODUCTO) + "',"\
            + "'" + str(RH) + "',"\
            + "'" + str(RH) + str(COD_PRODUCTO) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreOriginal.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',AutorOriginal.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',IdiomaOriginal.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',IdiomaTraduccion.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',fasciculo.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" \
            + ");\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        logging.info(' El Docente ' + name + ' ' + last + ' no tiene Traducciones Asociadas')
    conttraduccion = [COD_PRODUCTO]

def otrapbextract():
    from settings import my_url, name, doc, last, RH, COD_PRODUCTO
    import init, bs4, logging, sys, re
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
                logging.critical('Añadir: ' + tipo)
                print ("ALERTA: Revisar el archivo Eventos.log")
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
            init.rel_persona_producto_colciencias.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Anootrapb.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',palabras.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',areas.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',sectores.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',coautores.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',paginas.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" \
            + "\n")
            init.inrel_personas_producto_colciencias.append( \
            "REPLACE INTO `uapa_db`.`rel_personas_producto_colciencias`(`cod_rel_per_prod_col`,`cod_producto`,`cod_rh`,`cod_tipo_producto`,`nombre_producto`,`evento_asociado`,`datos_complementarios`,`lugar`,`ano`,`ambito`,`palabras_clave`,`areas`,`sectores`,`coautores`,`vincula_coautores`,`editorial`,`volumen`,`paginas`,`doi`,`finalidad`,`instituciones_asociadas`,`tipo_vinculacion_institucion`) VALUES"            + "('"+ str(RH) + str(COD_PRODUCTO) + "'," \
            + str(COD_PRODUCTO) + ","\
            + "'" + str(RH) + "',"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',tipo.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Anootrapb.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ","\
            + "null" + ","\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',palabras.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',areas.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',sectores.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',coautores.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            +"'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',paginas.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ");\n")
            init.colciencias_prod_bibliografica.append(RH + ";"\
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
            init.incolciencias_prod_bibliografica.append( \
            "REPLACE INTO `uapa_db`.`colciencias_prod_bibliografica`(`cod_colciencias_prod_bibliografica`,`cod_rh`,`cod_rel_per_prod_col`,`revista`,`issn/isbn`,`libro/revista_original_trad`,`nombre_libro/revista_trad`,`nombre_autor_original_trad`,`idioma_original`,`idioma_traduccion`,`nombre_capitulo`,`fasciculo`,`pagina_inicial`,`pagina_final`) VALUES"
            + "('" + str(COD_PRODUCTO) + "',"\
            + "'" + str(RH) + "',"\
            + "'" + str(RH) + str(COD_PRODUCTO) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" \
            + ");\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        logging.info(' El Docente ' + name + ' ' + last + ' no tiene Otras Producciones Asociadas')
    contotrapb = [COD_PRODUCTO]
