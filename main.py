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
import openpyxl
import init
import apropiacion
import produccion_bibliografica
global COD_PRODUCTO
wb = openpyxl.load_workbook('./Base.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
total = sheet.max_row + 2
COD_PRODUCTO = 1;
init.inicio()
for x in range(2,total-1):
    doc = sheet['A'+str(x)].value
    name = sheet['B'+str(x)].value
    last = sheet['C'+str(x)].value
    my_url = sheet['E'+str(x)].value
    depar = sheet['D'+str(x)].value
    index1 = my_url.find("cod_rh=") + 7
    index2 = len(my_url)
    RH = my_url[index1:index2]
    init.RE_DNI_CODRH.append(str(doc) + ";"\
    + str(RH) \
    + "\n")
    if my_url != '-':
        apropiacion.evenextract()
        from apropiacion import conteventos
        COD_PRODUCTO = int("".join(str(x) for x in conteventos))
        apropiacion.redesextract()
        from apropiacion import contredes
        COD_PRODUCTO = int("".join(str(x) for x in contredes))
        apropiacion.estrategiaextract()
        from apropiacion import contEstrategia
        COD_PRODUCTO = int("".join(str(x) for x in contEstrategia))
        produccion_bibliografica.artiextract()
        from produccion_bibliografica import contarticulo
        COD_PRODUCTO = int("".join(str(x) for x in contarticulo))
        # publib.pubextract()
        # pubcaplib.pubextract()
        # pubsoft.pubextract()
    else:
        pass
    COD_PRODUCTO = 1;

import printcsv

print ("Done! :]")
