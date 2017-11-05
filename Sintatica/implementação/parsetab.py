
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIGUALMAIORMENORMAIORIGUALMENORIGUALDIFERENTEleftSOMASUBRleftVEZESDIVIDEID VIRGULA ATRIBUICAO SOMA SUBR VEZES DIVIDE IGUAL MENOR MAIOR MENORIGUAL MAIORIGUAL ELOGICO OULOGICO NEGACAO DIFERENTE ABREPAR FECHAPAR DOISPONTOS ABRECOLCH FECHACOLCH ATE FLUTUANTE ENTAO REPITA ESCREVA SENAO RETORNA FIM LEIA SE INTEIRO\n\t\tprograma : lista_declaracoes\n\t\t\n\t\tlista_declaracoes : lista_declaracoes declaracao\n\t\t\t\t\t\t\t\t\t\n\t\t\n\t\tlista_declaracoes : declaracao\t\t\n\t\t\n\t\tdeclaracao : declaracao_variaveis\n\t\t\t\t\t| inicializacao_variaveis\n\t\t\t\t\t| declaracao_funcao\n\n\t\t\n\t\tdeclaracao_variaveis : tipo DOISPONTOS lista_variaveis\n\t\t\n\t\tinicializacao_variaveis : atribuicao\n\t\t\n\t\tlista_variaveis : lista_variaveis VIRGULA var\n\t\t\n\t\tlista_variaveis : var\n\t\t\n\t\tvar : ID\n\t    \n\t    var : ID indice\n\t    \n\t \tindice : indice ABRECOLCH expressao FECHACOLCH\n\t \t\n\t \tindice : ABRECOLCH expressao FECHACOLCH\n\t \ttipo : INTEIROtipo : FLUTUANTE\n\t \tdeclaracao_funcao : tipo cabecalho\n\t \t\n\t \tdeclaracao_funcao : cabecalho\n\t \t\n\t \tcabecalho : ID ABREPAR lista_parametros FECHAPAR corpo FIM\n\t \t\n\t \tlista_parametros : lista_parametros VIRGULA lista_parametros\n\t \t\n\t \tlista_parametros : parametro\n\t \t\t\t\t\t\t| vazio\n\t \t\n\t \tparametro : tipo DOISPONTOS ID\n\t \t\n \t\tparametro : parametro ABRECOLCH FECHACOLCH\n \t\t\n \t\tcorpo : corpo acao\n \t\t\n\t\tcorpo : vazio\n\t\t\n \t\tacao : expressao\n \t\t\t\t| declaracao_variaveis\n \t\t\t\t| se\n \t\t\t\t| repita\n \t\t\t\t| leia\n \t\t\t\t| escreva\n \t\t\t\t| retorna\n \t\t\t\t| error\n \t\t\n \t\tse : SE expressao ENTAO corpo FIM\n \t\t\n \t\tse : SE expressao ENTAO corpo SENAO corpo FIM\n \t\t\n \t\trepita : REPITA corpo ATE expressao\n \t\t\n \t\tatribuicao : var ATRIBUICAO expressao\n \t\t\n \t\tleia : LEIA ABREPAR ID FECHAPAR\n \t\t\n \t\tescreva : ESCREVA ABREPAR expressao FECHAPAR\n \t\t\n \t\tretorna : RETORNA ABREPAR expressao FECHAPAR\n \t\t\n \t\texpressao : expressao_simples\n \t\t\t\t\t| atribuicao\n \t\t\n \t\texpressao_simples : expressao_aditiva\n \t\t\n \t\texpressao_simples : expressao_simples operador_relacional expressao_aditiva\n \t\t\n \t\texpressao_aditiva : expressao_multiplicativa\n \t\t\n \t\texpressao_aditiva : expressao_aditiva operador_soma expressao_multiplicativa\n \t\t\n\t\texpressao_multiplicativa : expressao_unaria\n \t\t\n\t\texpressao_multiplicativa : expressao_multiplicativa operador_multiplicacao expressao_unaria\n\t \t\t\t\n\t\texpressao_unaria : fator\n\t\t\t\t\n\t\texpressao_unaria : operador_soma fator\n\t\t\n\t\toperador_relacional : MENOR\n\t\t\t\t\t\t\t| MAIOR\n\t\t\t\t\t\t\t| IGUAL\n\t\t\t\t\t\t\t| DIFERENTE\n\t\t\t\t\t\t\t| MENORIGUAL\n\t\t\t\t\t\t\t| MAIORIGUAL\n\t\t\t\t\t\t\t| ELOGICO\n\t\t\t\t\t\t\t| OULOGICO\n\t\t\t\t\t\t\t| NEGACAO\n\t\t\n\t\toperador_soma : SOMA\n\t\t\t\t\t\t| SUBR\n\t\t\n\t\toperador_multiplicacao : VEZES\n\t\t\t\t\t\t\t\t| DIVIDE\n\t\t\n\t\tfator : ABREPAR expressao FECHAPAR\n\t\t\n\t\tfator : var\n\t\t\t\t| chamada_funcao\n\t\t\t\t| numero\n\t\t\n\t\tnumero : INTEIRO\n\t\t\t\t| FLUTUANTE\n\t\t\n\t\tchamada_funcao : ID ABREPAR lista_argumentos FECHAPAR\n\t\t\n\t\tlista_argumentos : lista_argumentos VIRGULA expressao\n\t\t\n\t\tlista_argumentos : expressao\n\t\t\t\t\t\t| vazio\n\t\t\n        vazio :\n\t\t'
    
_lr_action_items = {'ATE':([20,22,23,24,25,29,30,31,32,33,35,36,37,38,39,40,41,59,60,67,73,74,75,76,80,81,83,88,90,91,92,94,95,96,97,98,100,102,103,104,109,118,119,120,121,124,126,],[-12,-7,-10,-11,-42,-38,-50,-70,-66,-48,-67,-68,-44,-11,-69,-43,-46,-51,-66,-14,-9,-45,-65,-47,-49,-13,-26,-71,-25,-75,-69,-27,-33,-70,-31,-28,-32,-30,-29,-34,114,-40,-37,-41,-39,-35,-36,]),'ESCREVA':([20,22,23,24,25,29,30,31,32,33,35,36,37,38,39,40,41,59,60,67,70,73,74,75,76,80,81,83,84,88,90,91,92,94,95,96,97,98,100,102,103,104,109,117,118,119,120,121,122,123,124,125,126,],[-12,-7,-10,-11,-42,-38,-50,-70,-66,-48,-67,-68,-44,-11,-69,-43,-46,-51,-66,-14,-75,-9,-45,-65,-47,-49,-13,-26,89,-71,-25,-75,-69,-27,-33,-70,-31,-28,-32,-30,-29,-34,89,-75,-40,-37,-41,-39,89,-75,-35,89,-36,]),'SOMA':([18,19,20,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,65,66,67,70,73,74,75,76,80,81,83,84,87,88,90,91,92,94,95,96,97,98,100,102,103,104,106,108,109,110,114,117,118,119,120,121,122,123,124,125,126,],[26,26,-12,-7,-10,-11,-42,-61,26,-38,-50,-70,-66,-48,-62,-67,-68,26,-11,-69,-43,-46,26,-57,-58,-53,-54,-55,-52,26,-59,-56,-60,-51,-66,26,26,26,-63,-64,-14,-75,-9,26,-65,-47,-49,-13,-26,26,26,-71,-25,-75,-69,-27,-33,-70,-31,-28,-32,-30,-29,-34,26,26,26,26,26,-75,-40,-37,-41,-39,26,-75,-35,26,-36,]),'IGUAL':([20,25,30,31,32,33,35,36,37,38,39,41,59,60,67,74,75,76,80,81,88,92,96,],[-12,52,-50,-70,-66,-48,-67,-68,-44,-11,-69,-46,-51,-66,-14,-45,-65,-47,-49,-13,-71,-69,-70,]),'ABRECOLCH':([11,20,24,38,46,67,81,85,86,],[19,43,19,19,72,-14,-13,-23,-24,]),'DIFERENTE':([20,25,30,31,32,33,35,36,37,38,39,41,59,60,67,74,75,76,80,81,88,92,96,],[-12,53,-50,-70,-66,-48,-67,-68,-44,-11,-69,-46,-51,-66,-14,-45,-65,-47,-49,-13,-71,-69,-70,]),'OULOGICO':([20,25,30,31,32,33,35,36,37,38,39,41,59,60,67,74,75,76,80,81,88,92,96,],[-12,56,-50,-70,-66,-48,-67,-68,-44,-11,-69,-46,-51,-66,-14,-45,-65,-47,-49,-13,-71,-69,-70,]),'FECHACOLCH':([20,25,29,30,31,32,33,35,36,37,38,39,40,41,42,59,60,67,68,72,74,75,76,80,81,88,],[-12,-42,-38,-50,-70,-66,-48,-67,-68,-44,-11,-69,-43,-46,67,-51,-66,-14,81,86,-45,-65,-47,-49,-13,-71,]),'VIRGULA':([20,21,22,23,24,25,29,30,31,32,33,35,36,37,38,39,40,41,44,46,47,59,60,63,67,69,73,74,75,76,77,78,79,80,81,82,85,86,88,107,],[-12,-75,48,-10,-11,-42,-38,-50,-70,-66,-48,-67,-68,-44,-11,-69,-43,-46,69,-21,-22,-51,-66,-75,-14,-75,-9,-45,-65,-47,87,-73,-74,-49,-13,69,-23,-24,-71,-72,]),'ATRIBUICAO':([6,11,20,32,38,67,81,],[18,-11,-12,18,-11,-14,-13,]),'ELOGICO':([20,25,30,31,32,33,35,36,37,38,39,41,59,60,67,74,75,76,80,81,88,92,96,],[-12,50,-50,-70,-66,-48,-67,-68,-44,-11,-69,-46,-51,-66,-14,-45,-65,-47,-49,-13,-71,-69,-70,]),'MAIOR':([20,25,30,31,32,33,35,36,37,38,39,41,59,60,67,74,75,76,80,81,88,92,96,],[-12,51,-50,-70,-66,-48,-67,-68,-44,-11,-69,-46,-51,-66,-14,-45,-65,-47,-49,-13,-71,-69,-70,]),'FLUTUANTE':([0,1,2,4,8,9,10,12,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,65,66,67,69,70,73,74,75,76,80,81,83,84,87,88,90,91,92,94,95,96,97,98,100,101,102,103,104,106,108,109,110,114,117,118,119,120,121,122,123,124,125,126,],[5,-5,-18,5,-6,-4,-3,-8,-17,-2,31,31,-12,5,-7,-10,-11,-42,-61,31,31,-38,-50,-70,-66,-48,-62,-67,-68,-44,-11,-69,-43,-46,31,-57,-58,-53,-54,-55,-52,31,-59,-56,-60,-51,-66,31,31,31,-63,-64,-14,5,-75,-9,-45,-65,-47,-49,-13,-26,96,31,-71,-25,-75,-69,-27,-33,-70,-31,-28,-32,-19,-30,-29,-34,31,31,96,31,31,-75,-40,-37,-41,-39,96,-75,-35,96,-36,]),'MENORIGUAL':([20,25,30,31,32,33,35,36,37,38,39,41,59,60,67,74,75,76,80,81,88,92,96,],[-12,57,-50,-70,-66,-48,-67,-68,-44,-11,-69,-46,-51,-66,-14,-45,-65,-47,-49,-13,-71,-69,-70,]),'FIM':([20,22,23,24,25,29,30,31,32,33,35,36,37,38,39,40,41,59,60,67,70,73,74,75,76,80,81,83,84,88,90,92,94,95,96,97,98,100,102,103,104,117,118,119,120,121,122,123,124,125,126,],[-12,-7,-10,-11,-42,-38,-50,-70,-66,-48,-67,-68,-44,-11,-69,-43,-46,-51,-66,-14,-75,-9,-45,-65,-47,-49,-13,-26,101,-71,-25,-69,-27,-33,-70,-31,-28,-32,-30,-29,-34,-75,-40,-37,-41,-39,124,-75,-35,126,-36,]),'$end':([1,2,4,8,9,10,12,13,15,17,20,22,23,24,25,29,30,31,32,33,35,36,37,38,39,40,41,59,60,67,73,74,75,76,80,81,88,101,],[-5,-18,-1,-6,-4,-3,-8,0,-17,-2,-12,-7,-10,-11,-42,-38,-50,-70,-66,-48,-67,-68,-44,-11,-69,-43,-46,-51,-66,-14,-9,-45,-65,-47,-49,-13,-71,-19,]),'SUBR':([18,19,20,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,65,66,67,70,73,74,75,76,80,81,83,84,87,88,90,91,92,94,95,96,97,98,100,102,103,104,106,108,109,110,114,117,118,119,120,121,122,123,124,125,126,],[34,34,-12,-7,-10,-11,-42,-61,34,-38,-50,-70,-66,-48,-62,-67,-68,34,-11,-69,-43,-46,34,-57,-58,-53,-54,-55,-52,34,-59,-56,-60,-51,-66,34,34,34,-63,-64,-14,-75,-9,34,-65,-47,-49,-13,-26,34,34,-71,-25,-75,-69,-27,-33,-70,-31,-28,-32,-30,-29,-34,34,34,34,34,34,-75,-40,-37,-41,-39,34,-75,-35,34,-36,]),'DIVIDE':([20,30,31,32,33,35,36,38,39,41,59,60,67,75,76,80,81,88,92,96,],[-12,-50,-70,-66,-48,-67,-68,-11,-69,66,-51,-66,-14,-65,66,-49,-13,-71,-69,-70,]),'ENTAO':([20,25,29,30,31,32,33,35,36,37,38,39,40,41,59,60,67,74,75,76,80,81,88,112,],[-12,-42,-38,-50,-70,-66,-48,-67,-68,-44,-11,-69,-43,-46,-51,-66,-14,-45,-65,-47,-49,-13,-71,117,]),'SENAO':([20,22,23,24,25,29,30,31,32,33,35,36,37,38,39,40,41,59,60,67,73,74,75,76,80,81,83,88,90,92,94,95,96,97,98,100,102,103,104,117,118,119,120,121,122,124,126,],[-12,-7,-10,-11,-42,-38,-50,-70,-66,-48,-67,-68,-44,-11,-69,-43,-46,-51,-66,-14,-9,-45,-65,-47,-49,-13,-26,-71,-25,-69,-27,-33,-70,-31,-28,-32,-30,-29,-34,-75,-40,-37,-41,-39,123,-35,-36,]),'REPITA':([20,22,23,24,25,29,30,31,32,33,35,36,37,38,39,40,41,59,60,67,70,73,74,75,76,80,81,83,84,88,90,91,92,94,95,96,97,98,100,102,103,104,109,117,118,119,120,121,122,123,124,125,126,],[-12,-7,-10,-11,-42,-38,-50,-70,-66,-48,-67,-68,-44,-11,-69,-43,-46,-51,-66,-14,-75,-9,-45,-65,-47,-49,-13,-26,91,-71,-25,-75,-69,-27,-33,-70,-31,-28,-32,-30,-29,-34,91,-75,-40,-37,-41,-39,91,-75,-35,91,-36,]),'RETORNA':([20,22,23,24,25,29,30,31,32,33,35,36,37,38,39,40,41,59,60,67,70,73,74,75,76,80,81,83,84,88,90,91,92,94,95,96,97,98,100,102,103,104,109,117,118,119,120,121,122,123,124,125,126,],[-12,-7,-10,-11,-42,-38,-50,-70,-66,-48,-67,-68,-44,-11,-69,-43,-46,-51,-66,-14,-75,-9,-45,-65,-47,-49,-13,-26,99,-71,-25,-75,-69,-27,-33,-70,-31,-28,-32,-30,-29,-34,99,-75,-40,-37,-41,-39,99,-75,-35,99,-36,]),'NEGACAO':([20,25,30,31,32,33,35,36,37,38,39,41,59,60,67,74,75,76,80,81,88,92,96,],[-12,58,-50,-70,-66,-48,-67,-68,-44,-11,-69,-46,-51,-66,-14,-45,-65,-47,-49,-13,-71,-69,-70,]),'ID':([0,1,2,3,4,5,7,8,9,10,12,14,15,17,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,65,66,67,70,71,73,74,75,76,80,81,83,84,87,88,90,91,92,94,95,96,97,98,100,101,102,103,104,106,108,109,110,111,114,117,118,119,120,121,122,123,124,125,126,],[11,-5,-18,16,11,-16,-15,-6,-4,-3,-8,24,-17,-2,38,38,-12,-7,-10,-11,-42,-61,38,38,-38,-50,-70,-66,-48,-62,-67,-68,-44,-11,-69,-43,-46,38,24,-57,-58,-53,-54,-55,-52,38,-59,-56,-60,-51,-66,38,38,38,-63,-64,-14,-75,85,-9,-45,-65,-47,-49,-13,-26,38,38,-71,-25,-75,-69,-27,-33,-70,-31,-28,-32,-19,-30,-29,-34,38,38,38,38,116,38,-75,-40,-37,-41,-39,38,-75,-35,38,-36,]),'INTEIRO':([0,1,2,4,8,9,10,12,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,65,66,67,69,70,73,74,75,76,80,81,83,84,87,88,90,91,92,94,95,96,97,98,100,101,102,103,104,106,108,109,110,114,117,118,119,120,121,122,123,124,125,126,],[7,-5,-18,7,-6,-4,-3,-8,-17,-2,39,39,-12,7,-7,-10,-11,-42,-61,39,39,-38,-50,-70,-66,-48,-62,-67,-68,-44,-11,-69,-43,-46,39,-57,-58,-53,-54,-55,-52,39,-59,-56,-60,-51,-66,39,39,39,-63,-64,-14,7,-75,-9,-45,-65,-47,-49,-13,-26,92,39,-71,-25,-75,-69,-27,-33,-70,-31,-28,-32,-19,-30,-29,-34,39,39,92,39,39,-75,-40,-37,-41,-39,92,-75,-35,92,-36,]),'ABREPAR':([11,16,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,65,66,67,70,73,74,75,76,80,81,83,84,87,88,89,90,91,92,94,95,96,97,98,99,100,102,103,104,105,106,108,109,110,114,117,118,119,120,121,122,123,124,125,126,],[21,21,28,28,-12,-7,-10,-11,-42,-61,28,28,-38,-50,-70,-66,-48,-62,-67,-68,-44,63,-69,-43,-46,28,-57,-58,-53,-54,-55,-52,28,-59,-56,-60,-51,-66,28,28,28,-63,-64,-14,-75,-9,-45,-65,-47,-49,-13,-26,28,28,-71,108,-25,-75,-69,-27,-33,-70,-31,-28,110,-32,-30,-29,-34,111,28,28,28,28,28,-75,-40,-37,-41,-39,28,-75,-35,28,-36,]),'DOISPONTOS':([3,5,7,45,92,93,96,],[14,-16,-15,71,-15,14,-16,]),'MAIORIGUAL':([20,25,30,31,32,33,35,36,37,38,39,41,59,60,67,74,75,76,80,81,88,92,96,],[-12,49,-50,-70,-66,-48,-67,-68,-44,-11,-69,-46,-51,-66,-14,-45,-65,-47,-49,-13,-71,-69,-70,]),'VEZES':([20,30,31,32,33,35,36,38,39,41,59,60,67,75,76,80,81,88,92,96,],[-12,-50,-70,-66,-48,-67,-68,-11,-69,65,-51,-66,-14,-65,65,-49,-13,-71,-69,-70,]),'MENOR':([20,25,30,31,32,33,35,36,37,38,39,41,59,60,67,74,75,76,80,81,88,92,96,],[-12,54,-50,-70,-66,-48,-67,-68,-44,-11,-69,-46,-51,-66,-14,-45,-65,-47,-49,-13,-71,-69,-70,]),'error':([20,22,23,24,25,29,30,31,32,33,35,36,37,38,39,40,41,59,60,67,70,73,74,75,76,80,81,83,84,88,90,91,92,94,95,96,97,98,100,102,103,104,109,117,118,119,120,121,122,123,124,125,126,],[-12,-7,-10,-11,-42,-38,-50,-70,-66,-48,-67,-68,-44,-11,-69,-43,-46,-51,-66,-14,-75,-9,-45,-65,-47,-49,-13,-26,104,-71,-25,-75,-69,-27,-33,-70,-31,-28,-32,-30,-29,-34,104,-75,-40,-37,-41,-39,104,-75,-35,104,-36,]),'FECHAPAR':([20,21,25,29,30,31,32,33,35,36,37,38,39,40,41,44,46,47,59,60,61,63,67,69,74,75,76,77,78,79,80,81,82,85,86,88,107,113,115,116,],[-12,-75,-42,-38,-50,-70,-66,-48,-67,-68,-44,-11,-69,-43,-46,70,-21,-22,-51,-66,75,-75,-14,-75,-45,-65,-47,88,-73,-74,-49,-13,-20,-23,-24,-71,-72,118,120,121,]),'LEIA':([20,22,23,24,25,29,30,31,32,33,35,36,37,38,39,40,41,59,60,67,70,73,74,75,76,80,81,83,84,88,90,91,92,94,95,96,97,98,100,102,103,104,109,117,118,119,120,121,122,123,124,125,126,],[-12,-7,-10,-11,-42,-38,-50,-70,-66,-48,-67,-68,-44,-11,-69,-43,-46,-51,-66,-14,-75,-9,-45,-65,-47,-49,-13,-26,105,-71,-25,-75,-69,-27,-33,-70,-31,-28,-32,-30,-29,-34,105,-75,-40,-37,-41,-39,105,-75,-35,105,-36,]),'SE':([20,22,23,24,25,29,30,31,32,33,35,36,37,38,39,40,41,59,60,67,70,73,74,75,76,80,81,83,84,88,90,91,92,94,95,96,97,98,100,102,103,104,109,117,118,119,120,121,122,123,124,125,126,],[-12,-7,-10,-11,-42,-38,-50,-70,-66,-48,-67,-68,-44,-11,-69,-43,-46,-51,-66,-14,-75,-9,-45,-65,-47,-49,-13,-26,106,-71,-25,-75,-69,-27,-33,-70,-31,-28,-32,-30,-29,-34,106,-75,-40,-37,-41,-39,106,-75,-35,106,-36,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'indice':([11,24,38,],[20,20,20,]),'expressao_simples':([18,19,28,43,63,84,87,106,108,109,110,114,122,125,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'acao':([84,109,122,125,],[90,90,90,90,]),'operador_soma':([18,19,28,37,43,55,62,63,64,74,84,87,106,108,109,110,114,122,125,],[27,27,27,62,27,27,27,27,27,62,27,27,27,27,27,27,27,27,27,]),'inicializacao_variaveis':([0,4,],[1,1,]),'cabecalho':([0,3,4,],[2,15,2,]),'corpo':([70,91,117,123,],[84,109,122,125,]),'lista_variaveis':([14,],[22,]),'tipo':([0,4,21,69,84,109,122,125,],[3,3,45,45,93,93,93,93,]),'expressao':([18,19,28,43,63,84,87,106,108,109,110,114,122,125,],[29,42,61,68,78,94,107,112,113,94,115,119,94,94,]),'fator':([18,19,27,28,43,55,62,63,64,84,87,106,108,109,110,114,122,125,],[30,30,59,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'retorna':([84,109,122,125,],[95,95,95,95,]),'var':([0,4,14,18,19,27,28,43,48,55,62,63,64,84,87,106,108,109,110,114,122,125,],[6,6,23,32,32,60,32,32,73,60,60,32,60,32,32,32,32,32,32,32,32,32,]),'expressao_unaria':([18,19,28,43,55,62,63,64,84,87,106,108,109,110,114,122,125,],[33,33,33,33,33,33,33,80,33,33,33,33,33,33,33,33,33,]),'leia':([84,109,122,125,],[97,97,97,97,]),'programa':([0,],[13,]),'declaracao_funcao':([0,4,],[8,8,]),'parametro':([21,69,],[46,46,]),'chamada_funcao':([18,19,27,28,43,55,62,63,64,84,87,106,108,109,110,114,122,125,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'expressao_aditiva':([18,19,28,43,55,63,84,87,106,108,109,110,114,122,125,],[37,37,37,37,74,37,37,37,37,37,37,37,37,37,37,]),'numero':([18,19,27,28,43,55,62,63,64,84,87,106,108,109,110,114,122,125,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'escreva':([84,109,122,125,],[100,100,100,100,]),'declaracao':([0,4,],[10,17,]),'lista_declaracoes':([0,],[4,]),'repita':([84,109,122,125,],[102,102,102,102,]),'lista_parametros':([21,69,],[44,82,]),'atribuicao':([0,4,18,19,28,43,63,84,87,106,108,109,110,114,122,125,],[12,12,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'operador_relacional':([25,],[55,]),'expressao_multiplicativa':([18,19,28,43,55,62,63,84,87,106,108,109,110,114,122,125,],[41,41,41,41,41,76,41,41,41,41,41,41,41,41,41,41,]),'declaracao_variaveis':([0,4,84,109,122,125,],[9,9,98,98,98,98,]),'vazio':([21,63,69,70,91,117,123,],[47,79,47,83,83,83,83,]),'lista_argumentos':([63,],[77,]),'operador_multiplicacao':([41,76,],[64,64,]),'se':([84,109,122,125,],[103,103,103,103,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaracoes','programa',1,'p_programa','TppSyn.py',35),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','TppSyn.py',42),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes1','TppSyn.py',48),
  ('declaracao -> declaracao_variaveis','declaracao',1,'p_declaracao','TppSyn.py',55),
  ('declaracao -> inicializacao_variaveis','declaracao',1,'p_declaracao','TppSyn.py',56),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','TppSyn.py',57),
  ('declaracao_variaveis -> tipo DOISPONTOS lista_variaveis','declaracao_variaveis',3,'p_declaracao_variaveis','TppSyn.py',65),
  ('inicializacao_variaveis -> atribuicao','inicializacao_variaveis',1,'p_inicializacao_variaveis','TppSyn.py',72),
  ('lista_variaveis -> lista_variaveis VIRGULA var','lista_variaveis',3,'p_lista_variaveis','TppSyn.py',79),
  ('lista_variaveis -> var','lista_variaveis',1,'p_lista_variaveis1','TppSyn.py',84),
  ('var -> ID','var',1,'p_var','TppSyn.py',91),
  ('var -> ID indice','var',2,'p_var1','TppSyn.py',96),
  ('indice -> indice ABRECOLCH expressao FECHACOLCH','indice',4,'p_indice','TppSyn.py',103),
  ('indice -> ABRECOLCH expressao FECHACOLCH','indice',3,'p_indice1','TppSyn.py',108),
  ('tipo -> INTEIRO','tipo',1,'p_tipo','TppSyn.py',114),
  ('tipo -> FLUTUANTE','tipo',1,'p_tipo1','TppSyn.py',118),
  ('declaracao_funcao -> tipo cabecalho','declaracao_funcao',2,'p_declaracao_funcao','TppSyn.py',124),
  ('declaracao_funcao -> cabecalho','declaracao_funcao',1,'p_declaracao_funcao1','TppSyn.py',129),
  ('cabecalho -> ID ABREPAR lista_parametros FECHAPAR corpo FIM','cabecalho',6,'p_cabecalho','TppSyn.py',136),
  ('lista_parametros -> lista_parametros VIRGULA lista_parametros','lista_parametros',3,'p_lista_parametros','TppSyn.py',143),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros1','TppSyn.py',148),
  ('lista_parametros -> vazio','lista_parametros',1,'p_lista_parametros1','TppSyn.py',149),
  ('parametro -> tipo DOISPONTOS ID','parametro',3,'p_parametro','TppSyn.py',156),
  ('parametro -> parametro ABRECOLCH FECHACOLCH','parametro',3,'p_parametro1','TppSyn.py',161),
  ('corpo -> corpo acao','corpo',2,'p_corpo','TppSyn.py',168),
  ('corpo -> vazio','corpo',1,'p_corpo1','TppSyn.py',173),
  ('acao -> expressao','acao',1,'p_acao','TppSyn.py',180),
  ('acao -> declaracao_variaveis','acao',1,'p_acao','TppSyn.py',181),
  ('acao -> se','acao',1,'p_acao','TppSyn.py',182),
  ('acao -> repita','acao',1,'p_acao','TppSyn.py',183),
  ('acao -> leia','acao',1,'p_acao','TppSyn.py',184),
  ('acao -> escreva','acao',1,'p_acao','TppSyn.py',185),
  ('acao -> retorna','acao',1,'p_acao','TppSyn.py',186),
  ('acao -> error','acao',1,'p_acao','TppSyn.py',187),
  ('se -> SE expressao ENTAO corpo FIM','se',5,'p_se','TppSyn.py',194),
  ('se -> SE expressao ENTAO corpo SENAO corpo FIM','se',7,'p_se1','TppSyn.py',199),
  ('repita -> REPITA corpo ATE expressao','repita',4,'p_repita','TppSyn.py',206),
  ('atribuicao -> var ATRIBUICAO expressao','atribuicao',3,'p_atribuicao','TppSyn.py',213),
  ('leia -> LEIA ABREPAR ID FECHAPAR','leia',4,'p_leia','TppSyn.py',220),
  ('escreva -> ESCREVA ABREPAR expressao FECHAPAR','escreva',4,'p_escreva','TppSyn.py',227),
  ('retorna -> RETORNA ABREPAR expressao FECHAPAR','retorna',4,'p_retorna','TppSyn.py',234),
  ('expressao -> expressao_simples','expressao',1,'p_expressao','TppSyn.py',241),
  ('expressao -> atribuicao','expressao',1,'p_expressao','TppSyn.py',242),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_expressao_simples','TppSyn.py',249),
  ('expressao_simples -> expressao_simples operador_relacional expressao_aditiva','expressao_simples',3,'p_expressao_simples1','TppSyn.py',254),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_expressao_aditiva','TppSyn.py',261),
  ('expressao_aditiva -> expressao_aditiva operador_soma expressao_multiplicativa','expressao_aditiva',3,'p_expressao_aditiva1','TppSyn.py',266),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_expressao_multiplicativa','TppSyn.py',273),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_expressao_multiplicativa1','TppSyn.py',278),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_expressao_unaria','TppSyn.py',285),
  ('expressao_unaria -> operador_soma fator','expressao_unaria',2,'p_expressao_unaria1','TppSyn.py',290),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_operador_relacional','TppSyn.py',297),
  ('operador_relacional -> MAIOR','operador_relacional',1,'p_operador_relacional','TppSyn.py',298),
  ('operador_relacional -> IGUAL','operador_relacional',1,'p_operador_relacional','TppSyn.py',299),
  ('operador_relacional -> DIFERENTE','operador_relacional',1,'p_operador_relacional','TppSyn.py',300),
  ('operador_relacional -> MENORIGUAL','operador_relacional',1,'p_operador_relacional','TppSyn.py',301),
  ('operador_relacional -> MAIORIGUAL','operador_relacional',1,'p_operador_relacional','TppSyn.py',302),
  ('operador_relacional -> ELOGICO','operador_relacional',1,'p_operador_relacional','TppSyn.py',303),
  ('operador_relacional -> OULOGICO','operador_relacional',1,'p_operador_relacional','TppSyn.py',304),
  ('operador_relacional -> NEGACAO','operador_relacional',1,'p_operador_relacional','TppSyn.py',305),
  ('operador_soma -> SOMA','operador_soma',1,'p_operador_soma','TppSyn.py',312),
  ('operador_soma -> SUBR','operador_soma',1,'p_operador_soma','TppSyn.py',313),
  ('operador_multiplicacao -> VEZES','operador_multiplicacao',1,'p_operador_multiplicacao','TppSyn.py',319),
  ('operador_multiplicacao -> DIVIDE','operador_multiplicacao',1,'p_operador_multiplicacao','TppSyn.py',320),
  ('fator -> ABREPAR expressao FECHAPAR','fator',3,'p_fator','TppSyn.py',327),
  ('fator -> var','fator',1,'p_fator1','TppSyn.py',332),
  ('fator -> chamada_funcao','fator',1,'p_fator1','TppSyn.py',333),
  ('fator -> numero','fator',1,'p_fator1','TppSyn.py',334),
  ('numero -> INTEIRO','numero',1,'p_numero','TppSyn.py',341),
  ('numero -> FLUTUANTE','numero',1,'p_numero','TppSyn.py',342),
  ('chamada_funcao -> ID ABREPAR lista_argumentos FECHAPAR','chamada_funcao',4,'p_chamada_funcao','TppSyn.py',349),
  ('lista_argumentos -> lista_argumentos VIRGULA expressao','lista_argumentos',3,'p_lista_argumentos','TppSyn.py',356),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_lista_argumentos1','TppSyn.py',361),
  ('lista_argumentos -> vazio','lista_argumentos',1,'p_lista_argumentos1','TppSyn.py',362),
  ('vazio -> <empty>','vazio',0,'p_vazio','TppSyn.py',369),
]
