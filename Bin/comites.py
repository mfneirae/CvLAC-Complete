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

def pcomitesextract():
    from settings import my_url, name, doc, last, RH, COD_PRODUCTO
    import init, bs4, logging, sys, re
    global contpcomites
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
        buscapcomites = containers[a].h3
        #print(buscapcomites)
        try:
            if buscapcomites.text == "Participación en comites de evaluación":
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
            info_pcomites = cont.text
            #Tipo Otra Produccion
            tipotex = tipotexno[x]
            tipo = tipotex.text
            Datos = tipo
            if tipo.strip() == "Datos complementarios - Participación en comités de evaluación - Profesor titular":
                tipo = "78"
            elif tipo.strip() == "Datos complementarios - Participación en comités de evaluación - Concurso docente":
                tipo = "79"
            elif tipo.strip() == "Datos complementarios - Participación en comités de evaluación - Jefe de cátedra":
                tipo = "80"
            elif tipo.strip() == "Datos complementarios - Participación en comités de evaluación - Evaluación de cursos":
                tipo = "81"
            elif tipo.strip() == "Datos complementarios - Participación en comités de evaluación - Acreditación de programas":
                tipo = "82"
            elif tipo.strip() == "Datos complementarios - Participación en comités de evaluación - Asignación de becas":
                tipo = "83"
            elif tipo.strip() == "Datos complementarios - Participación en comités de evaluación - Otra":
                tipo = "84"
            else:
                logging.critical('Añadir: ' + tipo)
                print ("ALERTA: Revisar el archivo Registros.log")
            #Nombre Producto
            index = info_pcomites.find('en:')
            index1 = info_pcomites.rfind(',',0,index) + 2
            NombreProducto = info_pcomites[index1:index]
            #Coautores
            index2 = index1
            index1 = 1
            coautores = info_pcomites[index1:index2]

            #INSTITUCIONES_ASOCIADAS
            index1 = info_pcomites.find('en:') + 3
            if info_pcomites.find("Palabras:") != -1:
                index2 = info_pcomites.find("Palabras:")
            elif info_pcomites.find("Areas:") != -1:
                index2 = info_pcomites.find("Areas:")
            elif info_pcomites.find("Sectores:") != -1:
                index2 = info_pcomites.find("Sectores:")
            else:
                index2 = len(info_pcomites)
            Instituciones = info_pcomites[index1:index2]
            #Palabras
            index1 = info_pcomites.find("Palabras:")
            index2 = info_pcomites.find("Areas:")
            index3 = info_pcomites.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_pcomites[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_pcomites[index1 + 9:index3]
            else:
                palabras = info_pcomites[index1 + 9:len(info_pcomites)]
            #Areas
            index1 = info_pcomites.find("Areas:")
            index2 = info_pcomites.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_pcomites[index1 + 6:index2]
            else:
                areas = info_pcomites[index1 + 6:len(info_pcomites)]
            #Sectores
            index1 = info_pcomites.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_pcomites[index1 + 9:len(info_pcomites)]
            init.rel_persona_producto_colciencias.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "0" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',Datos.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
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
            + re.sub(' +',' ',Instituciones.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" \
            + "\n")
            init.inrel_personas_producto_colciencias.append( \
            "REPLACE INTO `uapa_db`.`rel_personas_producto_colciencias`(`cod_producto`,`cod_rh`,`cod_tipo_producto`,`nombre_producto`,`cod_tipo_evento`,`evento_asociado`,`datos_complementarios`,`lugar`,`ano`,`ambito`,`palabras_clave`,`areas`,`sectores`,`coautores`,`vincula_coautores`,`editorial`,`volumen`,`paginas`,`doi`,`finalidad`,`instituciones_asociadas`,`tipo_vinculacion_institucion`) VALUES"
            + "('" + str(RH) + "',"\
            + str(COD_PRODUCTO) + ","\
            + re.sub(' +',' ',tipo.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ","\
            + "'" + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
            + "0" + ","\
            + "null" + ","\
            + "'" + re.sub(' +',' ',Datos.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(' +',' ',palabras.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
            + "'" + re.sub(' +',' ',areas.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
            + "'" + re.sub(' +',' ',sectores.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
            + "'" + re.sub(' +',' ',coautores.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(' +',' ',Instituciones.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
            + "null" + ");\n")
            init.colciencias_comites.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        logging.info(' El Docente ' + name + ' ' + last + 'no tiene Participaciones en Comités Asociadas')
    contpcomites = [COD_PRODUCTO]

def pjcomitesextract():
    from settings import my_url, name, doc, last, RH, COD_PRODUCTO
    import init, bs4, logging, sys, re
    global contpjcomites
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
        buscapjcomites = containers[a].h3
        #print(buscapjcomites)
        try:
            if buscapjcomites.text == "Jurado en comites de evaluación":
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
            info_pjcomites = cont.text
            #Tipo Otra Produccion
            tipotex = tipotexno[x]
            tipo = tipotex.text
            index1 = tipo.find('Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - ') + 76
            index2 = len(tipo)
            Datos = tipo
            Nivel = tipo[index1:index2]
            if tipo.strip() == "Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Pregrado":
                tipo = "85"
            elif tipo.strip() == "Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Especialización":
                tipo = "86"
            elif tipo.strip() == "Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Especialidad Médica":
                tipo = "87"
            elif tipo.strip() == "Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Maestría":
                tipo = "88"
            elif tipo.strip() == "Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Doctorado":
                tipo = "89"
            elif tipo.strip() == "Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Otra":
                tipo = "90"
            elif tipo.strip() == "Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Curso de perfeccionamiento/especialización":
                tipo = "91"
            else:
                logging.critical('Añadir: ' + tipo)
                print ("ALERTA: Revisar el archivo Registros.log")
            #Nombre Producto
            index1 = info_pjcomites.find('Titulo:') + 8
            index2 = info_pjcomites.find('Tipo de trabajo presentado:')
            NombreProducto = info_pjcomites[index1:index2]
            #Coautores
            index2 = index1 - 8
            index1 = 1
            coautores = info_pjcomites[index1:index2]
            #Tipo Trabajo Presentado
            index1 = info_pjcomites.find('Tipo de trabajo presentado:') + 28
            index2 = info_pjcomites.find('en:')
            TipoTrabajoPresentado = info_pjcomites[index1:index2]
            #Lugar
            index1 = info_pjcomites.find('en:') + 3
            index2 = info_pjcomites.find('programa académico')
            lugar = info_pjcomites[index1:index2]
            #Programa Académico
            index1 = info_pjcomites.find('programa académico') + 19
            index2 = info_pjcomites.find('Nombre del orientado')
            ProgramaAcademico = info_pjcomites[index1:index2]
            #Nombre del orientado
            index1 = info_pjcomites.find('Nombre del orientado:') + 22
            if info_pjcomites.find("Palabras:") != -1:
                index2 = info_pjcomites.find("Palabras:")
            elif info_pjcomites.find("Areas:") != -1:
                index2 = info_pjcomites.find("Areas:")
            elif info_pjcomites.find("Sectores:") != -1:
                index2 = info_pjcomites.find("Sectores:")
            else:
                index2 = len(info_pjcomites)
            NombreOrientado = info_pjcomites[index1:index2]
            #Palabras
            index1 = info_pjcomites.find("Palabras:")
            index2 = info_pjcomites.find("Areas:")
            index3 = info_pjcomites.find("Sectores:")
            if index1 == -1:
                palabras = ""
            elif index2 != -1:
                palabras = info_pjcomites[index1 + 9:index2]
            elif index2 == -1 and index3 != -1:
                palabras = info_pjcomites[index1 + 9:index3]
            else:
                palabras = info_pjcomites[index1 + 9:len(info_pjcomites)]
            #Areas
            index1 = info_pjcomites.find("Areas:")
            index2 = info_pjcomites.find("Sectores:")
            if index1 == -1:
                areas = ""
            elif index2 != -1:
                areas = info_pjcomites[index1 + 6:index2]
            else:
                areas = info_pjcomites[index1 + 6:len(info_pjcomites)]
            #Sectores
            index1 = info_pjcomites.find("Sectores:")
            if index1 == -1:
                sectores = ""
            else:
                sectores = info_pjcomites[index1 + 9:len(info_pjcomites)]
            init.rel_persona_producto_colciencias.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',Datos.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + "" + ";" \
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
            init.inrel_personas_producto_colciencias.append( \
            "REPLACE INTO `uapa_db`.`rel_personas_producto_colciencias`(`cod_producto`,`cod_rh`,`cod_tipo_producto`,`nombre_producto`,`cod_tipo_evento`,`evento_asociado`,`datos_complementarios`,`lugar`,`ano`,`ambito`,`palabras_clave`,`areas`,`sectores`,`coautores`,`vincula_coautores`,`editorial`,`volumen`,`paginas`,`doi`,`finalidad`,`instituciones_asociadas`,`tipo_vinculacion_institucion`) VALUES"
            + "('" + str(RH) + "',"\
            + str(COD_PRODUCTO) + ","\
            + re.sub(' +',' ',tipo.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ","\
            + "'" + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
            + "0" + ","\
            + "null" + ","\
            + "'" + re.sub(' +',' ',Datos.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "'" + re.sub(' +',' ',palabras.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
            + "'" + re.sub(' +',' ',areas.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
            + "'" + re.sub(' +',' ',sectores.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
            + "'" + re.sub(' +',' ',coautores.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ","\
            + "null" + ");\n")
            init.colciencias_comites.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + re.sub(' +',' ',TipoTrabajoPresentado.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',ProgramaAcademico.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',NombreOrientado.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + re.sub(' +',' ',Nivel.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        logging.info(' El Docente ' + name + ' ' + last + 'no tiene registros como Jurado en Comités Asociadas')
    contpjcomites = [COD_PRODUCTO]
