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
            print(p)
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

    def p_command0(self, p):
        """ command : forward NUMBER 
                    | fd NUMBER 
                    | forward VAR
                    | fd VAR """
        if isinstance(p[2], str):
            p[0] = Command("forward", p[2][1:])
        else:
            p[0] = Command("forward", p[2])

    def p_command1(self, p):
        """ command : right NUMBER 
                    | rt NUMBER
                    | right VAR
                    | rt VAR """
        if isinstance(p[2], str):
            p[0] = Command("right", p[2][1:])
        else:
            p[0] = Command("right", p[2])

    def p_command2(self, p):
        """ command : back NUMBER 
                    | bk NUMBER
                    | back VAR
                    | bk VAR """

        if len(p) == 3:
            p[0] = Command("backward", p[2][1:])
        else:
            p[0] = Command("backward", p[3])

    def p_command3(self, p):
        """ command : left NUMBER 
                    | lt NUMBER
                    | left VAR
                    | lt VAR """

        if isinstance(p[2], str):
            p[0] = Command("left", p[2][1:])
        else:
            p[0] = Command("left", p[2])

    # SETPOS | SETXY
    def p_command4(self, p):
        """ command : setpos '[' NUMBER NUMBER ']'
                    | setxy NUMBER NUMBER
                    | setpos '[' VAR NUMBER ']'
                    | setpos '[' NUMBER VAR ']'
                    | setpos '[' VAR VAR ']'
                    | setxy VAR NUMBER
                    | setxy NUMBER VAR
                    | setxy VAR VAR """
        if p[1] == 'setpos':
            if ':' not in p[3] and ':' not in p[4]: # number number
                p[0] = Command("setpos", {"x": p[3], "y": p[4]})
            elif ':' in p[3] and ':' not in p[4]: # var number
                p[0] = Command("setpos", {"x": p[3][1:], "y": p[4]})
            elif ':' in p[3] and ':' in p[4]: # var var
                p[0] = Command("setpos", {"x": p[3][1:], "y": p[4][1:]})
            else: # number var
                p[0] = Command("setpos", {"x": p[3], "y": p[4][1:]})
        else:
            if ':' not in p[2] and ':' not in p[3]: # number number
                p[0] = Command("setpos", {"x": p[2], "y": p[3]})
            elif ':' in p[2] and ':' not in p[3]: # var number
                p[0] = Command("setpos", {"x": p[2][1:], "y": p[3]})
            elif ':' in p[2] and ':' in p[4]: # var var
                p[0] = Command("setpos", {"x": p[2][1:], "y": p[3][1:]})
            else: # number var
                p[0] = Command("setpos", {"x": p[2], "y": p[3][1:]})

        # # Obrigado Professor
        # if len(p) == 6: #setpos '[' NUMBER NUMBER ']'
        #     if p[1] == 'setpos': #setpos '[' NUMBER NUMBER ']'
        #         p[0] = Command("setpos", {"x": p[3], "y": p[4]})
        #     else: # setxy ':' VAR ':' VAR """
        #         p[0] = Command("setpos", {"x": p[3], "y": p[5]})
        # elif len(p) == 7:  #setpos '[' ':' VAR NUMBER ']'
        #     if p[3] == ':': #setpos '[' ':' VAR NUMBER ']'
        #         p[0] = Command("setpos", {"x": p[4], "y": p[5]})
        #     else: #setpos 'setpos '[' NUMBER ':' VAR ']'
        #         p[0] = Command("setpos", {"x": p[3], "y": p[5]})
        # elif len(p) == 8: #setpos '[' VAR ':' VAR ']'
        #     p[0] = Command("setpos", {"x": p[4], "y": p[6]})
        # elif len(p) == 4: #setxy NUMBER NUMBER
        #     p[0] = Command("setpos", {"x": p[2], "y": p[3]})
        # elif len(p) == 5: #setxy ':' VAR NUMBER
        #     if p[2] == ':':#setxy ':' VAR NUMBER
        #         p[0] = Command("setpos", {"x": p[3], "y": p[4]})
        #     else: #setxy NUMBER ':' VAR
        #         p[0] = Command("setpos", {"x": p[2], "y": p[4]})


    def p_command5(self, p):
        """ command : setx NUMBER 
                    | setx VAR"""
        if isinstance(p[2], str):
            p[0] = Command("setx", p[2][1:])
        else:
            p[0] = Command("setx", p[2])

    def p_command6(self, p):
        """ command : sety NUMBER
                    | sety VAR """
        if isinstance(p[2], str):
            p[0] = Command("sety", p[2][1:])
        else:
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
                    | setpencolor '[' NUMBER NUMBER VAR ']'
                    | setpencolor '[' NUMBER VAR NUMBER ']'
                    | setpencolor '[' NUMBER VAR VAR ']'
                    | setpencolor '[' VAR NUMBER NUMBER ']'
                    | setpencolor '[' VAR NUMBER VAR ']'
                    | setpencolor '[' VAR VAR NUMBER ']'
                    | setpencolor '[' VAR VAR VAR ']' """

        if ':' in p[3]:
            if ':' in p[4] and ':' in p[5]: # var var var
                color = (p[3][1:], p[4][1:], p[5][1:])
            elif ':' in p[4] and ':' not in p[5]: # var var number
                color = (p[3][1:], p[4][1:], p[5])
            elif ':' not in p[4] and ':' not in p[5]: # var number number
                color = (p[3][1:], p[4], p[5])
            else: # var number var
                color = (p[3][1:], p[4], p[5])
            p[0] = Command("pencolor", color)
        else:
            if ':' in p[4] and ':' in p[5]: # number var var
                color = (p[3], p[4][1:], p[5][1:])
            elif ':' in p[4] and ':' not in p[5]: # number var number
                color = (p[3], p[4][1:], p[5])
            elif ':' not in p[4] and ':' not in p[5]: # number number number
                color = (p[3], p[4], p[5])
            else: # number number var
                color = (p[3], p[4], p[5])
            p[0] = Command("pencolor", color)

        # if len(p) == 7: #setpencolor '[' NUMBER NUMBER NUMBER ']'
        #     color = (p[3], p[4], p[5])
        #     p[0] = Command("pencolor", color)
        # elif len(p) == 8:
        #     if p[5] == ':': #setpencolor '[' NUMBER NUMBER ':' VAR ']'
        #         color = (p[3], p[4], p[6])
        #         p[0] = Command("pencolor", color)
        #     elif p[4] == ':': #setpencolor '[' NUMBER ':' VAR NUMBER ']'
        #         color = (p[3], p[5], p[6])
        #         p[0] = Command("pencolor", color)
        #     else: # setpencolor '[' ':' VAR NUMBER NUMBER ']' #8
        #         color = (p[4], p[5], p[6])
        #         p[0] = Command("pencolor", color)
        # elif len(p) == 9:
        #     if p[3] == 'NUMBER': #setpencolor '[' NUMBER ':' VAR ':' VAR ']'
        #         color = (p[3], p[5], p[7])
        #         p[0] = Command("pencolor", color)
        #     elif p[5] == 'NUMBER': #setpencolor '[' ':' VAR NUMBER ':' VAR ']'
        #         color = (p[4], p[5], p[7])
        #         p[0] = Command("pencolor", color)
        #     else: # setpencolor '[' ':' VAR ':' VAR NUMBER ']'
        #         color = (p[4], p[6], p[7])
        #         p[0] = Command("pencolor", color)
        # else: #setpencolor '[' ':' VAR ':' VAR ':' VAR ']'
        #     color = (p[4], p[6], p[8])
        #     p[0] = Command("pencolor", color)
            
    def p_command11(self, p):
        """ command : make VAR NUMBER
                    | make VAR VAR OPERATOR NUMBER
                    | make VAR NUMBER OPERATOR VAR """

        if len(p) == 4:
            p[0] = Command("make", {"make": 1, "var": p[2][1:], "number": p[3]})
        if len(p) == 8:
            if '"' in p[2]:
                p[0] = Command("make", {"make": 2, "var1": p[2][1:], "var2": p[3][1:], "operator": p[4], "number": p[5]})
            else:
                p[0] = Command("make", {"make": 3, "var1": p[2][1:], "number": p[3], "operator": p[4], "var2": p[5][1:]})
    
    def p_command12(self, p):
        """ command : repeat NUMBER '[' program ']' 
                    | repeat VAR '[' program ']' """

        if p[2] == "NUMBER":
            p[0] = Command("repeat", {"repeat": 1, "number": p[2], "code": p[4]})
        else:
            p[0] = Command("repeat", {"repeat": 2, "var": p[2][1:], "code": p[4]})

    def p_command13(self, p):
        """ command : while '[' VAR SIGN NUMBER ']' '[' program ']' """
#                    | while '[' ':' VAR SIGN NUMBER ']' '[' program ']' """ FIXME
        p[0] = Command("while", {'var': p[3][1:], 'sign': p[4], 'number': p[5], 'code': p[8]})

    def p_command14(self, p):
        """ command : if NUMBER SIGN NUMBER '[' program ']'
                    | if VAR SIGN NUMBER '[' program ']'
                    | if  NUMBER SIGN VAR '[' program ']'
                    | if VAR SIGN VAR '[' program ']'
                    | if '[' NUMBER SIGN NUMBER ']' '[' program ']'
                    | if '[' VAR SIGN NUMBER ']' '[' program ']'
                    | if '[' NUMBER SIGN VAR ']' '[' program ']'
                    | if '[' VAR SIGN VAR ']' '[' program ']' """
        if len(p) == 8:
            if ':' in p[2] and ':' in p[4]:
                p[0] = Command("if", {'if':3, 'var1': p[2][1:], 'sign': p[3], 'var2': p[4][1:], 'code': p[6]})
            elif ':' in p[2] and ':' not in p[4]:
                p[0] = Command("if", {'if': 2, 'var': p[2][1:], 'sign': p[3], 'number': p[4], 'code': p[6]})
            elif ':' in p[4]:
                p[0] = Command("if", {'if':2, 'number': p[2], 'sign': p[3], 'var': p[4][1:], 'code': p[6]})
            else:
                p[0] = Command("if", {'if':1, 'number1': p[2], 'sign': p[3], 'number2': p[4], 'code': p[6]})

        else:
            if ':' in p[3] and ':' in p[5]:
                p[0] = Command("if", {'if': 3, 'var1': p[3][1:], 'sign': p[4], 'var2': p[5][1:], 'code': p[8]})
            elif ':' in p[3] and ':' not in p[5]:
                p[0] = Command("if", {'if': 2, 'var': p[3][1:], 'sign': p[4], 'number': p[5], 'code': p[8]})
            elif ':' in p[5]:
                p[0] = Command("if", {'if': 2, 'number': p[3], 'sign': p[4], 'var': p[5][1:], 'code': p[8]})
            else:
                p[0] = Command("if", {'if': 1,'number1': p[3], 'sign': p[4], 'number2': p[5], 'code': p[8]})


    def p_command15(self, p):
        """ command : ifelse NUMBER SIGN NUMBER '[' program ']' '[' program ']'
                    | ifelse VAR SIGN NUMBER '[' program ']' '[' program ']'
                    | ifelse NUMBER SIGN VAR '[' program ']' '[' program ']'
                    | ifelse VAR SIGN VAR '[' program ']' '[' program ']'
                    | ifelse '[' NUMBER SIGN NUMBER ']' '[' program ']' '[' program ']'
                    | ifelse '[' VAR SIGN NUMBER ']' '[' program ']' '[' program ']'
                    | ifelse '[' NUMBER SIGN  VAR ']' '[' program ']' '[' program ']'
                    | ifelse '[' VAR SIGN VAR ']' '[' program ']' '[' program ']' """

        if len(p) == 11:
            if ':' in p[2] and ':' in p[4]:
                p[0] = Command("ifelse", {'ifelse':3, 'var1': p[2][1:], 'sign': p[3], 'var2': p[4][1:], 'code1': p[6], 'code2': p[9]})
            elif ':' in p[2] and ':' not in p[4]:
                p[0] = Command("ifelse", {'ifelse': 2, 'var': p[2][1:], 'sign': p[3], 'number': p[4], 'code1': p[6], 'code2': p[9]})
            elif ':' in p[4]:
                p[0] = Command("ifelse", {'ifelse':2, 'number': p[2], 'sign': p[3], 'var': p[4][1:], 'code1': p[6], 'code2': p[9]})
            else:
                p[0] = Command("ifelse", {'ifelse': 1, 'number1': p[2], 'sign': p[3], 'number2': p[4], 'code1': p[6], 'code2': p[9]})
        else:
            if ':' in p[3] and ':' in p[5]:
                p[0] = Command("ifelse", {'ifelse': 3, 'var1': p[3][1:], 'sign': p[4], 'var2': p[5][1:], 'code1': p[8], 'code2': p[11]})
            if ':' in p[3] and ':' not in p[5]:
                p[0] = Command("ifelse", {'ifelse':2, 'var': p[3][1:], 'sign': p[4], 'number': p[5], 'code1': p[8], 'code2': p[11]})
            elif ':' in p[5]:
                p[0] = Command("ifelse", {'ifelse':2, 'number': p[3], 'sign': p[4], 'var': p[5][1:], 'code1': p[8], 'code2': p[11]})
            else:
                p[0] = Command("ifelse", {'ifelse':1,'number1': p[3], 'sign': p[4], 'number2': p[5], 'code1': p[8], 'code2': p[11]})



    def p_command16(self, p):
        """ command : TO STR VAR '[' program ']' END """
        p[0] = Command("to", {'name': p[2], 'args': p[3], 'code': p[5]})


    def p_varlist(self, p):
        """ varlist : VAR
                    | varlist VAR"""
        if len(p) == 3:
            lst = p[1]
            lst.append(p[2][1:])
            p[0] = lst
        else:
            p[0] = p[1][1:]



    def p_valuelist(self, p):
        """ valuelist :
                    | NUMBER
                    | valuelist NUMBER """
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

