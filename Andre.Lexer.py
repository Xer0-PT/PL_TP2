# Lexer.py
import ply.lex as lex
import sys


class Lexer:
    literals = ""","[]"""
    t_ignore = " \n\t"
    
    tokens = ("forward", "fd", "right", "rt", "back", "bk", "left", 
                "lt", "setpos", "setxy", "setx", "sety", "home", "pendown",
                "pd", "penup", "pu", "setpencolor", "make", "repeat", "while",
                "if", "ifelse", "NUMBER", "TO", "END", "STR", "VAR", "OPERATOR", "SIGN")

    def t_COMMAND(self, t):
        r"""(forward|fd)|(back|bk)|(left|lt)|(right|rt)|setpos|setxy|setx|sety|home|
            (pendown|pd)|(penup|pu)|setpencolor|make|repeat|while|if|ifelse|TO|END"""
        t.type = t.value.replace(" ", "")
        # print(t.value)
        return t

    def t_OPERATOR(self, t):
        r"[+]|[-]|[/]|[*]"
        return t


    def t_VAR(self, t):
        r"(:|\")[a-z]+"
        return t

    def t_STR(self, t):
        r"[a-zA-Z]+"
        return t


    def t_SIGN(self,t):
        r"[>]|[<]|[=]"
        return t

    def t_NUMBER(self, t):
        r"[0-9.]+"
        t.value = float(t.value)
        return t

    def t_make(self, t):
        r"""make"""
        return t

    def t_error(self, t):
        print(f"Parser error. Unexpected char: {t.value[0]}", file=sys.stderr)
        exit(1)

    def __init__(self):
       self.lexer = None

    def Build(self, input, **kwargs):
       self.lexer = lex.lex(module=self, **kwargs)
       self.lexer.input(input)



