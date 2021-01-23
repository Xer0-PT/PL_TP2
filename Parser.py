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

    # Recebe o ficheiro/texto a que vai fazer parse
    def Parse(self, input, **kwargs):
        self.lexer = Lexer()
        self.lexer.Build(input, **kwargs)
        self.parser = yacc.yacc(module=self, **kwargs)
        program = self.parser.parse(lexer=self.lexer.lexer)
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
                    print("Division by zero")
                    exit(1)
                return left / right
            else:
                print(f"Unknown operator: {op}")

        if type(val) == float:
            if val < 0:
                val = val * (-1)
            return val

        if type(val) == tuple:
            return val

        # Verifica se é uma variável
        if val in self.vars:
            return self.vars[val]

        print(f"Variable {val} undefined")
        return 0


    def p_error(self, p):
        print("Syntax error", file=sys.stderr)
        if p:
            print(f"Unexpected token '{p.type}'", file=sys.stderr)
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

    def p_var(self, p):
        """ var : VAR
                | '"' VAR
                | ':' VAR """

        if len(p) == 3:
            p[0] = p[2]
        else:
            p[0] = p[1]

    def p_command0(self, p):
        """ command : forward NUMBER 
                    | fd NUMBER 
                    | forward var
                    | fd var """
        
        p[0] = Command("forward", p[2])

    def p_command1(self, p):
        """ command : right NUMBER 
                    | rt NUMBER
                    | right var
                    | rt var """

        p[0] = Command("right", p[2])

    def p_command2(self, p):
        """ command : backward NUMBER 
                    | bk NUMBER
                    | backward ':' VAR
                    | bk ':' VAR """
        p[0] = Command("backward", p[2])

    def p_command3(self, p):
        """ command : left NUMBER 
                    | lt NUMBER
                    | left ':' VAR
                    | lt ':' VAR """
        p[0] = Command("left", p[2])

    # SETPOS | SETXY
    def p_command4(self, p):
        """ command : setpos '[' NUMBER NUMBER ']'
                    | setxy NUMBER NUMBER
                    | setpos '[' ':' VAR NUMBER ']'
                    | setpos '[' NUMBER ':' VAR ']'
                    | setpos '[' ':' VAR ':' VAR ']'
                    | setxy ':' VAR NUMBER
                    | setxy NUMBER ':' VAR
                    | setxy ':' VAR ':' VAR """
        
        # Obrigado Professor
        if len(p) == 6:
            p[0] = Command("setpos", {"x": p[3], "y": p[4]})
        else:
            p[0] = Command("setpos", {"x": p[2], "y": p[3]})

    def p_command5(self, p):
        """ command : setx NUMBER 
                    | setx ':' VAR"""
        p[0] = Command("setx", p[2])

    def p_command6(self, p):
        """ command : sety NUMBER
                    | sety ':' VAR """
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
        """ command : setpencolor '[' NUMBER NUMBER NUMBER ']'
                    | setpencolor '[' NUMBER NUMBER ':' VAR ']'
                    | setpencolor '[' NUMBER ':' VAR NUMBER ']'
                    | setpencolor '[' NUMBER ':' VAR ':' VAR ']'
                    | setpencolor '[' ':' VAR NUMBER NUMBER ']'
                    | setpencolor '[' ':' VAR NUMBER ':' VAR ']'
                    | setpencolor '[' ':' VAR ':' VAR NUMBER ']'
                    | setpencolor '[' ':' VAR ':' VAR ':' VAR ']' """

        color = (p[3], p[4], p[5])

        p[0] = Command("pencolor", color)

    def p_command11(self, p):
        """ command : make '"' VAR NUMBER
                    | make '"' VAR ':' VAR OPERATOR NUMBER
                    | make '"' VAR NUMBER OPERATOR ':' VAR """

        if len(p) == 5:
            p[0] = Command("make", {"make": 1, "var": p[3], "number": p[4]})
        if len(p) == 8:
            if p[4] == ":":
                p[0] = Command("make", {"make": 2, "var1": p[3], "var2": p[5], "operator": p[6],"number": p[7]})
            else:
                p[0] = Command("make", {"make": 3, "var1": p[3], "number": p[4], "operator": p[5], "var2": p[7]})
    
    
    def p_command12(self, p):
        """ command : repeat NUMBER '[' program ']' 
                    | repeat ':' VAR '[' program ']' """

        if p[2] == "NUMBER":
            p[0] = Command("repeat", {"repeat": 1, "number": p[2], "code": p[4]})
        else:
            p[0] = Command("repeat", {"repeat": 2, "var": p[3], "code": p[5]})


    def p_command13(self, p):
        """ command : while '[' ':' VAR SIGN NUMBER ']' '[' program ']' """
        
        p[0] = Command("while", {'var': p[4], 'sign': p[5], 'number': p[6], 'code': p[9]})
