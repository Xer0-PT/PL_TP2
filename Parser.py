# Parser.py

import sys
import ply.yacc as yacc
from Lexer import Lexer

from Turtle import Turtle

class Parser:
    
    tokens = Lexer.tokens

    #tokens = ("COMMAND", "INT")

    # Tem de ter um sitio para guardar o parser
    # Tem de ter um sitio para guardar o lexer
    def __init__(self):
        self.parser = None
        self.lexer = None
        self.turtle = Turtle()

    # Recebe o ficheiro/texto a que vai fazer parse
    def Parse(self, input, **kwargs):
        self.lexer = Lexer()
        self.lexer.Build(input, **kwargs)
        self.parser = yacc.yacc(module=self, **kwargs)
        ans = self.parser.parse(lexer=self.lexer.lexer)
        print(ans)

    def p_error(self, t):
        print("Syntax error", file=sys.stderr)
        exit(1)

    # Isto é um programa
    def p_program0(self, t):
        """ program : command """

    # Isto é a recursividade de um programa
    def p_program1(self, t):
        """ program : program command """

    def p_command0(self, p):
        """ command : forward INT
                    | fd INT """
        self.turtle.addLine("fd", p[2])

    def p_command1(self, p):
        """ command : backward INT
                    | bk INT """
        self.turtle.addLine("bk", p[2])

    def p_command2(self, t):
        """ command : right INT
                    | rt INT """


    #def p_color(self, p):
    #    """ color : [INT INT INT] """
    #    p[0] = (p[1], p[2], p[3])

    # def p_pos(self, p):
    #     """ pos : INT """
    #     p[0] = (p[1])