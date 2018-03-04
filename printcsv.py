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
import init

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

f = open ("./Resultados/TIPO_PRODUCTO.csv", "w")
for item in init.TIPO_PRODUCTO:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/TIPO_EVENTO.csv", "w")
for item in init.TIPO_EVENTO:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()
