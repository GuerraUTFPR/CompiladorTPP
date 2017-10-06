# -*- coding: utf-8 -*-

from ast import AST
from ply import yacc
from TppLex import Lexer

class Tree:

    def __init__(self, type_node, child=[], value=''):
        self.type = type_node
        self.child = child
        self.value = value

    def __str__(self):
        return self.type

class Parser:

    def __init__(self, code):
        lex = Lexer()
        self.tokens = lex.tokens
        self.precedence = (           
            ('left', 'IGUAL', 'NEGACAO', 'MAIORIGUAL', 'MAIOR', 'MENORIGUAL', 'MENOR'),
            ('left', 'SOMA', 'SURB'),
            ('left', 'VEZES', 'DIVIDE'),
        )
        parser = yacc.yacc(debug=False, module=self, optimize=False)
        self.ast = parser.parse(code)


	def p_programa(self, p):
		'''
		programa : lista_declaracoes
		'''
		p[0] = Tree('programa',[p[1]])

	
	def p_lista_declaracoes(self, p):
		'''
		lista_declaracoes : lista_declaracoes declaracao
						  	|declaracao
		'''
		if (len(p) == 3):
			p[0] = Tree('lista_declaracoes', [p[1],p[2]])
		elif (len(p) == 2):
			p[0] = Tree('lista_declaracoes', [p[1]])

	def p_declaracao(self, p):
		'''
		declaracao: declaracao_variaveis
					|inicializacao_variaveis
					|declaracao_funcao

		'''
		p[0] = Tree('declaracao', [p[1]])

	def p_declaracao_variaveis(self, p):
		'''
		declaracao_variaveis: tipo ":" lista_variaveis
		'''
		p[0] = Tree('declaracao_variaveis', [p[1],p[3]], p[2])

	def p_inicializacao_variaveis(self, p):
		'''
		inicializacao_variaveis: atribuicao

		'''
		p[0] = Tree('inicializacao_variaveis', [p[1]])

	def p_lista_variaveis():
		'''
		lista_variaveis: lista_variaveis "," var
						 |var
		'''
		if

		########################### socorrrrrooooo #################
