#Class : Tokens.py
#Description : analizador léxico para el lenguaje SimpliciQL
#Author : Yony Alex Vilca Mamani
#Fecha : 07-Setiembre-2023
#Course : Compiladores
#Editor : Visual studio Code
# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# r'atring' -> r significa que la cadena es tradada sin caracteres de escape, 
# es decir r'\n' seria un \ seguido de n (no se interpretaria como salto de linea) 

 # List of token names.   This is always required
reserved = {
   'CREAR'  : 'TIPO_CREATE',
   'TABLA'  : 'TIPO_TABLE',
   'ENTERO'  : 'TIPO_INT',
   'NO' : 'TIPO_NOT',  
   'NULO'  : 'TIPO_NULL',
   'IDENTIDAD'  : 'TIPO_IDENTITY',
   'CADENAVAR'  : 'TIPO_VARCHAR',
   'UNICA'  : 'TIPO_UNIQUE',
   'POR DEFECTO'  : 'TIPO_DEFAULT',
   'RESTRICCION'  : 'TIPO_CONSTRAINT',
   'PRINCIPAL'  : 'TIPO_PRIMARY',
   'LLAVE'  : 'TIPO_KEY',
   'AUTOINCREMENTO'  : 'TIPO_AUTO_INCREMENT',
   'ASCENDENTE'  : 'TIPO_ASC',
   'ESTABLECER'  : 'TIPO_SET',
   'DONDE'  : 'TIPO_WHERE',
   'ELIMINAR'  : 'TIPO_DROP',
   'OBTENER'  : 'TIPO_SELECT',
   'DESDE'  : 'TIPO_FROM',
   'PROCEDIMIENTO'  : 'TIPO_PROCEDURE',
   'COMO'  : 'TIPO_AS',
   'INICIO'  : 'TIPO_BEGIN',
   'FIN'  : 'TIPO_END',
   'EJECUTAR'  : 'TIPO_EXEC',
   'ACTUALIZAR'  : 'TIPO_UPDATE',
   'DECIMAL'  : 'TIPO_DECIMAL',
   'REAL'  : 'TIPO_REAL',
   'BOOLEANO'  : 'TIPO_BOOLEAN',
   'FECHA'  : 'TIPO_DATE',
   'HORA'  : 'TIPO_TIME',
   'FECHAHORA'  : 'TIPO_DATETIME',
   'POR'  : 'TIPO_BY',
   'ORDENAR'  : 'TIPO_ORDER',
   'DESCENDENTE'  : 'TIPO_DESC',
   'FLOTANTE'  : 'TIPO_FLOAT',
   'EVALUAR'  : 'TIPO_EVAL',
   'LIMPIAR'  : 'TIPO_CLEAR',
   'INSERTAR'  : 'TIPO_INSERT',
   'ABORTAR'  : 'TIPO_ABORT',
   'AGREGAR'  : 'TIPO_ADD',
   'ALINEAR'  : 'TIPO_ALIGN',
   'POR_DEFECTO'  : 'TIPO_BYDEFAULT',
   'TODOS'  : 'TIPO_ALL',
   'MOVER'  : 'TIPO_MOVE',
   'PROMEDIO'  : 'TIPO_AVG',
   'EN'  : 'TIPO_IN',
   'DOBLE'  : 'TIPO_DOUBLE',
   'EXTRAER'  : 'TIPO_EXTRACT',
   'ALTERAR'  : 'TIPO_ALTER',
   'COLUMNA'  : 'TIPO_COLUMN',
   'RENOMBRAR'  : 'TIPO_RENAME',
   'HACIA'  : 'TIPO_TO',
   'DENTRO'  : 'TIPO_INTO',
   'VALORES'  : 'TIPO_VALUES',
   'FORANEA'  : 'TIPO_FOREIGN',
   'REFERENCIA'  : 'TIPO_REFERENCE',
   'CONTAR'  : 'TIPO_COUNT',
   'DISTINTO'  : 'TIPO_DISTINCT',
}

tokens = [
    'NUMBER',
    'MAS',
    'MENOS',
    'COMODIN',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'IGUAL',
    'COMA',
    'DOSPUNTOS',
    'PUNTOYCOMA',
    'ID',
    'CADENA',
    'COMENTARIOL',
    'COMENTARIOB',
    'MAYORIGUAL',
    'MENORIGUAL',
    'PUNTO',
    'NOIGUALA',
    'NOMENORQUE',
    'NOMAYORQUE',
    'MODULO',
    "PMARCA",
    "MAYOR",
    "MENOR"
    
 ] + list(reserved.values())

 # Regular expression rules for simple tokens
t_MAS    = r'\+'
t_MENOS   = r'-'
t_COMODIN   = r'\*'
t_DIVIDE  = r'/'
t_IGUAL  = r'\='
t_MAYORIGUAL    = r'\>='
t_MENORIGUAL  = r'\<='
t_MAYOR  = r'>'
T_MENOR  = r'<'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NOIGUALA  = r'\<\>'
t_NOMENORQUE = r'\!\>'
t_NOMAYORQUE  = r'\!\<'
t_MODULO  = r'%'
t_COMA   = r','
t_DOSPUNTOS   = r':'
t_PUNTOYCOMA = r';'
t_COMENTARIOL = r'--.*'
t_COMENTARIOB = r'/\*(.|\n)*?\*/'
t_PUNTO = r'\.'
t_PMARCA = r'@\w+'

#t_NUMBER  = r'\d+' 

# A regular expression rule with some action code
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]+'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_CADENA(t):
    r"'[^']*'"
    t.value = t.value[1:-1] # removemos las comillas simples
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # guardamos el valor del lexema  
    return t

 # Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

 # Error handling rule
def t_error(t):
    print("Illegal character '%s' at line %d, column %d" % (t.value[0], t.lineno, t.lexpos))
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
with open('data1.txt', 'r') as file:
    data = file.read()

# Give the lexer some input
lexer.input(data)

# Tokenize
tokensLexer = []
for tok in lexer:
    tokensLexer.append({
        'type': tok.type,
        'lexeme': tok.value,
        'line': tok.lineno,
        'column': tok.lexpos - lexer.lexdata.rfind('\n', 0, tok.lexpos)
    })

print(tokensLexer)
