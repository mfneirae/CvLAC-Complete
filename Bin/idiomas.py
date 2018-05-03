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

def idiomasextract():
    from settings import my_url, name, doc, last, RH, COD_IDIOMA
    import init, bs4, logging, sys, re
    global contidiomas
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
        buscaidiomas = containers[a].h3
        #print(buscaidiomas)
        try:
            if buscaidiomas.text == "Idiomas":
                all = a
                #print(all)
                break
        except AttributeError:
            pass

    if all != 0:
        containerb = containers[all]
        container = containerb.findAll("tr")
        for x in range(2, len(container)):
            cont = container[x]
            info_idiomas = cont.text
            index1 = info_idiomas.find('\xa0') + 1
            index2 = info_idiomas.find('\n',index1,len(info_idiomas))
            idioma = info_idiomas[index1:index2]
            index1 = index2 + 1
            index2 = info_idiomas.find('\n',index1,len(info_idiomas))
            habla = info_idiomas[index1:index2]
            index1 = index2 + 1
            index2 = info_idiomas.find('\n',index1,len(info_idiomas))
            escribe = info_idiomas[index1:index2]
            index1 = index2 + 1
            index2 = info_idiomas.find('\n',index1,len(info_idiomas))
            lee = info_idiomas[index1:index2]
            index1 = index2 + 1
            index2 = info_idiomas.find('\n',index1,len(info_idiomas))
            entiende = info_idiomas[index1:index2]
            init.colciencias_idiomas.append(RH + ";"\
            + str(COD_IDIOMA) + ";"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',idioma.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',habla.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',lee.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',escribe.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',entiende.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "\n")
            init.incolciencias_idiomas.append( \
            "REPLACE INTO `uapa_db`.`colciencias_idiomas`(`cod_colciencias_idiomas`,`cod_idiomas`,`cod_rh`,`idioma_persona`,`habla`,`lee`,`escribe`,`entiende`) VALUES"
            + "('" + str(RH) + "D" + str(COD_IDIOMA) + "',"\
            + str(COD_IDIOMA) + ","\
            + "'" + str(RH) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',idioma.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',habla.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',lee.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',escribe.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "',"\
            + "'" + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',entiende.strip().replace('"',"").replace("'","").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + "'"\
            + ");\n")

            COD_IDIOMA = COD_IDIOMA + 1
    else:
        logging.info(' El Docente ' + name + ' ' + last + 'no tiene idiomas Asociado')
    contidiomas = [COD_IDIOMA]
