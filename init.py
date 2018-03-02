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

def inicio():
    global RE_PERSONA_PRODUCTO
    global APROPIACION
    global RE_DNI_CODRH
    RE_PERSONA_PRODUCTO = ["COD_RH; \
COD_PRODUCTO; \
COD_TIPO_PRODUCTO; \
NOMPRE_PRODUCTO; \
EVENTO_ASOCIADO; \
DATOS_COMPLEMENTARIOS; \
LUGAR; \
AÑO; \
AMBITO; \
PALABRAS_CLAVE; \
ÁREAS; \
SECTORES; \
COAUTORES; \
VINCULA_COAUTORES; \
EDITORIAL; \
VOLUMEN; \
PAGINAS; \
DOI; \
FINALIDAD; \
INSTITUCIONES_ASOCIADAS; \
TIPO_VINCULACION_INSTITUCION\n"]
    APROPIACION = [ "COD_RH; \
COD_PRODUCTO; \
TIPO_EVENTO;\
TIPO_RED; \
FECHA_INI; \
AÑO_INI; \
MES_INI; \
FECHA_FIN; \
AÑO_FIN; \
MES_FIN\n"]
    RE_DNI_CODRH = [ "DNI; \
COD_RH\n"]
