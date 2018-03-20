init.incolciencias_prod_tecnica.append( \
"REPLACE INTO `uapa_db`.`colciencias_prod_tecnica`(`cod_colciencias_prod_tecnica`,`cod_rh`,`cod_producto`,`nombre_comercial`,`contrato/registro`,`titular`,`duracion`,`regulacion`,`tipo_regulacion`,`ciclo`,`estado_variedad`,`plataforma`,`ambiente`) VALUES"
+ "('" + str(RH) + str(COD_PRODUCTO) + "',"\
+ "('" + str(RH) + "',"\
+ str(COD_PRODUCTO) + ","\
+ "'" + re.sub(' +',' ',NombreComercial.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',Registro.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',Titular.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',Duracion.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',Regulacion.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',TipoRegulacion.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',Ciclo.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',Estado.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',Plataforma.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',Ambiente.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) \
+ ");\n")
+ "null" + ","\


init.incolciencias_prod_tecnica.append( \
"REPLACE INTO `uapa_db`.`colciencias_prod_tecnica`(`cod_colciencias_prod_tecnica`,`cod_rh`,`cod_producto`,`nombre_comercial`,`contrato/registro`,`titular`,`duracion`,`regulacion`,`tipo_regulacion`,`ciclo`,`estado_variedad`,`plataforma`,`ambiente`) VALUES"
+ "('" + str(RH) + str(COD_PRODUCTO) + "',"\
+ "('" + str(RH) + "',"\
+ str(COD_PRODUCTO) + ","\
+ "null" + ","\
+ "'" + re.sub(' +',' ',Registro.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "'" + re.sub(' +',' ',Titular.replace('"',"").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")) + "',"\
+ "null" + ","\
+ "null" + ","\
+ "null" + ","\
+ "null" + ","\
+ "null" + ","\
+ "null" + ","\
+ ");\n")
