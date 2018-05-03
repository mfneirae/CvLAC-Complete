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


import init

f = open ("./Resultados/rel_persona_producto_colciencias.csv", "w")
for item in init.rel_persona_producto_colciencias:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()
f = open ("./Resultados/colciencias_apropiacion.csv", "w")

for item in init.colciencias_apropiacion:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/rel_persona_colciencias.csv", "w")
for item in init.rel_persona_colciencias:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/v_colciencias_tipo_producto.csv", "w")
for item in init.v_colciencias_tipo_producto:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/v_colciencias_tipo_evento.csv", "w")
for item in init.v_colciencias_tipo_evento:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/colciencias_prod_bibliografica.csv", "w")
for item in init.colciencias_prod_bibliografica:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/colciencias_prod_tecnica.csv", "w")
for item in init.colciencias_prod_tecnica:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/colciencias_comites.csv", "w")
for item in init.colciencias_comites:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()


f = open ("./Resultados/colciencias_reconocimientos.csv", "w")
for item in init.colciencias_reconocimientos:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/colciencias_idiomas.csv", "w")
for item in init.colciencias_idiomas:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()
