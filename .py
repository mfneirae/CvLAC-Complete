init.inrel_persona_producto_colciencias.append( \
"REPLACE INTO `uapa_db`.`rel_persona_producto_colciencias`(`cod_producto`,`cod_rh`,`cod_tipo_producto`,`nombre_producto`,`cod_tipo_evento`,`evento_asociado`,`datos_complementarios`,`lugar`,`ano`,`ambito`,`palabras_clave`,`areas`,`sectores`,`coautores`,`vincula_coautores`,`editorial`,`volumen`,`paginas`,`doi`,`finalidad`,`instituciones_asociadas`,`tipo_vinculacion_institucion`) VALUES"
+ "('" + str(RH) + "',"\
+ str(COD_PRODUCTO) + ","\
+ "0" + ";"\
+ "null" + ";"\
+ re.sub(' +',' ',TipoEvento.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ","\
+ "'" + re.sub(' +',' ',NombreEvento.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "null" + ","\
+ "'" + re.sub(' +',' ',LugarEvento.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ re.sub(' +',' ',AnoEventoini.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + ","\
+ "'" + re.sub(' +',' ',Ambito.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "null" + ","\
+ "null" + ","\
+ "null" + ","\
+ "'" + re.sub(' +',' ',auto.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',vincula.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "null" + ","\
+ "null" + ","\
+ "null" + ","\
+ "null" + ","\
+ "null" + ","\
+ "'" + re.sub(' +',' ',insti.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',vinculain.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "\n")
