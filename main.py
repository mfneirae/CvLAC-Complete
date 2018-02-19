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
wb = openpyxl.load_workbook('./Base.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
total = sheet.max_row
import init
init.inicio()
for x in range(2,total):
    doc = sheet['A'+str(x)].value
    name = sheet['B'+str(x)].value
    last = sheet['C'+str(x)].value
    my_url = sheet['E'+str(x)].value
    depar = sheet['D'+str(x)].value
    if my_url != '-':
        import Eventos
        import pubeven
        import pubarti
        import publib
        import pubsoft
        import pubcaplib
        Eventos.evenextract()
        pubeven.pubextract()
        pubarti.pubextract()
        publib.pubextract()
        pubcaplib.pubextract()
        pubsoft.pubextract()
    else:
        pass

f = open ("./Resultados/Eventos.csv", "w")
for item in init.dbact:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()
f = open ("./Resultados/Publicaciones.csv", "w")
for item in init.dbpub:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()
print ("Done! :]")
