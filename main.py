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

wb = openpyxl.load_workbook('./Base.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
total = sheet.max_row +1
COD_PRODUCTO = 1;

init.inicio()
for x in range(2,total):
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
        COD_PRODUCTO = COD_PRODUCTO + 1
        # pubarti.pubextract()
        # publib.pubextract()
        # pubcaplib.pubextract()
        # pubsoft.pubextract()
    else:
        pass
    COD_PRODUCTO = 1;
    

f = open ("./Resultados/RE_PERSONA_PRODUCTO.csv", "w")
for item in init.RE_PERSONA_PRODUCTO:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass


f.close()

f = open ("./Resultados/APROPIACION.csv", "w")
for item in init.APROPIACION:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass


f.close()

f = open ("./Resultados/RE_DNI_CODRH.csv", "w")
for item in init.RE_DNI_CODRH:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass


f.close()

print ("Done! :]")
