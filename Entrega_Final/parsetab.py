
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMASMENOSleftMULTIPLICACIONDIVISIONleftPOTENCIArightUMENOSA ARREGLO CADENA COMA COMENTARIO DIF DIVISION DPAREN ENTERO ENTONCES FIN FINFUNC FINSI FLOTANTE FUNC IGUAL II IMPRIMIR IPAREN LINEA LIST MAI MAQ MAS MEI MENOS MEQ MULTIPLICACION NEW PALABRA PARA POTENCIA REGRESAR SI SIG VARprograma : programa declaracion\n               | declaracionprograma : errordeclaracion : instruccion LINEAdeclaracion : LINEAdeclaracion : error LINEAinstruccion : VAR variable IGUAL exprinstruccion : VAR variable IGUAL errorinstruccion : IMPRIMIR IPAREN plista DPARENinstruccion : IMPRIMIR errorinstruccion : IMPRIMIRinstruccion : SI IPAREN comparacion DPAREN ENTONCES ENTERO\n                    | SI IPAREN comparacion DPAREN ENTONCES LINEA programa FINSIinstruccion : SI error ENTONCES ENTEROinstruccion : SI comparacion ENTONCES errorinstruccion : PARA PALABRA IGUAL expr A expr optstepinstruccion : PARA PALABRA IGUAL error A expr optstepinstruccion : PARA PALABRA IGUAL expr A error optstepinstruccion : PARA PALABRA IGUAL expr A expr erroroptstep : expr\n               | vacioinstruccion : SIG PALABRAinstruccion : SIG errorinstruccion : FINinstruccion : COMENTARIOinstruccion : FUNC PALABRA IPAREN PALABRA DPAREN IGUAL expr\n                    | FUNC PALABRA IPAREN PALABRA DPAREN LINEA programa FINFUNCinstruccion : FUNC PALABRA IPAREN PALABRA DPAREN IGUAL errorinstruccion : FUNC PALABRA IPAREN error DPAREN IGUAL exprinstruccion : REGRESARinstruccion : ARREGLO arreglolistainstruccion : ARREGLO errorarreglolista : arreglolista COMA elementoarreglo\n               | elementoarregloelementoarreglo : PALABRA IPAREN ENTERO DPARENelementoarreglo : PALABRA IPAREN ENTERO COMA ENTERO DPARENexpr : expr MAS expr\n            | expr MENOS expr\n            | expr MULTIPLICACION expr\n            | expr DIVISION expr\n            | expr POTENCIA exprexpr : ENTERO\n            | FLOTANTEexpr : variableexpr : IPAREN expr DPARENexpr : MENOS expr %prec UMENOScomparacion : expr MEQ expr\n               | expr MEI expr\n               | expr MAQ expr\n               | expr MAI expr\n               | expr II expr\n               | expr IGUAL expr\n               | expr DIF exprvariable : PALABRA\n              | PALABRA IPAREN expr DPAREN\n              | PALABRA IPAREN expr COMA expr DPARENnumero  : ENTERO\n               | FLOTANTEnumero  : MENOS ENTERO\n               | MENOS FLOTANTEplista   : plista COMA pelemento\n               | pelementopelemento : CADENApelemento : CADENA exprpelemento : exprvacio : '
    
_lr_action_items = {'error':([0,1,2,3,5,7,8,10,15,16,18,19,21,26,30,31,40,49,63,64,65,76,86,87,88,89,90,97,101,109,110,113,114,117,118,128,132,],[3,17,-2,-3,-5,23,27,34,37,-1,-6,-4,-54,-42,-43,-44,69,77,-46,92,94,-45,-37,-38,-39,-40,-41,-55,111,3,121,127,3,-56,17,17,-38,]),'LINEA':([0,1,2,3,4,5,7,11,12,14,16,17,18,19,21,23,26,30,31,33,34,36,37,38,63,68,69,72,76,77,78,86,87,88,89,90,95,97,100,103,105,108,109,110,111,112,114,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,133,],[5,5,-2,18,19,-5,-11,-24,-25,-30,-1,18,-6,-4,-54,-10,-42,-43,-44,-22,-23,-31,-32,-34,-46,-7,-8,-9,-45,-15,-14,-37,-38,-39,-40,-41,-33,-55,109,114,-35,-12,5,-66,-66,-66,5,-56,5,-20,-16,-19,-21,-18,-17,-26,-28,5,-29,-36,-13,-38,-27,]),'VAR':([0,1,2,3,5,16,18,19,109,114,118,128,],[6,6,-2,-3,-5,-1,-6,-4,6,6,6,6,]),'IMPRIMIR':([0,1,2,3,5,16,18,19,109,114,118,128,],[7,7,-2,-3,-5,-1,-6,-4,7,7,7,7,]),'SI':([0,1,2,3,5,16,18,19,109,114,118,128,],[8,8,-2,-3,-5,-1,-6,-4,8,8,8,8,]),'PARA':([0,1,2,3,5,16,18,19,109,114,118,128,],[9,9,-2,-3,-5,-1,-6,-4,9,9,9,9,]),'SIG':([0,1,2,3,5,16,18,19,109,114,118,128,],[10,10,-2,-3,-5,-1,-6,-4,10,10,10,10,]),'FIN':([0,1,2,3,5,16,18,19,109,114,118,128,],[11,11,-2,-3,-5,-1,-6,-4,11,11,11,11,]),'COMENTARIO':([0,1,2,3,5,16,18,19,109,114,118,128,],[12,12,-2,-3,-5,-1,-6,-4,12,12,12,12,]),'FUNC':([0,1,2,3,5,16,18,19,109,114,118,128,],[13,13,-2,-3,-5,-1,-6,-4,13,13,13,13,]),'REGRESAR':([0,1,2,3,5,16,18,19,109,114,118,128,],[14,14,-2,-3,-5,-1,-6,-4,14,14,14,14,]),'ARREGLO':([0,1,2,3,5,16,18,19,109,114,118,128,],[15,15,-2,-3,-5,-1,-6,-4,15,15,15,15,]),'$end':([1,2,3,5,16,18,19,],[0,-2,-3,-5,-1,-6,-4,]),'FINSI':([2,3,5,16,18,19,118,],[-2,-3,-5,-1,-6,-4,131,]),'FINFUNC':([2,3,5,16,18,19,128,],[-2,-3,-5,-1,-6,-4,133,]),'PALABRA':([6,8,9,10,13,15,21,22,24,26,29,30,31,40,41,42,45,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,73,76,86,87,88,89,90,97,98,101,102,110,111,112,113,115,117,122,132,],[21,21,32,33,35,39,-54,21,21,-42,21,-43,-44,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-46,21,93,39,21,-45,-37,-38,-39,-40,-41,-55,21,21,21,21,21,21,21,21,-56,21,-38,]),'IPAREN':([7,8,21,22,24,26,29,30,31,35,39,40,41,42,45,51,52,53,54,55,56,57,58,59,60,61,62,63,64,73,76,86,87,88,89,90,97,98,101,102,110,111,112,113,115,117,122,132,],[22,24,41,42,42,-42,42,-43,-44,65,67,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-46,42,42,-45,-37,-38,-39,-40,-41,-55,42,42,42,42,42,42,42,42,-56,42,-38,]),'ENTERO':([8,21,22,24,26,29,30,31,40,41,42,45,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,67,73,76,86,87,88,89,90,97,98,100,101,102,106,110,111,112,113,115,117,122,132,],[26,-54,26,26,-42,26,-43,-44,26,26,26,26,78,26,26,26,26,26,26,26,26,26,26,26,26,-46,26,96,26,-45,-37,-38,-39,-40,-41,-55,26,108,26,26,116,26,26,26,26,26,-56,26,-38,]),'FLOTANTE':([8,21,22,24,26,29,30,31,40,41,42,45,51,52,53,54,55,56,57,58,59,60,61,62,63,64,73,76,86,87,88,89,90,97,98,101,102,110,111,112,113,115,117,122,132,],[30,-54,30,30,-42,30,-43,-44,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-46,30,30,-45,-37,-38,-39,-40,-41,-55,30,30,30,30,30,30,30,30,-56,30,-38,]),'MENOS':([8,21,22,24,26,28,29,30,31,40,41,42,45,46,48,51,52,53,54,55,56,57,58,59,60,61,62,63,64,68,70,71,73,74,76,79,80,81,82,83,84,85,86,87,88,89,90,91,97,98,101,102,107,110,111,112,113,115,117,119,122,126,129,132,],[29,-54,29,29,-42,59,29,-43,-44,29,29,29,29,59,59,29,29,29,29,29,29,29,29,29,29,29,29,-46,29,59,59,59,29,59,-45,59,59,59,59,59,59,59,-37,-38,-39,-40,-41,59,-55,29,29,29,59,122,29,122,29,29,-56,59,29,59,59,-38,]),'IGUAL':([20,21,26,28,30,31,32,48,63,76,86,87,88,89,90,97,103,104,117,],[40,-54,-42,56,-43,-44,64,56,-46,-45,-37,-38,-39,-40,-41,-55,113,115,-56,]),'MEQ':([21,26,28,30,31,48,63,76,86,87,88,89,90,97,117,],[-54,-42,51,-43,-44,51,-46,-45,-37,-38,-39,-40,-41,-55,-56,]),'MEI':([21,26,28,30,31,48,63,76,86,87,88,89,90,97,117,],[-54,-42,52,-43,-44,52,-46,-45,-37,-38,-39,-40,-41,-55,-56,]),'MAQ':([21,26,28,30,31,48,63,76,86,87,88,89,90,97,117,],[-54,-42,53,-43,-44,53,-46,-45,-37,-38,-39,-40,-41,-55,-56,]),'MAI':([21,26,28,30,31,48,63,76,86,87,88,89,90,97,117,],[-54,-42,54,-43,-44,54,-46,-45,-37,-38,-39,-40,-41,-55,-56,]),'II':([21,26,28,30,31,48,63,76,86,87,88,89,90,97,117,],[-54,-42,55,-43,-44,55,-46,-45,-37,-38,-39,-40,-41,-55,-56,]),'DIF':([21,26,28,30,31,48,63,76,86,87,88,89,90,97,117,],[-54,-42,57,-43,-44,57,-46,-45,-37,-38,-39,-40,-41,-55,-56,]),'MAS':([21,26,28,30,31,46,48,63,68,70,71,74,76,79,80,81,82,83,84,85,86,87,88,89,90,91,97,107,110,112,117,119,126,129,132,],[-54,-42,58,-43,-44,58,58,-46,58,58,58,58,-45,58,58,58,58,58,58,58,-37,-38,-39,-40,-41,58,-55,58,58,58,-56,58,58,58,-38,]),'MULTIPLICACION':([21,26,28,30,31,46,48,63,68,70,71,74,76,79,80,81,82,83,84,85,86,87,88,89,90,91,97,107,110,112,117,119,126,129,132,],[-54,-42,60,-43,-44,60,60,-46,60,60,60,60,-45,60,60,60,60,60,60,60,60,60,-39,-40,-41,60,-55,60,60,60,-56,60,60,60,60,]),'DIVISION':([21,26,28,30,31,46,48,63,68,70,71,74,76,79,80,81,82,83,84,85,86,87,88,89,90,91,97,107,110,112,117,119,126,129,132,],[-54,-42,61,-43,-44,61,61,-46,61,61,61,61,-45,61,61,61,61,61,61,61,61,61,-39,-40,-41,61,-55,61,61,61,-56,61,61,61,61,]),'POTENCIA':([21,26,28,30,31,46,48,63,68,70,71,74,76,79,80,81,82,83,84,85,86,87,88,89,90,91,97,107,110,112,117,119,126,129,132,],[-54,-42,62,-43,-44,62,62,-46,62,62,62,62,-45,62,62,62,62,62,62,62,62,62,62,62,-41,62,-55,62,62,62,-56,62,62,62,62,]),'DPAREN':([21,26,30,31,43,44,45,46,47,48,63,70,71,74,76,79,80,81,82,83,84,85,86,87,88,89,90,93,94,96,97,99,107,116,117,],[-54,-42,-43,-44,72,-62,-63,-65,75,76,-46,97,76,-64,-45,-47,-48,-49,-50,-51,-52,-53,-37,-38,-39,-40,-41,103,104,105,-55,-61,117,130,-56,]),'COMA':([21,26,30,31,36,38,43,44,45,46,63,70,74,76,86,87,88,89,90,95,96,97,99,105,117,130,],[-54,-42,-43,-44,66,-34,73,-62,-63,-65,-46,98,-64,-45,-37,-38,-39,-40,-41,-33,106,-55,-61,-35,-56,-36,]),'ENTONCES':([21,25,26,27,30,31,63,75,76,79,80,81,82,83,84,85,86,87,88,89,90,97,117,],[-54,49,-42,50,-43,-44,-46,100,-45,-47,-48,-49,-50,-51,-52,-53,-37,-38,-39,-40,-41,-55,-56,]),'A':([21,26,30,31,63,76,86,87,88,89,90,91,92,97,117,],[-54,-42,-43,-44,-46,-45,-37,-38,-39,-40,-41,101,102,-55,-56,]),'CADENA':([22,73,],[45,45,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,109,114,],[1,118,128,]),'declaracion':([0,1,109,114,118,128,],[2,16,2,2,16,16,]),'instruccion':([0,1,109,114,118,128,],[4,4,4,4,4,4,]),'variable':([6,8,22,24,29,40,41,42,45,51,52,53,54,55,56,57,58,59,60,61,62,64,73,98,101,102,110,111,112,113,115,122,],[20,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'comparacion':([8,24,],[25,47,]),'expr':([8,22,24,29,40,41,42,45,51,52,53,54,55,56,57,58,59,60,61,62,64,73,98,101,102,110,111,112,113,115,122,],[28,46,48,63,68,70,71,74,79,80,81,82,83,84,85,86,87,88,89,90,91,46,107,110,112,119,119,119,126,129,132,]),'arreglolista':([15,],[36,]),'elementoarreglo':([15,66,],[38,95,]),'plista':([22,],[43,]),'pelemento':([22,73,],[44,99,]),'optstep':([110,111,112,],[120,124,125,]),'vacio':([110,111,112,],[123,123,123,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> programa declaracion','programa',2,'p_programa','Yacc.py',25),
  ('programa -> declaracion','programa',1,'p_programa','Yacc.py',26),
  ('programa -> error','programa',1,'p_programa_error','Yacc.py',43),
  ('declaracion -> instruccion LINEA','declaracion',2,'p_declaracion','Yacc.py',48),
  ('declaracion -> LINEA','declaracion',1,'p_declaracion_blanca','Yacc.py',59),
  ('declaracion -> error LINEA','declaracion',2,'p_declaracion_mala','Yacc.py',64),
  ('instruccion -> VAR variable IGUAL expr','instruccion',4,'p_instruccion_var','Yacc.py',71),
  ('instruccion -> VAR variable IGUAL error','instruccion',4,'p_instruccion_mal_var','Yacc.py',76),
  ('instruccion -> IMPRIMIR IPAREN plista DPAREN','instruccion',4,'p_instruccion_imprimir','Yacc.py',81),
  ('instruccion -> IMPRIMIR error','instruccion',2,'p_instruccion_imprimir_mal','Yacc.py',86),
  ('instruccion -> IMPRIMIR','instruccion',1,'p_instruccion_imprimir_vacio','Yacc.py',91),
  ('instruccion -> SI IPAREN comparacion DPAREN ENTONCES ENTERO','instruccion',6,'p_instruccion_si','Yacc.py',96),
  ('instruccion -> SI IPAREN comparacion DPAREN ENTONCES LINEA programa FINSI','instruccion',8,'p_instruccion_si','Yacc.py',97),
  ('instruccion -> SI error ENTONCES ENTERO','instruccion',4,'p_instruccion_si_mal','Yacc.py',104),
  ('instruccion -> SI comparacion ENTONCES error','instruccion',4,'p_instruccion_si_mal2','Yacc.py',109),
  ('instruccion -> PARA PALABRA IGUAL expr A expr optstep','instruccion',7,'p_instruccion_para','Yacc.py',114),
  ('instruccion -> PARA PALABRA IGUAL error A expr optstep','instruccion',7,'p_instruccion_para_mal_initial','Yacc.py',119),
  ('instruccion -> PARA PALABRA IGUAL expr A error optstep','instruccion',7,'p_instruccion_para_mal_final','Yacc.py',124),
  ('instruccion -> PARA PALABRA IGUAL expr A expr error','instruccion',7,'p_instruccion_para_mal_step','Yacc.py',129),
  ('optstep -> expr','optstep',1,'p_optstep','Yacc.py',133),
  ('optstep -> vacio','optstep',1,'p_optstep','Yacc.py',134),
  ('instruccion -> SIG PALABRA','instruccion',2,'p_instruccion_sig','Yacc.py',141),
  ('instruccion -> SIG error','instruccion',2,'p_instruccion_sig_mal','Yacc.py',147),
  ('instruccion -> FIN','instruccion',1,'p_instruccion_FIN','Yacc.py',152),
  ('instruccion -> COMENTARIO','instruccion',1,'p_instruccion_rem','Yacc.py',157),
  ('instruccion -> FUNC PALABRA IPAREN PALABRA DPAREN IGUAL expr','instruccion',7,'p_instruccion_def','Yacc.py',162),
  ('instruccion -> FUNC PALABRA IPAREN PALABRA DPAREN LINEA programa FINFUNC','instruccion',8,'p_instruccion_def','Yacc.py',163),
  ('instruccion -> FUNC PALABRA IPAREN PALABRA DPAREN IGUAL error','instruccion',7,'p_instruccion_def_mal_rhs','Yacc.py',168),
  ('instruccion -> FUNC PALABRA IPAREN error DPAREN IGUAL expr','instruccion',7,'p_instruccion_def_mal_arg','Yacc.py',173),
  ('instruccion -> REGRESAR','instruccion',1,'p_instruccion_regresar','Yacc.py',177),
  ('instruccion -> ARREGLO arreglolista','instruccion',2,'p_instruccion_arreglo','Yacc.py',181),
  ('instruccion -> ARREGLO error','instruccion',2,'p_instruccion_arreglo_mal','Yacc.py',186),
  ('arreglolista -> arreglolista COMA elementoarreglo','arreglolista',3,'p_arreglolista','Yacc.py',190),
  ('arreglolista -> elementoarreglo','arreglolista',1,'p_arreglolista','Yacc.py',191),
  ('elementoarreglo -> PALABRA IPAREN ENTERO DPAREN','elementoarreglo',4,'p_elementoarreglo_individual','Yacc.py',199),
  ('elementoarreglo -> PALABRA IPAREN ENTERO COMA ENTERO DPAREN','elementoarreglo',6,'p_elementoarreglo_doble','Yacc.py',204),
  ('expr -> expr MAS expr','expr',3,'p_expr_binaria','Yacc.py',208),
  ('expr -> expr MENOS expr','expr',3,'p_expr_binaria','Yacc.py',209),
  ('expr -> expr MULTIPLICACION expr','expr',3,'p_expr_binaria','Yacc.py',210),
  ('expr -> expr DIVISION expr','expr',3,'p_expr_binaria','Yacc.py',211),
  ('expr -> expr POTENCIA expr','expr',3,'p_expr_binaria','Yacc.py',212),
  ('expr -> ENTERO','expr',1,'p_expr_numero','Yacc.py',218),
  ('expr -> FLOTANTE','expr',1,'p_expr_numero','Yacc.py',219),
  ('expr -> variable','expr',1,'p_expr_variable','Yacc.py',224),
  ('expr -> IPAREN expr DPAREN','expr',3,'p_expr_groupo','Yacc.py',229),
  ('expr -> MENOS expr','expr',2,'p_expr_unario','Yacc.py',234),
  ('comparacion -> expr MEQ expr','comparacion',3,'p_comparacion','Yacc.py',238),
  ('comparacion -> expr MEI expr','comparacion',3,'p_comparacion','Yacc.py',239),
  ('comparacion -> expr MAQ expr','comparacion',3,'p_comparacion','Yacc.py',240),
  ('comparacion -> expr MAI expr','comparacion',3,'p_comparacion','Yacc.py',241),
  ('comparacion -> expr II expr','comparacion',3,'p_comparacion','Yacc.py',242),
  ('comparacion -> expr IGUAL expr','comparacion',3,'p_comparacion','Yacc.py',243),
  ('comparacion -> expr DIF expr','comparacion',3,'p_comparacion','Yacc.py',244),
  ('variable -> PALABRA','variable',1,'p_variable','Yacc.py',248),
  ('variable -> PALABRA IPAREN expr DPAREN','variable',4,'p_variable','Yacc.py',249),
  ('variable -> PALABRA IPAREN expr COMA expr DPAREN','variable',6,'p_variable','Yacc.py',250),
  ('numero -> ENTERO','numero',1,'p_numero','Yacc.py',259),
  ('numero -> FLOTANTE','numero',1,'p_numero','Yacc.py',260),
  ('numero -> MENOS ENTERO','numero',2,'p_numero_signo','Yacc.py',264),
  ('numero -> MENOS FLOTANTE','numero',2,'p_numero_signo','Yacc.py',265),
  ('plista -> plista COMA pelemento','plista',3,'p_plista','Yacc.py',269),
  ('plista -> pelemento','plista',1,'p_plista','Yacc.py',270),
  ('pelemento -> CADENA','pelemento',1,'p_elemento_cadena','Yacc.py',279),
  ('pelemento -> CADENA expr','pelemento',2,'p_elemento_CADENA_expr','Yacc.py',284),
  ('pelemento -> expr','pelemento',1,'p_elemento_expr','Yacc.py',289),
  ('vacio -> <empty>','vacio',0,'p_vacio','Yacc.py',293),
]
