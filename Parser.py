# Parser.py

import sys
import ply.yacc as yacc
from Lexer import Lexer
from Turtle import Turtle
from Command import Command

class Parser:
    
    tokens = Lexer.tokens

    # Tem de ter um sitio para guardar o parser
    # Tem de ter um sitio para guardar o lexer
    def __init__(self):
        self.parser = None
        self.lexer = None
        self.turtle = Turtle()
        self.vars = {}
        self.funcs = {}

    def Parse(self, input, **kwargs):
        self.lexer = Lexer()
        self.lexer.Build(input, **kwargs)
        self.parser = yacc.yacc(module=self, **kwargs)
        program = self.parser.parse(lexer=self.lexer.lexer)
        print(program)
        Command.exec(program, self)

    def value(self, val):

        if type(val) == dict and "operator" in val:
            left = self.value(val["left"])
            right = self.value(val["right"])
            op = val["operator"]
            if   op == "+": return left + right
            elif op == "*": return left * right
            elif op == "-": return left - right
            elif op == "/":
                if right == 0:
                    print("(Parser.py) Division by zero")
                    exit(1)
                return left / right
            else:
                print(f"(Parser.py) Unknown operator: {op}")

        if type(val) == float:
            if val < 0:
                val = val * (-1)
            return val

        if type(val) == tuple:
            return val

        # Verifica se é uma variável e devolve valor da variável
        if val in self.vars:
            return self.vars[val]

        print(f"(Parser.py) Variable {val} undefined")
        return 0


    def p_error(self, p):
        print("(Parser.py) Syntax error", file=sys.stderr)
        if p:
            print(f"(Parser.py) Unexpected token '{p}'", file=sys.stderr)
        exit(1)

    # Isto é um programa
    def p_program0(self, p):
        """ program : command """
        p[0] = [p[1]]

    # Isto é a recursividade de um programa
    def p_program1(self, p):
        """ program : program command """
        lst = p[1]
        lst.append(p[2])
        p[0] = lst

    def p_value(self, p):
        """ value   : NUMBER
                    | '"' VAR
                    | ':' VAR """

        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_command0(self, p):
        """ command : forward value 
                    | fd value """
        
        p[0] = Command("forward", p[2])

    def p_command1(self, p):
        """ command : right value 
                    | rt value """
        
        p[0] = Command("right", p[2])

    def p_command2(self, p):
        """ command : back value 
                    | bk value """

        p[0] = Command("backward", p[2])

    def p_command3(self, p):
        """ command : left value 
                    | lt value """

        p[0] = Command("left", p[2])

    # SETPOS | SETXY
    def p_command4(self, p):
        """ command : setpos '[' value value ']'
                    | setxy value value """
        
        if len(p) == 6:
            args = {'x': p[3], 'y': p[4]}
        else:
            args = {'x': p[2], 'y': p[3]}

        p[0] = Command("setpos", args)                

    def p_command5(self, p):
        """ command : setx value """

        p[0] = Command("setx", p[2])
        
    def p_command6(self, p):
        """ command : sety value """
        p[0] = Command("sety", p[2])
        
    def p_command7(self, p):
        """ command : home """
        p[0] = Command("home", "")

    def p_command8(self, p):
        """ command : pendown
                    | pd """
        p[0] = Command("pendown", "")
    
    def p_command9(self, p):
        """ command : penup
                    | pu """
        p[0] = Command("penup", "")
    
    def p_command10(self, p):
        """ command : setpencolor '[' value value value ']' """

        p[0] = Command("pencolor", {'r': p[3], 'g': p[4], 'b': p[5]})
            
    def p_command11(self, p):
        """ command : make value value
                    | make value value OPERATOR value """

        if len(p) == 4:
            args = {'var': p[2], 'val1': p[3]}
        else:
            args = {'var': p[2], 'val1': p[3], 'operator': p[4], 'val2': p[5]}

        p[0] = Command("make", args)
    
    def p_command12(self, p):
        """ command : repeat value '[' program ']' """

        p[0] = Command("repeat", {"value": p[2], "code": p[4]})

    def p_command13(self, p):
        """ command : while '[' value SIGN value ']' '[' program ']' """
        
        p[0] = Command("while", {'value1': p[3], 'sign': p[4], 'value2': p[5], 'code': p[8]})

    # IF | IFELSE
    def p_command14(self, p):
        """ command : if value SIGN value '[' program ']'
                    | ifelse value SIGN value '[' program ']' '[' program ']' """

        if len(p) == 8:
            args = {'value1': p[2], 'sign': p[3], 'value2': p[4], 'code1': p[6]}
        else:
            args = {'value1': p[2], 'sign': p[3], 'value2': p[4], 'code1': p[6], 'code2': p[9]}

        p[0] = Command("if", args)

    def p_varlist(self, p):
        """ varlist :
                    | value
                    | varlist value """
        if len(p) == 1:
            p[0] = []
        elif len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1]
            p[0].append(p[2])

    def p_command16(self, p):        
        """ command : TO STR varlist program END """

        p[0] = Command("to", {'name': p[2], 'args': p[3], 'code': p[4]})

    def p_valuelist(self, p):
        """ valuelist :
                        | value
                        | valuelist value """
        if len(p) == 1:
            p[0] = []
        elif len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1]
            p[0].append(p[2])

    def p_command17(self, p):
        """ command : STR valuelist """
        p[0] = Command("call", {'name': p[1], 'args': p[2]})
