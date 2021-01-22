# Lexer.py
import ply.lex as lex
import sys


class Lexer:
    literals = """:,"[]"""
    t_ignore = " \n\t"
    
    tokens = ("forward", "fd", "right", "rt", "backward", "bk", "left", "lt", "setpos", "setxy", "setx",
                 "sety", "home", "pendown", "pd", "penup", "pu", "setpencolor", "NUMBER")

    def t_COMMAND(self, t):
        r"""(forward|fd)|(back|bk)|(left|lt)|(right|rt)|setpos|setxy|setx|sety|home|
            (pendown|pd)|(penup|pu)|setpencolor"""
        t.type = t.value.replace(" ", "")
        return t

    def t_OPERATION(self, t):
        r"[+]|[-]|[/]|[*]"
        return t
    
    def t_VAR(self, t):
        r"[a-wyz][0-9a-z]*"
        return t
    
    def t_SIGN(self,t):
        r"[>]|[<]"
        return t

    def t_NUMBER(self, t):
        r"[0-9.]+"
        t.value = float(t.value)
        return t


    def t_error(self, t):
        print(f"Parser error. Unexpected char: {t.value[0]}", file=sys.stderr)
        exit(1)

    def __init__(self):
       self.lexer = None

    def Build(self, input, **kwargs):
       self.lexer = lex.lex(module=self, **kwargs)
       self.lexer.input(input)



