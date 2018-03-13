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

def inicio():
    global RE_PERSONA_PRODUCTO
    global APROPIACION
    global RE_DNI_CODRH
    global TIPO_PRODUCTO
    global TIPO_EVENTO
    global PROD_BIBLIOGRAFICA
    global PROD_TECNICA
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

    PROD_BIBLIOGRAFICA = [ "COD_RH; \
    COD_PRODUCTO; \
    REVISTA; \
    ISSN/ISBN; \
    LIBRO/REVISTA_ORIGINAL_TRAD; \
    NOMBRE_LIBRO/REVISTA_TRAD; \
    NOMRE_AUTOR_ORIGINAL_TRAD; \
    IDIOMA_ORIGINAL; \
    IDIOMA_TRADUCCION; \
    NOMBRE_CAPITULO; \
    FASCICULO; \
    PAGINA_INICIAL; \
    PAGINA_FINAL\n"]

    TIPO_PRODUCTO = [ "COD_TIPO_PRODUCTO; \
    TIPO_PRODUCTO_COL; \
    SUB_TIPO_PRODUCTO_COL; \
    TIPO_UAPA; \
    TIPO_PREGRADO; \
    TIPO_POSGRADO\n \
    0; \
    Evento sin producto asociado; \
    Evento sin producto asociado; \
    Evento sin producto asociado; \
    ;\
    ;\n \
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
    ;\n \
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
    ;\
    ;\n \
    8; \
    Producción bibliográfica - Artículo - Publicado en revista especializada; \
    Publicado en revista especializada; \
    Artículo; \
    ;\
    ;\n \
    9; \
    Producción bibliográfica - Artículo - Corto (Resumen); \
    Corto (Resumen); \
    Artículo; \
    ;\
    ;\n \
    10; \
    Estrategias pedagógicas para el fomento a la CTI; \
    Estrategias pedagógicas; \
    Estrategias pedagógicas; \
    ;\
    ;\n \
    11; \
    Producción bibliográfica - Artículo - Caso clínico; \
    Caso Clínico; \
    Artículo; \
    ;\
    ;\n \
    12; \
    Producción bibliográfica - Trabajos en eventos (Capítulos de memoria) - Resumen; \
    Capítulo de Memoria; \
    Resumen; \
    ;\
    ;\n \
    13; \
    Producción técnica - Presentación de trabajo - Congreso; \
    Congreso; \
    Congreso; \
    ;\
    ;\n \
    14; \
    Producción técnica - Presentación de trabajo - Simposio; \
    Simposio; \
    Simposio; \
    ;\
    ;\n \
    15; \
    Producción técnica - Presentación de trabajo - Seminario; \
    Seminario; \
    Seminario; \
    ;\
    ;\n \
    16; \
    Producción técnica - Presentación de trabajo - Otro; \
    Otro; \
    Otro; \
    ;\
    ;\n \
    17; \
    Producción bibliográfica - Libro - Libro resultado de investigación; \
    Libro resultado de investigación; \
    Libro; \
    ;\
    ;\n \
    18; \
    Producción bibliográfica - Libro - Otro libro publicado; \
    Otro libro publicado; \
    Libro - Otro; \
    ;\
    ;\n \
    19; \
    Producción bibliográfica - Libro - Libro pedagógico y/o de divulgación; \
    Libro pedagógico y/o de divulgación; \
    Libro - pedagógico; \
    ;\
    ;\n \
    20; \
    Otro capítulo de libro publicado; \
    Otro capítulo de libro; \
    Capítulo de libro - Otro; \
    ;\
    ;\n \
    21; \
    Capítulo de libro; \
    Capítulo de libro; \
    Capítulo de libro; \
    ;\
    ;\n \
    22; \
    Producción bibliográfica - Otro artículo publicado - Periódico de noticias; \
    Periódico de noticias; \
    Otro; \
    ;\
    ;\n \
    23; \
    Producción bibliográfica - Otro artículo publicado - Revista de divulgación; \
    Revista de divulgación; \
    Otro; \
    ;\
    ;\n \
    24; \
    Producción bibliográfica - Otro artículo publicado - Cartas al editor; \
    Cartas al editor; \
    Otro; \
    ;\
    ;\n \
    25; \
    Producción bibliográfica - Otro artículo publicado - Reseñas de libros; \
    Reseñas de libros; \
    Otro; \
    ;\
    ;\n \
    26; \
    Producción bibliográfica - Otro artículo publicado - Columna de opinión; \
    Columnas de opinión; \
    Otro; \
    ;\
    ;\n \
    27; \
    Producción bibliográfica - Documento de trabajo (Working Paper); \
    Documento de trabajo (Working Paper); \
    Otro; \
    ;\
    ;\n \
    28; \
    Producción bibliográfica - Traducciones - Artículo; \
    Traducciones - Artículo; \
    Traducciones; \
    ;\
    ;\n \
    29; \
    Producción bibliográfica - Traducciones - Libro; \
    Traducciones - Libro; \
    Traducciones; \
    ;\
    ;\n \
    30; \
    Producción bibliográfica - Traducciones - Otra; \
    Traducciones - Otra; \
    Traducciones; \
    ;\
    ;\n \
    31; \
    Producción bibliográfica - Otra producción bibliográfica - Introducción; \
    Introducción; \
    Otro; \
    ;\
    ;\n \
    32; \
    Producción bibliográfica - Otra producción bibliográfica - Prólogo; \
    Prólogo; \
    Otro; \
    ;\
    ;\n \
    33; \
    Producción bibliográfica - Otra producción bibliográfica - Epílogo; \
    Epílogo; \
    Otro; \
    ;\
    ;\n \
    34; \
    Producción bibliográfica - Otra producción bibliográfica - Otra; \
    Otra; \
    Otro; \
    ;\
    ;\n \
    35; \
    Producción técnica - Softwares - Computacional; \
    Software; \
    Software; \
    ;\
    ;\n \
    36; \
    Producción técnica - Productos tecnológicos - Gen Clonado; \
    Productos tecnológicos - Gen Clonado; \
    Productos tecnológicos; \
    ;\
    ;\n \
    37; \
    Producción técnica - Productos tecnológicos - Coleccion biologica de referencia con informacion sistematizada; \
    Productos tecnológicos - Coleccion biologica de referencia con informacion sistematizada; \
    Productos tecnológicos; \
    ;\
    ;\n \
    38; \
    Producción técnica - Productos tecnológicos - Otro; \
    Productos tecnológicos - Otro; \
    Productos tecnológicos; \
    ;\
    ;\n \
    39; \
    Producción técnica - Productos tecnológicos - Base de datos de referencia para investigación; \
    Productos tecnológicos - Base de datos de referencia para investigación; \
    Productos tecnológicos; \
    ;\
    ;\n \
    N; \
    el final; \
    el final; \
    el final; \
    ;\
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

    PROD_TECNICA = [ "COD_RH; \
    COD_PRODUCTO; \
    RNOMBRE_COMERCIAL; \
    CONTRATO/REGISTRO; \
    TITULAR; \
    DURACION; \
    REGULACION; \
    TIPO-REGULACION; \
    CICLO; \
    ESTADO_VARIEDAD; \
    PLATAFORMA; \
    AMBIENTE\n"]
