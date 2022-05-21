import glob

from lark import Lark, Transformer
import os


class CalcTransformer(Transformer):
    def add(self, args):
        # print(args[0].children[0].value)
        # print(args)
        # print(args[1].children[0].value)
        # a = int(args[0].children[0].value)
        # b = int(args[1].children[0].value)
        # return int(args[0]) + int(args[1])
        # return a + self.product(args[1])
        return args[0] + args[1]

    def sub(self, args):
        return args[0] - args[1]

    def mul(self, args):
        return args[0] * args[1]

    def dev(self, args):
        return args[0] / args[1]

    def number(self, args):
        return int(args[0])

    def neg(self, args):
        return -1 * int(args[0])


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

?if: "if" "(" or ")" "{" stmts "}" ("else" "{" stmts "}")?

?for: "for" "("type? NAME "=" sum";" or ";" (NAME "=")? sum ")" "{" stmts "}"

?while: "while" "(" or ")" "{" stmts "}"

?return: "return" sum

?var_init: type? NAME ("["[NAME | NUMBER]"]")* "=" [sum | "'" /./ "'" | OPEN_BRACE NUMBER ("," NUMBER)* CLOSE_BRACE ] 
    | type NAME array_append*


?string: DOUBLE_QUOTE /[^\n]/*  DOUBLE_QUOTE

?array_append: "["[sum]"]"


?func: type NAME "(" params? ")" "{" stmts "}"

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


COMMENT: "//" /[^\n]/*
BACKTICK     : "`"
PERCENTAGE   : "%"
EXCLAMATION  : "!"
DOUBLE_QUOTE : "\""

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
path = ''
for filename in glob.glob(os.path.join(path, '*.txt')):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        ast = parser.parse(f)
        print(ast.pretty())
# , parser='lalr', transformer=CalcTransformer()
ast = parser.parse(f)
print(ast.pretty())
# print(ast)
