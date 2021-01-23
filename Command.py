# Command.py

def go_forward(command, parser):
    length = parser.value(command.args)
    parser.turtle.Forward(length)

def go_backward(command, parser):
    length = parser.value(command.args)
    parser.turtle.Backward(length)

def go_left(command, parser):
    angle = parser.value(command.args)
    parser.turtle.Left(angle)

def go_right(command, parser):
    angle = parser.value(command.args)
    parser.turtle.Right(angle)

def go_setpos(command, parser):
    x = parser.value(command.args['x'])
    y = parser.value(command.args['y'])
    parser.turtle.SetPos(x, y)

def go_setx(command, parser):
    x = parser.value(command.args)
    parser.turtle.SetX(x)
    
def go_sety(command, parser):
    y = parser.value(command.args)
    parser.turtle.SetY(y)

def go_home(command, parser):    
    parser.turtle.Home()

def set_pendown(command, parser):
    parser.turtle.PenDown()

def set_penup(command, parser):
    parser.turtle.PenUp()

def set_pencolor(command, parser):
    color = parser.value(command.args)
    parser.turtle.PenColor(color)

def do_make(command, parser):
    if command.args["make"] == 1:
        var = command.args['var']
        value = parser.value(command.args['number'])
        parser.vars[var] = value
    
    elif command.args["make"] == 2:

        var = command.args['var1'] # variável a ser guardada
        left = parser.value(command.args['var2']) # valor da variável
        right = parser.value(command.args['number'])
        operator = command.args['operator']

        operation = {'left': left, 'operator': operator, 'right': right}

        result = parser.value(operation)
        parser.vars[var] = result

    elif command.args["make"] == 3:
        
        var = command.args['var1'] # variável a ser guardada
        right = parser.value(command.args['var2']) # valor da variável
        left = parser.value(command.args['number'])
        operator = command.args['operator']

        operation = {'left': left, 'operator': operator, 'right': right}

        result = parser.value(operation)
        parser.vars[var] = result


def do_repeat(command, parser):
    code = command.args['code']
    i = 0

    if command.args["repeat"] == 1:
        repeat = parser.value(command.args['number'])
    else:
        repeat = parser.value(command.args['var'])

    while i < repeat:
        Command.exec(code, parser)
        i += 1

def do_while(command, parser):
    code = command.args['code']
    val = parser.value(command.args['var'])
    number = parser.value(command.args['number'])
    sign = command.args['sign']

    if sign == '>':
        while val > number:
            Command.exec(code, parser)
            val = parser.value(command.args['var'])
    elif sign == '<':
        while val < number:
            Command.exec(code, parser)
            val = parser.value(command.args['var'])


def do_if(command, parser):
    code = command.args['code']
    sign = command.args['sign']

    if command.args['if'] == 1:
        number1 = parser.value(command.args['number1'])
        number2 = parser.value(command.args['number2'])

        if try_if(sign, number1, number2) == True:
            Command.exec(code, parser)
        else:
            print("ERRRRROOUU!!!") # https://www.youtube.com/watch?v=qPl_ToZtDoQ

    elif command.args['if'] == 2:
        var = parser.value(command.args['var'])
        number = parser.value(command.args['number'])

        if try_if(sign, var, number) == True:
            Command.exec(code, parser)
        else:
            print("Wrong math!")

    else:
        var1 = parser.value(command.args['var1'])
        var2 = parser.value(command.args['var2'])

        if try_if(sign, var1, var2) == True:
            Command.exec(code, parser)
        else:
            print("Wrong math!")

def do_ifelse(command, parser):
    code1 = command.args['code1']
    code2 = command.args['code2']
    sign = command.args['sign']

    if command.args['ifelse'] == 1:
        number1 = parser.value(command.args['number1'])
        number2 = parser.value(command.args['number2'])

        if try_if(sign, number1, number2) == True:
            Command.exec(code1, parser)
        else:
            Command.exec(code2, parser)

    elif command.args['ifelse'] == 2:
        var = parser.value(command.args['var'])
        number = parser.value(command.args['number'])

        if try_if(sign, var, number) == True:
            Command.exec(code1, parser)
        else:
            Command.exec(code2, parser)

    else:
        var1 = parser.value(command.args['var1'])
        var2 = parser.value(command.args['var2'])

        if try_if(sign, var1, var2) == True:
            Command.exec(code1, parser)
        else:
            Command.exec(code2, parser)

def try_if(sign, val1, val2):
    if sign == '>':
        if val1 > val2:
            return True
    elif sign == '<':
        if val1 < val2:
            return True
    elif sign == '=':
        if val1 == val2:
            return True
    else:
        print("Unkown signal!")

class Command:
    dispatch_table = {
        "forward": go_forward,
        "backward": go_backward,
        "left": go_left,
        "right": go_right,
        "setpos": go_setpos,
        "setx": go_setx,
        "sety": go_sety,
        "home": go_home,
        "pendown": set_pendown,
        "penup": set_penup,
        "pencolor": set_pencolor,
        "make": do_make,
        "repeat": do_repeat,
        "while": do_while,
        "if": do_if,
        "ifelse": do_ifelse,
    }

    def __init__(self, command, args):
        self.name = command
        self.args = args
        
    def __repr__(self):
            return f"Command({self.name}, {self.args})"

    def draw(self, parser):
        self.dispatch_table[self.name](self, parser)

    @classmethod
    def exec(cls, program, parser):
        for command in program:
            command.draw(parser)
