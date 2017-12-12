# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join
import os




onlyfiles = [f for f in listdir("/home/guerra/Área de trabalho/UTFPR/Compiladores/ProjetoTpp/Semantica/implementação/semantica-testes/") if isfile(join ("//home/guerra/Área de trabalho/UTFPR/Compiladores/ProjetoTpp/Semantica/implementação/semantica-testes/",f))]
file = open("SaidasSemanticas.txt","w")

for x in sorted(onlyfiles):
	if str(x) == "script.py" or str(x) == "SaidasSemanticas.txt":
		pass

	os.system("echo Executando: "+ str(x))
	os.system("python sem.py semantica-testes/" + str(x))
	os.system("echo \n")
