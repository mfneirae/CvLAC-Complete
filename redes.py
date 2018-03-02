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
def redesextract():
    from main import my_url, name, doc, last, depar, RH, COD_PRODUCTO
    import init
    import bs4
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    all = 0
    a = 0
    x = 0
    y = 0
    auto = ""
    vincula = ""
    insti = ""
    vinculain = ""
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("table")
    for a in range(0,len(containers)):
        buscaeventos = containers[a].h3
        #print(buscaeventos)
        try:
            if buscaeventos.text == "Redes de conocimiento especializado":
                all = a
                #print(all)
                break
        except AttributeError:
            pass
    if all != 0:
