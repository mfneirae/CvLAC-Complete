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
    global TIPO_PRODUCTO
    global TIPO_EVENTO
    RE_PERSONA_PRODUCTO = ["COD_RH; \
    COD_PRODUCTO; \
    COD_TIPO_PRODUCTO; \
    NOMPRE_PRODUCTO; \
    COD_TIPO_EVENTO; \
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
    FECHA_INI; \
    AÑO_INI; \
    MES_INI; \
    FECHA_FIN; \
    AÑO_FIN; \
    MES_FIN\n"]

    TIPO_PRODUCTO = [ "COD_TIPO_PRODUCTO; \
    TIPO_PRODUCTO_COL; \
    SUB_TIPO_PRODUCTO_COL; \
    TIPO_UAPA; \
    TIPO_PREGRADO; \
    TIPO_POSGRADO\n \
    1; \
    Redes de conocimiento; \
    Redes de conocimiento; \
    Redes de conocimiento; \
    ;\
    ;\n \
    2; \
    Producción bibliográfica - Trabajos en eventos (Capítulos de memoria) - Completo; \
    Capítulos de memoria; \
    Capítulos de memoria; \
    ;\
    ;\n \
    3; \
    Producción técnica - Presentación de trabajo - Comunicación; \
    Presentación de trabajo; \
    Trabajo de Comunicación; \
    ;\
    ;\n \
    4; \
    Demás trabajos - Demás trabajos - Póster; \
    Demás trabajos; \
    Poster; \
    ;\
    ;\
    5; \
    Producción técnica - Presentación de trabajo - Conferencia; \
    Presentación de trabajo; \
    Conferencia; \
    ;\
    ;\n \
    6; \
    Producción técnica - Presentación de trabajo - Ponencia; \
    Presentación de trabajo; \
    Ponencia; \
    ;\
    ;\n \
    7; \
    Estrategias pedagógicas para el fomento a la CTI; \
    Estrategias pedagógicas; \
    Estrategias pedagógicas; \
    ;\n"]

    TIPO_EVENTO = [ "COD_TIPO_EVENTO; \
    TIPO_EVENTO_COL; \
    TIPO_EVENTO_UAPA; \
    TIPO_EVENTO_PREGRADO; \
    TIPO_EVENTO_POSGRADO\n \
    E1; \
    Otro; \
    Otro; \
    ; \
    \n \
    E2; \
    Taller; \
    Taller; \
    ; \
    \n \
    E3; \
    Congreso; \
    Congreso; \
    ; \
    \n \
    E4; \
    Encuentro; \
    Encuentro; \
    ; \
    \n \
    E5; \
    Seminario; \
    Seminario; \
    ; \
    \n \
    E6; \
    Simposio; \
    Simposio; \
    ;\n"]

    RE_DNI_CODRH = [ "DNI; \
    COD_RH\n"]
