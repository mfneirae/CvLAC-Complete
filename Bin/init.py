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
    #Tablas CSV
    global rel_persona_producto_colciencias
    global colciencias_apropiacion
    global rel_persona_colciencias
    global v_colciencias_tipo_producto
    global v_colciencias_tipo_evento
    global colciencias_prod_bibliografica
    global colciencias_prod_tecnica
    global colciencias_comites
    global colciencias_reconocimientos
    global colciencias_idiomas
    #Tablas Insert
    global inrel_personas_producto_colciencias
    global incolciencias_apropiacion
    global inrel_persona_colciencias
    global inv_colciencias_tipo_producto
    global inv_colciencias_tipo_evento
    global incolciencias_prod_bibliografica
    global incolciencias_prod_tecnica
    global incolciencias_comites
    global incolciencias_reconocimientos
    global incolciencias_idiomas
    rel_persona_producto_colciencias = ["COD_RH; \
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

    colciencias_apropiacion = [ "COD_COLCIENCIAS_APROPIACION; \
COD_RH; \
COD_PRODUCTO; \
FECHA_INI; \
AÑO_INI; \
MES_INI; \
FECHA_FIN; \
AÑO_FIN; \
MES_FIN\n"]

    colciencias_comites = [ "COD_RH; \
COD_PRODUCTO; \
TIPO_TRABAJO_PRESENTADO; \
PROGRAMA_ACADEMICO; \
NOMBRE_ORIENTADO; \
NIVEL\n"]

    colciencias_reconocimientos = [ "COD_RH; \
COD_RECONOCIMIENTO; \
NOMBRE_RECONOCIMIENTO; \
MES_RECONOCIMIENTO; \
AÑO_RECONOCIMIENTO; \
INSTITUCION_RECONOCIMIENTO\n"]

    colciencias_idiomas = [ "COD_RH; \
COD_IDIOMA; \
NOMBRE_IDIOMA; \
HABLA; \
ESCRIBE; \
LEE\
ENTIENDE\n"]

    colciencias_prod_bibliografica = [ "COD_RH; \
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

    v_colciencias_tipo_producto = [ "COD_TIPO_PRODUCTO; \
TIPO_PRODUCTO_COL; \
SUB_TIPO_PRODUCTO_COL; \
TIPO_UAPA; \
TIPO_PREGRADO; \
TIPO_POSGRADO\n\
0; \
Evento sin producto asociado; \
Evento sin producto asociado; \
Evento sin producto asociado; \
;\
;\n\
1; \
Redes de conocimiento; \
Redes de conocimiento; \
Redes de conocimiento; \
;\
;\n\
2; \
Producción bibliográfica - Trabajos en eventos (Capítulos de memoria) - Completo; \
Capítulos de memoria; \
Capítulos de memoria; \
;\
;\n\
3; \
Producción técnica - Presentación de trabajo - Comunicación; \
Presentación de trabajo; \
Trabajo de Comunicación; \
;\
;\n\
4; \
Demás trabajos - Demás trabajos - Póster; \
Demás trabajos; \
Poster; \
;\
;\n\
5; \
Producción técnica - Presentación de trabajo - Conferencia; \
Presentación de trabajo; \
Conferencia; \
;\
;\n\
6; \
Producción técnica - Presentación de trabajo - Ponencia; \
Presentación de trabajo; \
Ponencia; \
;\
;\n\
7; \
Estrategias pedagógicas para el fomento a la CTI; \
Estrategias pedagógicas; \
Estrategias pedagógicas; \
;\
;\n\
8; \
Producción bibliográfica - Artículo - Publicado en revista especializada; \
Publicado en revista especializada; \
Artículo; \
;\
;\n\
9; \
Producción bibliográfica - Artículo - Corto (Resumen); \
Corto (Resumen); \
Artículo; \
;\
;\n\
10; \
Estrategias pedagógicas para el fomento a la CTI; \
Estrategias pedagógicas; \
Estrategias pedagógicas; \
;\
;\n\
11; \
Producción bibliográfica - Artículo - Caso clínico; \
Caso Clínico; \
Artículo; \
;\
;\n\
12; \
Producción bibliográfica - Trabajos en eventos (Capítulos de memoria) - Resumen; \
Capítulo de Memoria; \
Resumen; \
;\
;\n\
13; \
Producción técnica - Presentación de trabajo - Congreso; \
Congreso; \
Congreso; \
;\
;\n\
14; \
Producción técnica - Presentación de trabajo - Simposio; \
Simposio; \
Simposio; \
;\
;\n\
15; \
Producción técnica - Presentación de trabajo - Seminario; \
Seminario; \
Seminario; \
;\
;\n\
16; \
Producción técnica - Presentación de trabajo - Otro; \
Otro; \
Otro; \
;\
;\n\
17; \
Producción bibliográfica - Libro - Libro resultado de investigación; \
Libro resultado de investigación; \
Libro; \
;\
;\n\
18; \
Producción bibliográfica - Libro - Otro libro publicado; \
Otro libro publicado; \
Libro - Otro; \
;\
;\n\
19; \
Producción bibliográfica - Libro - Libro pedagógico y/o de divulgación; \
Libro pedagógico y/o de divulgación; \
Libro - pedagógico; \
;\
;\n\
20; \
Otro capítulo de libro publicado; \
Otro capítulo de libro; \
Capítulo de libro - Otro; \
;\
;\n\
21; \
Capítulo de libro; \
Capítulo de libro; \
Capítulo de libro; \
;\
;\n\
22; \
Producción bibliográfica - Otro artículo publicado - Periódico de noticias; \
Periódico de noticias; \
Otro; \
;\
;\n\
23; \
Producción bibliográfica - Otro artículo publicado - Revista de divulgación; \
Revista de divulgación; \
Otro; \
;\
;\n\
24; \
Producción bibliográfica - Otro artículo publicado - Cartas al editor; \
Cartas al editor; \
Otro; \
;\
;\n\
25; \
Producción bibliográfica - Otro artículo publicado - Reseñas de libros; \
Reseñas de libros; \
Otro; \
;\
;\n\
26; \
Producción bibliográfica - Otro artículo publicado - Columna de opinión; \
Columnas de opinión; \
Otro; \
;\
;\n\
27; \
Producción bibliográfica - Documento de trabajo (Working Paper); \
Documento de trabajo (Working Paper); \
Otro; \
;\
;\n\
28; \
Producción bibliográfica - Traducciones - Artículo; \
Traducciones - Artículo; \
Traducciones; \
;\
;\n\
29; \
Producción bibliográfica - Traducciones - Libro; \
Traducciones - Libro; \
Traducciones; \
;\
;\n\
30; \
Producción bibliográfica - Traducciones - Otra; \
Traducciones - Otra; \
Traducciones; \
;\
;\n\
31; \
Producción bibliográfica - Otra producción bibliográfica - Introducción; \
Introducción; \
Otro; \
;\
;\n\
32; \
Producción bibliográfica - Otra producción bibliográfica - Prólogo; \
Prólogo; \
Otro; \
;\
;\n\
33; \
Producción bibliográfica - Otra producción bibliográfica - Epílogo; \
Epílogo; \
Otro; \
;\
;\n\
34; \
Producción bibliográfica - Otra producción bibliográfica - Otra; \
Otra; \
Otro; \
;\
;\n\
35; \
Producción técnica - Softwares - Computacional; \
Software; \
Software; \
;\
;\n\
36; \
Producción técnica - Productos tecnológicos - Gen Clonado; \
Productos tecnológicos - Gen Clonado; \
Productos tecnológicos; \
;\
;\n\
37; \
Producción técnica - Productos tecnológicos - Coleccion biologica de referencia con informacion sistematizada; \
Productos tecnológicos - Coleccion biologica de referencia con informacion sistematizada; \
Productos tecnológicos; \
;\
;\n\
38; \
Producción técnica - Productos tecnológicos - Otro; \
Productos tecnológicos - Otro; \
Productos tecnológicos; \
;\
;\n\
39; \
Producción técnica - Productos tecnológicos - Base de datos de referencia para investigación; \
Productos tecnológicos - Base de datos de referencia para investigación; \
Productos tecnológicos; \
;\
;\n\
40; \
Producción técnica - Diseño Industrial; \
Diseño Industrial; \
Otro; \
;\
;\n\
41; \
Producción técnica - Esquema de circuito integrado; \
Esquema de circuito integrado; \
Otro; \
;\
;\n\
42; \
Producción técnica - Innovaciones generadas de producción empresarial - Organizacional; \
Innovaciones generadas de producción empresarial - Organizacional; \
Innovaciones; \
;\
;\n\
43; \
Producción técnica - Innovaciones generadas de producción empresarial - Empresarial; \
Innovaciones generadas de producción empresarial - Empresarial; \
Innovaciones; \
;\
;\n\
44; \
Producción técnica - Variedad animal; \
Variedad animal; \
Otro; \
;\
;\n\
45; \
Producción técnica - Innovación de proceso o procedimiento; \
Innovación de proceso o procedimiento; \
Innovación; \
;\
;\n\
46; \
Producción técnica - Cartas, mapas o similares - Aerofotograma; \
Aerofotograma; \
Otro; \
;\
;\n\
47; \
Producción técnica - Cartas, mapas o similares - Carta; \
Carta; \
Otro; \
;\
;\n\
48; \
Producción técnica - Cartas, mapas o similares - Fotograma; \
Fotograma; \
Otro; \
;\
;\n\
49; \
Producción técnica - Cartas, mapas o similares - Mapa; \
Mapa; \
Otro; \
;\
;\n\
50; \
Producción técnica - Cartas, mapas o similares - Otra; \
Otra; \
Otro; \
;\
;\n\
51; \
Producción técnica - Variedad vegetal; \
Variedad vegetal; \
Otro; \
;\
;\n\
52; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Servicios de proyectos de IDI; \
Servicios de proyectos de IDI; \
Otro; \
;\
;\n\
53; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Comercialización de tecnología; \
Comercialización de tecnología; \
Otro; \
;\
;\n\
54; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Análisis de competitividad; \
Análisis de competitividad; \
Otro; \
;\
;\n\
55; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Informe técnico; \
Informe técnico; \
Otro; \
;\
;\n\
56; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Otro; \
Otro; \
Otro; \
;\
;\n\
57; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Acciones de transferencia tecnológica; \
Acciones de transferencia tecnológica; \
Otro; \
;\
;\n\
58; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Desarrollo de productos; \
Desarrollo de productos; \
Otro; \
;\
;\n\
59; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Implementación de sistemas de análisis; \
Implementación de sistemas de análisis; \
Otro; \
;\
;\n\
60; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Consultoría en artes,arquitectura y diseño; \
Consultoría en artes,arquitectura y diseño; \
Otro; \
;\
;\n\
61; \
Producción técnica - Regulación, norma, reglamento o legislación - Ambiental o de Salud; \
Regulación, norma, reglamento o legislación - Ambiental o de Salud; \
Otro; \
;\
;\n\
62; \
Producción técnica - Regulación, norma, reglamento o legislación - Educativa; \
Regulación, norma, reglamento o legislación - Educativa; \
Otro; \
;\
;\n\
63; \
Producción técnica - Regulación, norma, reglamento o legislación - Social; \
Regulación, norma, reglamento o legislación - Social; \
Otro; \
;\
;\n\
64; \
Producción técnica - Regulación, norma, reglamento o legislación - Técnica; \
Regulación, norma, reglamento o legislación - Técnica; \
Otro; \
;\
;\n\
65; \
Producción técnica - Regulación, norma, reglamento o legislación - Guía de práctica clínica; \
Regulación, norma, reglamento o legislación - Guía de práctica clínica; \
Otro; \
;\
;\n\
66; \
Producción técnica - Regulación, norma, reglamento o legislación - Proyecto de ley; \
Regulación, norma, reglamento o legislación - Proyecto de ley; \
Otro; \
;\
;\n\
67; \
Producción técnica - Reglamento Técnico; \
Reglamento Técnico; \
Otro; \
;\
;\n\
68; \
Producción técnica - Empresa de base tecnológica - Spin-off; \
Empresa de base tecnológica - Spin-off; \
Otro; \
;\
;\n\
69; \
Producción técnica - Empresa de base tecnológica - Start-up; \
Empresa de base tecnológica - Start-up; \
Otro; \
;\
;\n\
70; \
Demás trabajos - Demás trabajos; \
Demás trabajos; \
Otro; \
;\
;\n\
71; \
Producción técnica - Signos; \
Signos; \
Otro; \
;\
;\n\
72; \
Producción técnica - Softwares - Multimedia; \
Multimedia; \
Software; \
;\
;\n\
73; \
Producción técnica - Softwares - Otra; \
Softwares - Otra; \
Software; \
;\
;\n\
74; \
Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Básica; \
Técnica - Básica; \
Otro; \
;\
;\n\
75; \
Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Ensayo; \
Técnica - Ensayo; \
Otro; \
;\
;\n\
76; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Servicios de Proyectos de I+D+I; \
Servicios de Proyectos de I+D+I; \
Otro; \
;\
;\n\
77; \
Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Proceso; \
Técnica - Proceso; \
Otro; \
;\
;\n\
78; \
Datos complementarios - Participación en comités de evaluación - Profesor titular; \
Participación en comités de evaluación - Profesor titular; \
Comités; \
;\
;\n\
79; \
Datos complementarios - Participación en comités de evaluación - Concurso docente; \
Participación en comités de evaluación - Concurso docente; \
Comités; \
;\
;\n\
80; \
Datos complementarios - Participación en comités de evaluación - Jefe de cátedra; \
Participación en comités de evaluación - Jefe de cátedra; \
Comités; \
;\
;\n\
81; \
Datos complementarios - Participación en comités de evaluación - Evaluación de cursos; \
Participación en comités de evaluación - Evaluación de cursos; \
Comités; \
;\
;\n\
82; \
Datos complementarios - Participación en comités de evaluación - Acreditación de programas; \
Participación en comités de evaluación - Acreditación de programas; \
Comités; \
;\
;\n\
83; \
Datos complementarios - Participación en comités de evaluación - Asignación de becas; \
Participación en comités de evaluación - Asignación de becas; \
Comités; \
;\
;\n\
84; \
Datos complementarios - Participación en comités de evaluación - Otra; \
Participación en comités de evaluación - Otra; \
Comités; \
;\
;\n\
85; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Pregrado; \
Jurado Pregrado; \
Comités; \
;\
;\n\
86; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Especialización; \
Jurado Especialización; \
Comités; \
;\
;\n\
87; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Especialidad Médica; \
Jurado Especialidad Médica; \
Comités; \
;\
;\n\
88; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Maestría; \
Jurado Maestría; \
Comités; \
;\
;\n\
89; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Doctorado; \
Jurado Doctorado; \
Comités; \
;\
;\n\
90; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Otra; \
Jurado Otra; \
Comités; \
;\
;\n\
91; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Curso de perfeccionamiento/especialización; \
Jurado Especializaciones; \
Comités; \
;\
;\n"]
# N; \
# el final; \
# el final; \
# el final; \
# ;\
# ;\n"]

    v_colciencias_tipo_evento = [ "COD_TIPO_EVENTO; \
TIPO_EVENTO_COL; \
TIPO_EVENTO_UAPA; \
TIPO_EVENTO_PREGRADO; \
TIPO_EVENTO_POSGRADO\n\
0; \
Sin Información; \
Sin Información; \
; \
\n\
1; \
Otro; \
Otro; \
; \
\n\
2; \
Taller; \
Taller; \
; \
\n\
3; \
Congreso; \
Congreso; \
; \
\n\
4; \
Encuentro; \
Encuentro; \
; \
\n\
5; \
Seminario; \
Seminario; \
; \
\n\
6; \
Simposio; \
Simposio; \
;\n"]

    rel_persona_colciencias = [ "DNI; \
COD_RH\n"]

    colciencias_prod_tecnica = [ "COD_COLCIENCIAS_PROD_TECNICA; \
COD_RH; \
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

#***************************************************************************
#Insert
#***************************************************************************
    inv_colciencias_tipo_producto = [ "REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`cod_tipo_producto`,\
`tipo_producto_col`,\
`sub_tipo_producto_col`,\
`tipo_uapa`) VALUES (\
0,\
'Evento sin producto asociado',\
'Evento sin producto asociado',\
'Evento sin producto asociado');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
1,\
'Redes de conocimiento',\
'Redes de conocimiento',\
'Redes de conocimiento');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
2,\
'Producción bibliográfica - Trabajos en eventos (Capítulos de memoria) - Completo',\
'Capítulos de memoria',\
'Capítulos de memoria');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
3,\
'Producción técnica - Presentación de trabajo - Comunicación',\
'Presentación de trabajo',\
'Trabajo de Comunicación');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
4,\
'Demás trabajos - Demás trabajos - Póster',\
'Demás trabajos',\
'Poster');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
5,\
'Producción técnica - Presentación de trabajo - Conferencia',\
'Presentación de trabajo',\
'Conferencia');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
6,\
'Producción técnica - Presentación de trabajo - Ponencia',\
'Presentación de trabajo',\
'Ponencia');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
7,\
'Estrategias pedagógicas para el fomento a la CTI',\
'Estrategias pedagógicas',\
'Estrategias pedagógicas');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
8,\
'Producción bibliográfica - Artículo - Publicado en revista especializada',\
'Publicado en revista especializada',\
'Artículo');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
9,\
'Producción bibliográfica - Artículo - Corto (Resumen)',\
'Corto (Resumen)',\
'Artículo');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
10,\
'Estrategias pedagógicas para el fomento a la CTI',\
'Estrategias pedagógicas',\
'Estrategias pedagógicas');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
11,\
'Producción bibliográfica - Artículo - Caso clínico',\
'Caso Clínico',\
'Artículo');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
12,\
'Producción bibliográfica - Trabajos en eventos (Capítulos de memoria) - Resumen',\
'Capítulo de Memoria',\
'Resumen');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
13,\
'Producción técnica - Presentación de trabajo - Congreso',\
'Congreso',\
'Congreso');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
14,\
'Producción técnica - Presentación de trabajo - Simposio',\
'Simposio',\
'Simposio');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
15,\
'Producción técnica - Presentación de trabajo - Seminario',\
'Seminario',\
'Seminario');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
16,\
'Producción técnica - Presentación de trabajo - Otro',\
'Otro',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
17,\
'Producción bibliográfica - Libro - Libro resultado de investigación',\
'Libro resultado de investigación',\
'Libro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
18,\
'Producción bibliográfica - Libro - Otro libro publicado',\
'Otro libro publicado',\
'Libro - Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
19,\
'Producción bibliográfica - Libro - Libro pedagógico y/o de divulgación',\
'Libro pedagógico y/o de divulgación',\
'Libro - pedagógico');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
20,\
'Otro capítulo de libro publicado',\
'Otro capítulo de libro',\
'Capítulo de libro - Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
21,\
'Capítulo de libro',\
'Capítulo de libro',\
'Capítulo de libro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
22,\
'Producción bibliográfica - Otro artículo publicado - Periódico de noticias',\
'Periódico de noticias',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
23,\
'Producción bibliográfica - Otro artículo publicado - Revista de divulgación',\
'Revista de divulgación',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
24,\
'Producción bibliográfica - Otro artículo publicado - Cartas al editor',\
'Cartas al editor',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
25,\
'Producción bibliográfica - Otro artículo publicado - Reseñas de libros',\
'Reseñas de libros',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
26,\
'Producción bibliográfica - Otro artículo publicado - Columna de opinión',\
'Columnas de opinión',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
27,\
'Producción bibliográfica - Documento de trabajo (Working Paper)',\
'Documento de trabajo (Working Paper)',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
28,\
'Producción bibliográfica - Traducciones - Artículo',\
'Traducciones - Artículo',\
'Traducciones');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
29,\
'Producción bibliográfica - Traducciones - Libro',\
'Traducciones - Libro',\
'Traducciones');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
30,\
'Producción bibliográfica - Traducciones - Otra',\
'Traducciones - Otra',\
'Traducciones');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
31,\
'Producción bibliográfica - Otra producción bibliográfica - Introducción',\
'Introducción',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
32,\
'Producción bibliográfica - Otra producción bibliográfica - Prólogo',\
'Prólogo',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
33,\
'Producción bibliográfica - Otra producción bibliográfica - Epílogo',\
'Epílogo',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
34,\
'Producción bibliográfica - Otra producción bibliográfica - Otra',\
'Otra',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
35,\
'Producción técnica - Softwares - Computacional',\
'Software',\
'Software');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
36,\
'Producción técnica - Productos tecnológicos - Gen Clonado',\
'Productos tecnológicos - Gen Clonado',\
'Productos tecnológicos');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
37,\
'Producción técnica - Productos tecnológicos - Coleccion biologica de referencia con informacion sistematizada',\
'Productos tecnológicos - Coleccion biologica de referencia con informacion sistematizada',\
'Productos tecnológicos');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
38,\
'Producción técnica - Productos tecnológicos - Otro',\
'Productos tecnológicos - Otro',\
'Productos tecnológicos');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
39,\
'Producción técnica - Productos tecnológicos - Base de datos de referencia para investigación',\
'Productos tecnológicos - Base de datos de referencia para investigación',\
'Productos tecnológicos');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
40,\
'Producción técnica - Diseño Industrial',\
'Diseño Industrial',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
41,\
'Producción técnica - Esquema de circuito integrado',\
'Esquema de circuito integrado',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
42,\
'Producción técnica - Innovaciones generadas de producción empresarial - Organizacional',\
'Innovaciones generadas de producción empresarial - Organizacional',\
'Innovaciones');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
43,\
'Producción técnica - Innovaciones generadas de producción empresarial - Empresarial',\
'Innovaciones generadas de producción empresarial - Empresarial',\
'Innovaciones');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
44,\
'Producción técnica - Variedad animal',\
'Variedad animal',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
45,\
'Producción técnica - Innovación de proceso o procedimiento',\
'Innovación de proceso o procedimiento',\
'Innovación');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
46,\
'Producción técnica - Cartas, mapas o similares - Aerofotograma',\
'Aerofotograma',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
47,\
'Producción técnica - Cartas, mapas o similares - Carta',\
'Carta',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
48,\
'Producción técnica - Cartas, mapas o similares - Fotograma',\
'Fotograma',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
49,\
'Producción técnica - Cartas, mapas o similares - Mapa',\
'Mapa',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
50,\
'Producción técnica - Cartas, mapas o similares - Otra',\
'Otra',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
51,\
'Producción técnica - Variedad vegetal',\
'Variedad vegetal',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
52,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Servicios de proyectos de IDI',\
'Servicios de proyectos de IDI',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
53,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Comercialización de tecnología',\
'Comercialización de tecnología',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
54,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Análisis de competitividad',\
'Análisis de competitividad',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
55,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Informe técnico',\
'Informe técnico',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
56,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Otro',\
'Otro',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
57,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Acciones de transferencia tecnológica',\
'Acciones de transferencia tecnológica',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
58,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Desarrollo de productos',\
'Desarrollo de productos',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
59,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Implementación de sistemas de análisis',\
'Implementación de sistemas de análisis',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
60,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Consultoría en artes,arquitectura y diseño',\
'Consultoría en artes,arquitectura y diseño',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
61,\
'Producción técnica - Regulación, norma, reglamento o legislación - Ambiental o de Salud',\
'Regulación, norma, reglamento o legislación - Ambiental o de Salud',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
62,\
'Producción técnica - Regulación, norma, reglamento o legislación - Educativa',\
'Regulación, norma, reglamento o legislación - Educativa',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
63,\
'Producción técnica - Regulación, norma, reglamento o legislación - Social',\
'Regulación, norma, reglamento o legislación - Social',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
64,\
'Producción técnica - Regulación, norma, reglamento o legislación - Técnica',\
'Regulación, norma, reglamento o legislación - Técnica',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
65,\
'Producción técnica - Regulación, norma, reglamento o legislación - Guía de práctica clínica',\
'Regulación, norma, reglamento o legislación - Guía de práctica clínica',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
66,\
'Producción técnica - Regulación, norma, reglamento o legislación - Proyecto de ley',\
'Regulación, norma, reglamento o legislación - Proyecto de ley',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
67,\
'Producción técnica - Reglamento Técnico',\
'Reglamento Técnico',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
68,\
'Producción técnica - Empresa de base tecnológica - Spin-off',\
'Empresa de base tecnológica - Spin-off',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
69,\
'Producción técnica - Empresa de base tecnológica - Start-up',\
'Empresa de base tecnológica - Start-up',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
70,\
'Demás trabajos - Demás trabajos',\
'Demás trabajos',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
71,\
'Producción técnica - Signos',\
'Signos',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
72,\
'Producción técnica - Softwares - Multimedia',\
'Multimedia',\
'Software');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
73,\
'Producción técnica - Softwares - Otra',\
'Softwares - Otra',\
'Software');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
74,\
'Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Básica',\
'Técnica - Básica',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
75,\
'Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Ensayo',\
'Técnica - Ensayo',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
76,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Servicios de Proyectos de I+D+I',\
'Servicios de Proyectos de I+D+I',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
77,\
'Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Proceso',\
'Técnica - Proceso',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
78,\
'Datos complementarios - Participación en comités de evaluación - Profesor titular',\
'Participación en comités de evaluación - Profesor titular',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
79,\
'Datos complementarios - Participación en comités de evaluación - Concurso docente',\
'Participación en comités de evaluación - Concurso docente',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
80,\
'Datos complementarios - Participación en comités de evaluación - Jefe de cátedra',\
'articipación en comités de evaluación - Jefe de cátedra',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
81,\
'Datos complementarios - Participación en comités de evaluación - Evaluación de cursos',\
'Participación en comités de evaluación - Evaluación de cursos',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
82,\
'Datos complementarios - Participación en comités de evaluación - Acreditación de programas',\
'Participación en comités de evaluación - Acreditación de programas',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
83,\
'Datos complementarios - Participación en comités de evaluación - Asignación de becas',\
'Participación en comités de evaluación - Asignación de becas',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
84,\
'Datos complementarios - Participación en comités de evaluación - Otra',\
'Participación en comités de evaluación - Otra',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
85,\
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Pregrado',\
'Jurado Pregrado',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
86,\
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Especialización',\
'Jurado Especialización',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
87,\
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Especialidad Médica',\
'Jurado Especialidad Médica',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
88,\
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Maestría',\
'Jurado Maestría',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
89,\
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Doctorado',\
'Jurado Doctorado',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
90, \
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Otra',\
'Jurado Otra',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
92, \
'Producción técnica - Prototipo - Servicios',\
'Prototipo - Servicios',\
'Servicios');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
93, \
'Producción técnica - Plantas piloto - Planta piloto',\
'Plantas piloto - Planta piloto',\
'Planta piloto');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
94, \
'Producción técnica - Prototipo - Industrial',\
'Prototipo - Industrial',\
'Industrial');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
95, \
'Producción técnica - Signos Distintivos - Marcas',\
'Signos Distintivos - Marcas',\
'Marcas');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
96, \
'Producción técnica - Signos Distintivos - Nombres comerciales',\
'Signos Distintivos - Nombres comerciales',\
'Nombres comerciales');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
97, \
'Apropiación - Eventos Cientificos - Otro',\
'Eventos Cientificos -  Otro',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
98, \
'Apropiación - Eventos Cientificos - Taller',\
'Eventos Cientificos -  Taller',\
'Taller');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
99, \
'Apropiación - Eventos Cientificos - Congreso',\
'Eventos Cientificos -  Congreso',\
'Congreso');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
100, \
'Apropiación - Eventos Cientificos - Encuentro',\
'Eventos Cientificos -  Encuentro',\
'Encuentro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
101, \
'Apropiación - Eventos Cientificos - Seminario',\
'Eventos Cientificos -  Seminario',\
'Seminario');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
102, \
'Apropiación - Eventos Cientificos - Simposio',\
'Eventos Cientificos -  Simposio',\
'Simposio');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
103, \
'Apropiación - Eventos Cientificos - Informes de investigación',\
'Eventos Cientificos -  Informes de investigación',\
'Informes de investigación');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
104, \
'Apropiación - Impresos - Manual',\
'Impresos - Manual',\
'Manual');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
105, \
'Apropiación - Impresos - Boletín',\
'Impresos - Boletín',\
'Boletín');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
106, \
'Apropiación - Contenido Multimedia - Comentario',\
'Contenido Multimedia - Comentario',\
'Comentario');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
107, \
'Apropiación - Contenido Multimedia - Entrevista',\
'Contenido Multimedia - Entrevista',\
'Entrevista');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
108, \
'Apropiación - Contenido Virtual - Página Web',\
'Contenido Virtual - Página Web',\
'Página Web');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
109, \
'Apropiación - Estrategias de Comunicación - Estrategias de Comunicación',\
'Estrategias de Comunicación - Estrategias de Comunicación',\
'Estrategias de Comunicación');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
110, \
'Apropiación - Estrategias Pedagógicas - Estrategias Pedagógicas para el fomento a la CTI',\
'Estrategias Pedagógicas - Estrategias Pedagógicas para el fomento a la CTI',\
'Estrategias Pedagógicas para el fomento a la CTI');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
111, \
'Apropiación - Participación Ciudadana - Participación Ciudadana en Proyectos de CTI',\
'Participación Ciudadana - Participación Ciudadana en Proyectos de CTI',\
'Participación Ciudadana en Proyectos de CTI');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
112, \
'Apropiación - Participación Ciudadana - Espacios de Participación Ciudadana',\
'Participación Ciudadana - Espacios de Participación Ciudadana',\
'Espacios de Participación Ciudadana');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
113, \
'Producción en arte, arquitectura y diseño - Obras o productos - Obras o productos',\
'Obras o productos - Obras o productos',\
'Obras o productos');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
114, \
'Actividades de Formación - Actividades de Formación - Asesorías al Programa Ondas',\
'Actividades de Formación - Asesorías al Programa Ondas',\
'Asesorías al Programa Ondas');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
115, \
'Actividades de Formación - Curso de Corta Duración Dictados - Perfeccionamiento',\
'Curso de Corta Duración Dictados - Perfeccionamiento',\
'Perfeccionamiento');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
116, \
'Actividades de Formación - Curso de Corta Duración Dictados - Extensión Extracurricular',\
'Curso de Corta Duración Dictados - Extensión Extracurricular',\
'Extensión Extracurricular');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
117, \
'Actividades de Formación - Trabajos dirigidos/turorías - Monografía de conclusión de curso',\
'Trabajos dirigidos/turorías - Monografía de conclusión de curso',\
'Monografía de conclusión de curso');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
118, \
'Actividades de Formación - Curso de Corta Duración Dictados - Otro',\
'Curso de Corta Duración Dictados - Otro',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
119, \
'Proyectos - Investigación, desarrollo e innovación - Proyectos',\
'Investigación, desarrollo e innovación - Proyectos',\
'Proyectos');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
120, \
'Apropiación social y circularción del conocimiento - Revista',\
'Investigación, desarrollo e innovación - Revista',\
'Revista');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
121, \
'Apropiación social y circularción del conocimiento - Cartilla',\
'Contenidos Impresos - Cartilla',\
'Cartilla');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
122, \
'Actividades de Formación - Cursos de Corta Duración - Especialización',\
'Cursos de Corta Duración - Especialización',\
'Especialización');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
123, \
'Apropiación - Contenidos Multimedia - Otro',\
'Contenidos Multimedia - Otro',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
124, \
'Apropiación - Contenidos Virtuales - Blog',\
'Contenidos Virtuales - Blog',\
'Blog');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
125, \
'Apropiación - Contenidos Virtuales - Aplicativo',\
'Contenidos Virtuales - Aplicativo',\
'Aplicativo');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
91, \
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Curso de perfeccionamiento/especialización',\
'Jurado Especial',\
'Comités');\n"]

    inv_colciencias_tipo_evento = [ "REPLACE INTO `uapa_db`.`v_colciencias_tipo_evento` ( \
`cod_tipo_evento`,\
`tipo_evento_col`) VALUES (\
0,\
'Sin Información');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_evento` ( \
`cod_tipo_evento`,\
`tipo_evento_col`) VALUES (\
1,\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_evento` ( \
`cod_tipo_evento`,\
`tipo_evento_col`) VALUES (\
2,\
'Taller');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_evento` ( \
`cod_tipo_evento`,\
`tipo_evento_col`) VALUES (\
3,\
'Congreso');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_evento` ( \
`cod_tipo_evento`,\
`tipo_evento_col`) VALUES (\
4,\
'Encuentro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_evento` ( \
`cod_tipo_evento`,\
`tipo_evento_col`) VALUES (\
5,\
'Seminario');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_evento` ( \
`cod_tipo_evento`,\
`tipo_evento_col`) VALUES (\
6,\
'Simposio');\n"]

#     inrel_persona_colciencias = [ "SET unique_checks = 0;\n\
# SET foreign_key_checks = 0;\n"]
#
#     incolciencias_apropiacion = [ "SET unique_checks = 0;\n\
# SET foreign_key_checks = 0;\n"]
#
#     inrel_personas_producto_colciencias = [ "SET unique_checks = 0;\n\
# SET foreign_key_checks = 0;\n"]
#
#     incolciencias_prod_tecnica = [ "SET unique_checks = 0;\n\
# SET foreign_key_checks = 0;\n"]
#
#     incolciencias_prod_bibliografica = [ "SET unique_checks = 0;\n\
# SET foreign_key_checks = 0;\n"]
#
#     incolciencias_comites = [ "SET unique_checks = 0;\n\
# SET foreign_key_checks = 0;\n"]
#
#     incolciencias_reconocimientos = [ "SET unique_checks = 0;\n\
# SET foreign_key_checks = 0;\n"]

    inrel_persona_colciencias = []

    incolciencias_apropiacion = []

    inrel_personas_producto_colciencias = []

    incolciencias_prod_tecnica = []

    incolciencias_prod_bibliografica = []

    incolciencias_comites = []

    incolciencias_reconocimientos = []

    incolciencias_idiomas = []
