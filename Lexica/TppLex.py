#!/usr/bin/python
# -*- coding: utf-8 -*-
import ply.lex as lex
import sys

def __init__(self):
self.lexer = lex.lex(debug=False, module=self, optimize=False)

#hash de palavras reservadas
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
'escreva'   :'ESCREVA',
'inteiro'   :'INTEIRO',    

}
#vetor de tokens concatenado com o hash de palavras reservadas
tokens = [
'ID',
'VIRGULA',
'ATRIBUICAO',  

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


] + list(reserved.values())

# Expressão regular para tokens simples
t_SOMA = r'\+'
t_SUBR = r'\-'
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




# Expressão regular para identificadores e palavras reservadas
def t_ID(self, t):
r'[a-zA-Z][a-zA-Z_0-9à-ú]*'
t.type = self.reserved.get(t.value,'ID') #verifica se é palavra reservada
return t

# Expressão regular para comentários, com tratamento de contagem de linhas
def t_COMENTARIO(self, t):
r'\{[\s]*[^}]*[\s]*[^{]*\}'    

flag = 0
for x in xrange(0,len(t.value)): #verificando a quantidade de quebra de linhas
if t.value[x] == '{':
flag += 1
elif t.value[x] == '}':
flag -= 1

if t.value[x] == '\n':
t.lexer.lineno += 1

#  print flag
if flag != 0:
print "Comentario sem fechar chaves."


# Expressão regular para identificar numeros flutuante, considerando o ponto (ex: 2. é flutuante)
def t_FLUTUANTE(self, t):
r'[0-9]+[\.][0-9]*'
t.value = float(t.value)   
return t  

#exŕessão regular para identificar números inteiros
def t_INTEIRO(self, t):
r'[0-9]+'
t.value = int(t.value)   
return t

# regra para contagem de linhas
def t_newline(self, t):
r'\n+'
t.lexer.lineno += len(t.value)


# caracteres ignorados
t_ignore  = '\t '

# Mostrar erro
def t_error(self, t):
print "Caractére ilegal" + t.value[0]
t.lexer.skip(1)


def main():  
  lexer = lex.lex()
  f = open(sys.argv[1], 'r')

  arq = open(sys.argv[1]+"_tokens.txt", 'w')

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
      arq.write(s+'\n')      

  f.close()
  arq.close()

if __name__ == "__main__":
  main()
