
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMASMENOSleftMULTIPLICACIONDIVISIONleftPOTENCIArightUMENOSA ARREGLO CADENA COMA COMENTARIO COMILLA DIF DIVISION DPAREN ENTERO ENTONCES FIN FINFUNC FINSI FLOTANTE FUNC IGUAL II IMPRIMIR IPAREN LINEA MAI MAQ MAS MEI MENOS MEQ MULTIPLICACION PALABRA PARA POTENCIA SALTO SI SIG VARprograma : programa declaracion\n               | declaracionprograma : errordeclaracion : instruccion LINEAdeclaracion : LINEAdeclaracion : error LINEA\n                    | errorinstruccion : SALTO ENTEROinstruccion : VAR variable IGUAL expr\n                    | VAR variable IGUAL cadenacadena : CADENAinstruccion : IMPRIMIR IPAREN plista DPARENinstruccion : IMPRIMIRinstruccion : FINSIinstruccion : SI IPAREN comparacion DPAREN ENTONCES ENTERO\n                    | SI IPAREN comparacion DPAREN ENTONCESinstruccion : PARA PALABRA IGUAL expr A exprinstruccion : SIG PALABRAinstruccion : FINinstruccion : COMENTARIOinstruccion : FUNC PALABRA IPAREN PALABRA DPAREN IGUAL exprinstruccion : FUNC PALABRA IPAREN DPARENinstruccion : PALABRA IPAREN DPARENinstruccion : FINFUNC PALABRAinstruccion : ARREGLO arreglolistaarreglolista : arreglolista COMA elementoarreglo\n               | elementoarregloelementoarreglo : PALABRA IPAREN ENTERO DPARENelementoarreglo : PALABRA IPAREN ENTERO COMA ENTERO DPARENexpr : expr MAS expr\n            | expr MENOS expr\n            | expr MULTIPLICACION expr\n            | expr DIVISION expr\n            | expr POTENCIA exprexpr : ENTERO\n            | FLOTANTEexpr : variableexpr : IPAREN expr DPARENexpr : MENOS expr %prec UMENOScomparacion : expr MEQ expr\n               | expr MEI expr\n               | expr MAQ expr\n               | expr MAI expr\n               | expr II expr\n               | expr IGUAL expr\n               | expr DIF exprvariable : PALABRA\n              | PALABRA IPAREN expr DPAREN\n              | PALABRA IPAREN expr COMA expr DPARENplista   : plista COMA pelemento\n               | pelementopelemento : CADENApelemento : CADENA exprpelemento : expr'
    
_lr_action_items = {'error':([0,1,2,3,5,19,20,21,22,],[3,20,-2,-3,-5,-1,-7,-6,-4,]),'LINEA':([0,1,2,3,4,5,8,9,14,15,19,20,21,22,23,25,30,32,33,34,44,45,46,50,54,55,56,59,67,78,79,81,83,85,86,87,88,89,90,100,103,104,107,108,109,],[5,5,-2,21,22,-5,-13,-14,-19,-20,-1,21,-6,-4,-8,-47,-18,-24,-25,-27,-35,-36,-37,-23,-9,-10,-11,-12,-39,-22,-26,-48,-38,-30,-31,-32,-33,-34,-16,-28,-15,-17,-49,-21,-29,]),'SALTO':([0,1,2,3,5,19,20,21,22,],[6,6,-2,-3,-5,-1,-7,-6,-4,]),'VAR':([0,1,2,3,5,19,20,21,22,],[7,7,-2,-3,-5,-1,-7,-6,-4,]),'IMPRIMIR':([0,1,2,3,5,19,20,21,22,],[8,8,-2,-3,-5,-1,-7,-6,-4,]),'FINSI':([0,1,2,3,5,19,20,21,22,],[9,9,-2,-3,-5,-1,-7,-6,-4,]),'SI':([0,1,2,3,5,19,20,21,22,],[10,10,-2,-3,-5,-1,-7,-6,-4,]),'PARA':([0,1,2,3,5,19,20,21,22,],[11,11,-2,-3,-5,-1,-7,-6,-4,]),'SIG':([0,1,2,3,5,19,20,21,22,],[13,13,-2,-3,-5,-1,-7,-6,-4,]),'FIN':([0,1,2,3,5,19,20,21,22,],[14,14,-2,-3,-5,-1,-7,-6,-4,]),'COMENTARIO':([0,1,2,3,5,19,20,21,22,],[15,15,-2,-3,-5,-1,-7,-6,-4,]),'FUNC':([0,1,2,3,5,19,20,21,22,],[16,16,-2,-3,-5,-1,-7,-6,-4,]),'PALABRA':([0,1,2,3,5,7,11,13,16,17,18,19,20,21,22,26,27,36,37,38,41,43,49,51,52,60,62,63,64,65,66,69,70,71,72,73,74,75,82,98,105,],[12,12,-2,-3,-5,25,28,30,31,32,35,-1,-7,-6,-4,25,25,25,25,25,25,25,25,77,35,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'FINFUNC':([0,1,2,3,5,19,20,21,22,],[17,17,-2,-3,-5,-1,-7,-6,-4,]),'ARREGLO':([0,1,2,3,5,19,20,21,22,],[18,18,-2,-3,-5,-1,-7,-6,-4,]),'$end':([1,2,3,5,19,20,21,22,],[0,-2,-3,-5,-1,-7,-6,-4,]),'ENTERO':([6,26,27,36,37,38,41,43,49,53,60,62,63,64,65,66,69,70,71,72,73,74,75,82,90,98,101,105,],[23,44,44,44,44,44,44,44,44,80,44,44,44,44,44,44,44,44,44,44,44,44,44,44,103,44,106,44,]),'IPAREN':([8,10,12,25,26,27,31,35,36,37,38,41,43,49,60,62,63,64,65,66,69,70,71,72,73,74,75,82,98,105,],[26,27,29,37,38,38,51,53,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'IGUAL':([24,25,28,44,45,46,48,67,81,83,85,86,87,88,89,99,107,],[36,-47,49,-35,-36,-37,74,-39,-48,-38,-30,-31,-32,-33,-34,105,-49,]),'MAS':([25,42,44,45,46,48,54,57,58,61,67,76,81,83,85,86,87,88,89,91,92,93,94,95,96,97,102,104,107,108,],[-47,62,-35,-36,-37,62,62,62,62,62,-39,62,-48,-38,-30,-31,-32,-33,-34,62,62,62,62,62,62,62,62,62,-49,62,]),'MENOS':([25,26,27,36,37,38,41,42,43,44,45,46,48,49,54,57,58,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,76,81,82,83,85,86,87,88,89,91,92,93,94,95,96,97,98,102,104,105,107,108,],[-47,43,43,43,43,43,43,63,43,-35,-36,-37,63,43,63,63,63,43,63,43,43,43,43,43,-39,43,43,43,43,43,43,43,63,-48,43,-38,-30,-31,-32,-33,-34,63,63,63,63,63,63,63,43,63,63,43,-49,63,]),'MULTIPLICACION':([25,42,44,45,46,48,54,57,58,61,67,76,81,83,85,86,87,88,89,91,92,93,94,95,96,97,102,104,107,108,],[-47,64,-35,-36,-37,64,64,64,64,64,-39,64,-48,-38,64,64,-32,-33,-34,64,64,64,64,64,64,64,64,64,-49,64,]),'DIVISION':([25,42,44,45,46,48,54,57,58,61,67,76,81,83,85,86,87,88,89,91,92,93,94,95,96,97,102,104,107,108,],[-47,65,-35,-36,-37,65,65,65,65,65,-39,65,-48,-38,65,65,-32,-33,-34,65,65,65,65,65,65,65,65,65,-49,65,]),'POTENCIA':([25,42,44,45,46,48,54,57,58,61,67,76,81,83,85,86,87,88,89,91,92,93,94,95,96,97,102,104,107,108,],[-47,66,-35,-36,-37,66,66,66,66,66,-39,66,-48,-38,66,66,66,66,-34,66,66,66,66,66,66,66,66,66,-49,66,]),'DPAREN':([25,29,39,40,41,42,44,45,46,47,51,57,58,61,67,77,80,81,83,84,85,86,87,88,89,91,92,93,94,95,96,97,102,106,107,],[-47,50,59,-51,-52,-54,-35,-36,-37,68,78,81,83,-53,-39,99,100,-48,-38,-50,-30,-31,-32,-33,-34,-40,-41,-42,-43,-44,-45,-46,107,109,-49,]),'COMA':([25,33,34,39,40,41,42,44,45,46,57,61,67,79,80,81,83,84,85,86,87,88,89,100,107,109,],[-47,52,-27,60,-51,-52,-54,-35,-36,-37,82,-53,-39,-26,101,-48,-38,-50,-30,-31,-32,-33,-34,-28,-49,-29,]),'MEQ':([25,44,45,46,48,67,81,83,85,86,87,88,89,107,],[-47,-35,-36,-37,69,-39,-48,-38,-30,-31,-32,-33,-34,-49,]),'MEI':([25,44,45,46,48,67,81,83,85,86,87,88,89,107,],[-47,-35,-36,-37,70,-39,-48,-38,-30,-31,-32,-33,-34,-49,]),'MAQ':([25,44,45,46,48,67,81,83,85,86,87,88,89,107,],[-47,-35,-36,-37,71,-39,-48,-38,-30,-31,-32,-33,-34,-49,]),'MAI':([25,44,45,46,48,67,81,83,85,86,87,88,89,107,],[-47,-35,-36,-37,72,-39,-48,-38,-30,-31,-32,-33,-34,-49,]),'II':([25,44,45,46,48,67,81,83,85,86,87,88,89,107,],[-47,-35,-36,-37,73,-39,-48,-38,-30,-31,-32,-33,-34,-49,]),'DIF':([25,44,45,46,48,67,81,83,85,86,87,88,89,107,],[-47,-35,-36,-37,75,-39,-48,-38,-30,-31,-32,-33,-34,-49,]),'A':([25,44,45,46,67,76,81,83,85,86,87,88,89,107,],[-47,-35,-36,-37,-39,98,-48,-38,-30,-31,-32,-33,-34,-49,]),'CADENA':([26,36,60,],[41,56,41,]),'FLOTANTE':([26,27,36,37,38,41,43,49,60,62,63,64,65,66,69,70,71,72,73,74,75,82,98,105,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'ENTONCES':([68,],[90,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'declaracion':([0,1,],[2,19,]),'instruccion':([0,1,],[4,4,]),'variable':([7,26,27,36,37,38,41,43,49,60,62,63,64,65,66,69,70,71,72,73,74,75,82,98,105,],[24,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'arreglolista':([18,],[33,]),'elementoarreglo':([18,52,],[34,79,]),'plista':([26,],[39,]),'pelemento':([26,60,],[40,84,]),'expr':([26,27,36,37,38,41,43,49,60,62,63,64,65,66,69,70,71,72,73,74,75,82,98,105,],[42,48,54,57,58,61,67,76,42,85,86,87,88,89,91,92,93,94,95,96,97,102,104,108,]),'comparacion':([27,],[47,]),'cadena':([36,],[55,]),}

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
  ('declaracion -> error','declaracion',1,'p_declaracion_mala','Yacc.py',65),
  ('instruccion -> SALTO ENTERO','instruccion',2,'p_instruccion_salto','Yacc.py',72),
  ('instruccion -> VAR variable IGUAL expr','instruccion',4,'p_instruccion_var','Yacc.py',77),
  ('instruccion -> VAR variable IGUAL cadena','instruccion',4,'p_instruccion_var','Yacc.py',78),
  ('cadena -> CADENA','cadena',1,'p_cadena','Yacc.py',86),
  ('instruccion -> IMPRIMIR IPAREN plista DPAREN','instruccion',4,'p_instruccion_imprimir','Yacc.py',91),
  ('instruccion -> IMPRIMIR','instruccion',1,'p_instruccion_imprimir_vacio','Yacc.py',96),
  ('instruccion -> FINSI','instruccion',1,'p_instruccion_finsi','Yacc.py',101),
  ('instruccion -> SI IPAREN comparacion DPAREN ENTONCES ENTERO','instruccion',6,'p_instruccion_si','Yacc.py',106),
  ('instruccion -> SI IPAREN comparacion DPAREN ENTONCES','instruccion',5,'p_instruccion_si','Yacc.py',107),
  ('instruccion -> PARA PALABRA IGUAL expr A expr','instruccion',6,'p_instruccion_para','Yacc.py',114),
  ('instruccion -> SIG PALABRA','instruccion',2,'p_instruccion_sig','Yacc.py',118),
  ('instruccion -> FIN','instruccion',1,'p_instruccion_fin','Yacc.py',124),
  ('instruccion -> COMENTARIO','instruccion',1,'p_instruccion_comentario','Yacc.py',129),
  ('instruccion -> FUNC PALABRA IPAREN PALABRA DPAREN IGUAL expr','instruccion',7,'p_instruccion_func_expr','Yacc.py',133),
  ('instruccion -> FUNC PALABRA IPAREN DPAREN','instruccion',4,'p_instruccion_func','Yacc.py',138),
  ('instruccion -> PALABRA IPAREN DPAREN','instruccion',3,'p_instruccion_func_ir','Yacc.py',143),
  ('instruccion -> FINFUNC PALABRA','instruccion',2,'p_instruccion_func_fin','Yacc.py',147),
  ('instruccion -> ARREGLO arreglolista','instruccion',2,'p_instruccion_arreglo','Yacc.py',152),
  ('arreglolista -> arreglolista COMA elementoarreglo','arreglolista',3,'p_arreglolista','Yacc.py',157),
  ('arreglolista -> elementoarreglo','arreglolista',1,'p_arreglolista','Yacc.py',158),
  ('elementoarreglo -> PALABRA IPAREN ENTERO DPAREN','elementoarreglo',4,'p_elementoarreglo_individual','Yacc.py',166),
  ('elementoarreglo -> PALABRA IPAREN ENTERO COMA ENTERO DPAREN','elementoarreglo',6,'p_elementoarreglo_doble','Yacc.py',171),
  ('expr -> expr MAS expr','expr',3,'p_expr_binaria','Yacc.py',175),
  ('expr -> expr MENOS expr','expr',3,'p_expr_binaria','Yacc.py',176),
  ('expr -> expr MULTIPLICACION expr','expr',3,'p_expr_binaria','Yacc.py',177),
  ('expr -> expr DIVISION expr','expr',3,'p_expr_binaria','Yacc.py',178),
  ('expr -> expr POTENCIA expr','expr',3,'p_expr_binaria','Yacc.py',179),
  ('expr -> ENTERO','expr',1,'p_expr_numero','Yacc.py',185),
  ('expr -> FLOTANTE','expr',1,'p_expr_numero','Yacc.py',186),
  ('expr -> variable','expr',1,'p_expr_variable','Yacc.py',191),
  ('expr -> IPAREN expr DPAREN','expr',3,'p_expr_grupo','Yacc.py',196),
  ('expr -> MENOS expr','expr',2,'p_expr_unario','Yacc.py',201),
  ('comparacion -> expr MEQ expr','comparacion',3,'p_comparacion','Yacc.py',205),
  ('comparacion -> expr MEI expr','comparacion',3,'p_comparacion','Yacc.py',206),
  ('comparacion -> expr MAQ expr','comparacion',3,'p_comparacion','Yacc.py',207),
  ('comparacion -> expr MAI expr','comparacion',3,'p_comparacion','Yacc.py',208),
  ('comparacion -> expr II expr','comparacion',3,'p_comparacion','Yacc.py',209),
  ('comparacion -> expr IGUAL expr','comparacion',3,'p_comparacion','Yacc.py',210),
  ('comparacion -> expr DIF expr','comparacion',3,'p_comparacion','Yacc.py',211),
  ('variable -> PALABRA','variable',1,'p_variable','Yacc.py',215),
  ('variable -> PALABRA IPAREN expr DPAREN','variable',4,'p_variable','Yacc.py',216),
  ('variable -> PALABRA IPAREN expr COMA expr DPAREN','variable',6,'p_variable','Yacc.py',217),
  ('plista -> plista COMA pelemento','plista',3,'p_plista','Yacc.py',226),
  ('plista -> pelemento','plista',1,'p_plista','Yacc.py',227),
  ('pelemento -> CADENA','pelemento',1,'p_elemento_cadena','Yacc.py',236),
  ('pelemento -> CADENA expr','pelemento',2,'p_elemento_CADENA_expr','Yacc.py',241),
  ('pelemento -> expr','pelemento',1,'p_elemento_expr','Yacc.py',246),
]
