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

def reconocimientosextract():
    from settings import my_url, name, doc, last, RH, COD_RECONOCIMIENTO
    import init, bs4, logging, sys, re
    global contreconocimientos
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
        buscareconocimientos = containers[a].h3
        #print(buscareconocimientos)
        try:
            if buscareconocimientos.text == "Reconocimientos":
                all = a
                #print(all)
                break
        except AttributeError:
            pass

    if all != 0:
        containerb = containers[all]
        container = containerb.findAll("li")
        for x in range(0, len(container)):
            cont = container[x]
            info_reconocimientos = cont.text
            #Nombre Producto
            index1 = 0
            index2 = info_reconocimientos.find(',')
            NombreProducto = info_reconocimientos[index1:index2]
            #Insitucion
            index1 = info_reconocimientos.find(',') + 1
            index2 = info_reconocimientos.find('-')
            Institucion = info_reconocimientos[index1:index2]
            #Mes
            index1 = info_reconocimientos.rfind('-',0,len(info_reconocimientos)) + 2
            index2 = info_reconocimientos.find('de ',index1,len(info_reconocimientos))
            Mes = info_reconocimientos[index1:index2]
            #Programa Académico
            index1 = index2 + 3
            index2 = len(info_reconocimientos)
            Ano = info_reconocimientos[index1:index2]
            init.colciencias_reconocimientos.append(RH + ";"\
            + str(COD_RECONOCIMIENTO) + ";"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Mes.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Ano.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Institucion.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "\n")
            init.incolciencias_reconocimientos.append( \
            "REPLACE INTO `uapa_db`.`colciencias_reconocimientos`(`cod_colciencias_reconocimientos`,`cod_reconocimiento`,`cod_rh`,`nombre_reconocimiento`,`mes_reconocimiento`,`ano_reconocimiento`,`institucion_reconocimiento`) VALUES"
            + "('" + str(RH) + "R" + str(COD_RECONOCIMIENTO) + "',"\
            + str(COD_RECONOCIMIENTO) + ","\
            + "'" + str(RH) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Mes.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Ano.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Institucion.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "'"\
            + ");\n")

            COD_RECONOCIMIENTO = COD_RECONOCIMIENTO + 1
    else:
        logging.info(' El Docente ' + name + ' ' + last + ' no tiene Reconocimientos Asociado')
    contreconocimientos = [COD_RECONOCIMIENTO]
