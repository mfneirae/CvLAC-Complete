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
def artiextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import bs4
    import init
    import re
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
                print(tipo)
            Tipoarticulo = info_articulo[index1:index2]
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
            index2 = info_articulo.find("\nv.",index1,index1 + 50)
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
            init.RE_PERSONA_PRODUCTO.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + tipo + ";"\
            + NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","") + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + lugar.strip().replace("\r\n","") + ";" \
            + AnoEvento.strip().replace("\r\n","") + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',coautores.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + "" + ";" \
            + editorial.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","") + ";" \
            + Volumen.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","") + ";" \
            + "" + ";" \
            + doi.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","") + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" \
            + "\n")
            init.PROD_BIBLIOGRAFICA.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + Revista.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","") + ";" \
            + ISSN.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","") + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(' +',' ',fasciculo.strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ";" \
            + Pagini.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","") + ";" \
            + Pagfin.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","") + ";" \
            + "\n")
            COD_PRODUCTO = COD_PRODUCTO + 1
    else:
        print("El Docente ",name," ",last," ","no tiene Artículos Asociados")
    contarticulo = [COD_PRODUCTO]
