from ast import AST
from ply import yacc
from TppSyn import tokens

def programa(t):
	'''programa : lista_declaracoes '''
	t[0] = t[1]
	
def lista_declaracoes(t):
	