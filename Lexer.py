# Lexer.py
import ply.lex as lex
import sys


class Lexer:
    literals = """:,"[]"""
    t_ignore = " \n\t"
    
    tokens = ("forward", "fd", "INT")

    def t_COMMAND(self, t):
        r"""(forward|fd)"""        
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

    def t_INT(self, t):
        r"[0-9]+"
        t.value = int(t.value)
        return t


    def t_error(self, t):
        print(f"Parser error. Unexpected char: {t.value[0]}", file=sys.stderr)
        exit(1)

    def __init__(self):
       self.lexer = None

    def Build(self, input, **kwargs):
       self.lexer = lex.lex(module=self, **kwargs)
       self.lexer.input(input)



