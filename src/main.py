from pathlib import Path
from os import listdir
from os.path import isfile, join

from lark import Lark, Transformer


grammar = """
?type: "int"
    | "float"
    | "void"
    | "bool"
    | "char"

?param: var_init

?params: param ("," param )*

?literal: NUMBER
    | NAME

?stmt: if
    | sum ";"
    | var_init ";"
    | for
    | while
    | return ";"
    | "print" "(" sum array_append* ")" ";"

?stmts: stmt*

?or: compare
    | and
    | or "||" and

?and: compare
    | compare "&&" compare

?compare: sum "==" sum
    | sum "!=" sum
    | sum ">=" sum
    | sum "<=" sum
    | sum ">" sum
    | sum "<" sum
    | "true"
    | "false"
    | NUMBER
    | NAME
    | "!" compare

?if: "if" OPEN_PAREN or CLOSE_PAREN OPEN_BRACE stmts CLOSE_BRACE ("else" OPEN_BRACE stmts CLOSE_BRACE)?

?for: "for" OPEN_PAREN type? NAME EQUALLY sum";" or ";" (NAME EQUALLY)? sum CLOSE_PAREN OPEN_BRACE stmts CLOSE_BRACE

?while: "while" OPEN_PAREN or CLOSE_PAREN OPEN_BRACE stmts CLOSE_BRACE

?return: "return" sum

?var_init: type? NAME (OPEN_BRACKET[NAME | NUMBER]CLOSE_BRACKET)* EQUALLY [sum | "'" /./ "'" | OPEN_BRACE NUMBER ("," NUMBER)* CLOSE_BRACE ]
    | type NAME array_append*


?string: DOUBLE_QUOTE /[^\\n]/*  DOUBLE_QUOTE

?array_append: OPEN_BRACKET [sum] CLOSE_BRACKET


?func: type NAME OPEN_PAREN params? CLOSE_PAREN OPEN_BRACE stmts CLOSE_BRACE

?start: func*

?sum: product
    | sum "+" product   -> add
    | sum "-" product   -> sub
    | atom "++"
    | atom "--"

?product: atom
    | product "*" atom  -> mul
    | product "/" atom  -> div

?atom: NUMBER           -> number
    | "-" atom         -> neg
    | NAME             -> var
    | NAME array_append
    | "(" sum ")"
    | string
    | NAME "(" sum? ("," sum)* ")" -> func_colling


COMMENT: "//" /[^\\n]/*
BACKTICK     : "`"
PERCENTAGE   : "%"
EXCLAMATION  : "!"
DOUBLE_QUOTE : "\\""
EQUALLY: "="


?parens       : OPEN_PAREN | CLOSE_PAREN | OPEN_BRACKET | CLOSE_BRACKET
OPEN_BRACKET  : "["
CLOSE_BRACKET : "]"
OPEN_BRACE    : "{"
CLOSE_BRACE   : "}"
OPEN_PAREN    : "("
CLOSE_PAREN   : ")"


%import common.CNAME -> NAME
%import common.NUMBER
%import common.WS_INLINE
%import common.WS


%ignore COMMENT
%ignore WS_INLINE
%ignore WS

          """
parser = Lark(grammar)
path = "E:/tk/file/"
only_files = [f for f in listdir(path) if isfile(join(path, f))]
all_lines = []
for file_name in only_files:
    file_path = Path(path) / file_name
    with open(file_path, 'r') as f:
        file_content = f.read()
        ast = parser.parse(file_content)
        print(ast.pretty())
        # print(ast)
