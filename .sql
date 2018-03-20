init.incolciencias_apropiacion.append("REPLACE INTO `uapa_db`.`v_colciencias_tipo_evento` (" \
+ "`cod_colciencias_apropiacion`,"\
+ "`cod_rh`,"\
+ "`cod_producto`,"\
+ "`fecha_ini`,"\
+ "`ano_ini`,"\
+ "`mes_ini`,"\
+ "`fecha_fin`,"\
+ "`ano_fin`,"\
+ "`mes_fin`) VALUES ( "\
+ str(RH) + str(COD_PRODUCTO) + ";"\
+ str(RH) + ";"\
+ str(COD_PRODUCTO) + ";"\
+ "'" + FechaEventoini + "',"\
+ AnoEventoini + ","\
+ "'" + MesEventoini + "',"\
+ "'" + FechaEventofin + "',"\
+ AnoEventofin + ","\
+ "'" + MesEventofin + "');\n")
