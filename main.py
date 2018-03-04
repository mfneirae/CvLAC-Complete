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
import pubeventos
import pubarti
import publib
import pubsoft
import pubcaplib
import redes
import estrategias
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
        pubeventos.evenextract()
        from pubeventos import conteventos
        COD_PRODUCTO = int("".join(str(x) for x in conteventos))
        redes.redesextract()
        from redes import contredes
        COD_PRODUCTO = int("".join(str(x) for x in contredes))
        estrategias.estrategiaextract()
        from estrategias import contEstrategia
        COD_PRODUCTO = int("".join(str(x) for x in contEstrategia))
        # pubarti.pubextract()
        # publib.pubextract()
        # pubcaplib.pubextract()
        # pubsoft.pubextract()
    else:
        pass
    COD_PRODUCTO = 1;

import printcsv

print ("Done! :]")
