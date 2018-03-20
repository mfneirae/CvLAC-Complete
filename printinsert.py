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

f = open ("./Resultados/inv_colciencias_tipo_producto.sql", "w")
for item in init.inv_colciencias_tipo_producto:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/inv_colciencias_tipo_evento.sql", "w")
for item in init.inv_colciencias_tipo_evento:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/inrel_persona_colciencias.sql", "w")
for item in init.inrel_persona_colciencias:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/incolciencias_apropiacion.sql", "w")
init.incolciencias_apropiacion = [w.replace("''", 'null') for w in init.incolciencias_apropiacion]
init.incolciencias_apropiacion = [w.replace(",,", ',null,') for w in init.incolciencias_apropiacion]
for item in init.incolciencias_apropiacion:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/inrel_personas_producto_colciencias.sql", "w")
init.inrel_personas_producto_colciencias = [w.replace("''", 'null') for w in init.inrel_personas_producto_colciencias]
init.inrel_personas_producto_colciencias = [w.replace(",,", ',null,') for w in init.inrel_personas_producto_colciencias]
for item in init.inrel_personas_producto_colciencias:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/incolciencias_prod_tecnica.sql", "w")
init.incolciencias_prod_tecnica = [w.replace("''", 'null') for w in init.incolciencias_prod_tecnica]
init.incolciencias_prod_tecnica = [w.replace(",,", ',null,') for w in init.incolciencias_prod_tecnica]
for item in init.incolciencias_prod_tecnica:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()
