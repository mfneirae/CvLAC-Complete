init.inrel_personas_producto_colciencias.append( \
"REPLACE INTO `uapa_db`.`rel_personas_producto_colciencias`(`cod_producto`,`cod_rh`,`cod_tipo_producto`,`nombre_producto`,`cod_tipo_evento`,`evento_asociado`,`datos_complementarios`,`lugar`,`ano`,`ambito`,`palabras_clave`,`areas`,`sectores`,`coautores`,`vincula_coautores`,`editorial`,`volumen`,`paginas`,`doi`,`finalidad`,`instituciones_asociadas`,`tipo_vinculacion_institucion`) VALUES"
+ "('" + str(RH) + "',"\
+ str(COD_PRODUCTO) + ","\
+ re.sub(' +',' ',tipo.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ","\
+ "'" + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "0" + ","\
+ "null" + ","\
+ "null" + ","\
+ "'" + re.sub(' +',' ',lugar.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ re.sub(' +',' ',Anoptnorma.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ","\
+ "null" + ","\
+ "'" + re.sub(' +',' ',palabras.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',areas.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',sectores.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',coautores.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "null" + ","\
+ "'" + re.sub(' +',' ',Editorial.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',Volumen.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',Paginas.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',doi.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "null" + ","\
+ "'" + re.sub(' +',' ',Instituciones.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "null" + ");\n")

init.inrel_personas_producto_colciencias.append( \
"REPLACE INTO `uapa_db`.`rel_personas_producto_colciencias`(`cod_producto`,`cod_rh`,`cod_tipo_producto`,`nombre_producto`,`cod_tipo_evento`,`evento_asociado`,`datos_complementarios`,`lugar`,`ano`,`ambito`,`palabras_clave`,`areas`,`sectores`,`coautores`,`vincula_coautores`,`editorial`,`volumen`,`paginas`,`doi`,`finalidad`,`instituciones_asociadas`,`tipo_vinculacion_institucion`) VALUES"
+ "('" + str(RH) + "',"\
+ str(COD_PRODUCTO) + ","\
+ re.sub(' +',' ',tipo.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ","\
+ "'" + re.sub(' +',' ',NombreProducto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "0" + ","\
+ "null" + ","\
+ "'" + re.sub(' +',' ',Datos.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "null" + ","\
+ "null" + ","\
+ "null" + ","\
+ "'" + re.sub(' +',' ',palabras.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',areas.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',sectores.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',coautores.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "null" + ","\
+ "null" + ","\
+ "null" + ","\
+ "null" + ","\
+ "null" + ","\
+ "null" + ","\
+ "'" + re.sub(' +',' ',Instituciones.strip().replace('"',"").replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "null" + ");\n")
