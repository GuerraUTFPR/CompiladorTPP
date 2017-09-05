import ply.lex as lex

reserved = {
  'se'        : 'SE',
  'então'     : 'ENTAO',
  'senão'     : 'SENAO',
  'fim'       : 'FIM',
  'repita'    : 'REPITA' ,
  'flutuante' : 'FLUTUANTE',
  'retorna'   : 'RETORNA',
  'até'       : 'ATE',
  'leia'      : 'LEIA',
  'escreve'   : 'ESCREVE',
  'inteiro'   : 'INTEIRO',
}

tokens = [
   'NUMERO',
   'SOMA',
   'SUBR',
   'VEZES',
   'DIVIDE',
   'IGUAL',
   'VIRGULA',
   'ATRIBUICAO',
   'MENOR',
   'MAIOR',
   'MENORIGUAL',
   'MAIORIGUAL',
   'ABREPAR',
   'FECHAPAR',
   'DOISPONTOS',
   'ABRECOLCH',
   'FECHACOLCH',
   'ELOGICO',
   'OULOGICO',
   'NEGACAO',
   'ID',
] + list(reserved.values())


# Regular expression rules for simple tokens
t_SOMA    = r'\+'
t_SUBR   = r'-'
t_VEZES   = r'\*'
t_DIVIDE  = r'\/'
t_IGUAL = r'\='
t_VIRGULA = r'\,'
#t_ATRIBUICAO = r'\:\='
t_MENOR = r'\<'
t_MAIOR = r'\>'
#t_MENORIGUAL = r'\<\='
#t_MAIORIGUAL = r'\>\='
t_ABREPAR  = r'\('
t_FECHAPAR  = r'\)'
t_DOISPONTOS = r'\:'
t_ABRECOLCH = r'\['
t_FECHACOLCH = r'\]'
#t_ELOGICO = r'\&\&'
#t_OULOGICO = r'\|\|'
t_NEGACAO = r'\!'


def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return 
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
3 + 4 * 10
  + -20 *2
'''

# Give the lexer some input
lexer.input(data)

# Tokenize

for tok in lexer:
    print(tok)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)