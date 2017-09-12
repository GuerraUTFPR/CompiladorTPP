#!/usr/bin/python
# coding: utf-8

import ply.lex as lex
import sys

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
t_SOMA = r'\+'
t_SUBR = r'-'
t_VEZES = r'\*'
t_DIVIDE = r'\/'
t_IGUAL = r'\='
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
#t_COMENTARIO = r'\{\s*.*\s*\}'
#t_COMENTARIO = r'\{[^}]*[^{]*\}'

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9à-ú]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_COMENTARIO(t):
  #r'\{\s*.*\s*\}'
  r'\{[\s]*[^}]*[\s]*[^{]*\}'
  for x in xrange(0,len(t.value)):
    if t.value[x] == '\n':
      t.lexer.lineno += 1
  return t

def t_FLUTUANTE(t):
    r'[0-9]+[\.][0-9]*'
    t.value = float(t.value)   
    return t  

def t_INTEIRO(t):
    r'[0-9]+'
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
    print("Caractére ilegal '%s'" % t.value[0])
    t.lexer.skip(1)




def main():  
  lexer = lex.lex()
  f = open(sys.argv[1], 'r')

  data = f.read()
  
  # Give the lexer some input
  lexer.input(data)

  # Tokenize
  while True:
      tok = lexer.token()      
      if not tok: 
          break      # No more input
      tipo = tok.type
      valor = tok.value
      linha = tok.lineno
      s = '<' + tipo + ', ' + str(valor) + ', ' + str(linha) + '>'
      print s    
      #print '<' + repr(tipo) + ' ' + repr(valor) + ' ' + repr(linha) + '>'

if __name__ == "__main__":
  main()