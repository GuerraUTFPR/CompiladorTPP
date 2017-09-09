#!/usr/bin/python
# coding: utf-8

import ply.lex as lex
reserved = {
  'se'        :'SE',
  'então'     :'ENTAO',
  'senão'     :'SENAO',
  'fim'       :'FIM',
  'repita'    :'REPITA' ,
  'flutuante' :'FLUTUANTE',
  'retorna'   :'RETORNA',
  'até'       :'ATE',
  'leia'      :'LEIA',
  'escreve'   :'ESCREVE',
  'inteiro'   :'INTEIRO',
  'principal' :'PRINCIPAL',

}

tokens = [
  'ID',
  'VIRGULA',
  'ATRIBUICAO',
  'COMENTARIO',  

  'SOMA',
  'SUBR',
  'VEZES',
  'DIVIDE',   
  'IGUAL',

  'MENOR',
  'MAIOR',
  'MENORIGUAL',
  'MAIORIGUAL',
  'ELOGICO',
  'OULOGICO',
  'NEGACAO',
  'DIFERENTE',

  'ABREPAR',
  'FECHAPAR',
  'DOISPONTOS',
  'ABRECOLCH',
  'FECHACOLCH',   
  'CHAVEDIR',
  'CHAVEESQ',

] + list(reserved.values())


# Regular expression rules for simple tokens
t_SOMA    = r'\+'
t_SUBR   = r'-'
t_VEZES   = r'\*'
t_DIVIDE  = r'\/'
t_IGUAL = r'\=\='
t_VIRGULA = r'\,'
t_ATRIBUICAO = r'\:\='
t_MENOR = r'\<'
t_MAIOR = r'\>'
t_MENORIGUAL = r'\<\='
t_MAIORIGUAL = r'\>\='
t_ABREPAR  = r'\('
t_FECHAPAR  = r'\)'
t_DOISPONTOS = r'\:'
t_ABRECOLCH = r'\['
t_FECHACOLCH = r'\]'
t_ELOGICO = r'\&\&'
t_OULOGICO = r'\|\|'
t_NEGACAO = r'\!'
t_DIFERENTE = r'\!\='
t_CHAVEDIR = r'\}'
t_CHAVEESQ = r'\{'
t_COMENTARIO = r'\{.*\}'


def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9à-ú]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t


def t_FLUTUANTE(t):
    r'[-+]?[0-9]+[\.][0-9]*'
    t.value = float(t.value)   
    return t  

def t_INTEIRO(t):
    r'[-+]?[0-9]+'
    t.value = int(t.value)   
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
inteiro principal()  
  inteiro: digitado
  inteiro: i
  i := 1
  repita
    flutuante: f
    inteiro: int
    flutuante: resultado
    f := i/2.
    int := i/2
    resultado := f - int
    
    se  resultado > 0
      escreva (i)
    fim
    i := i+1
  até i <= digitado
fim
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)