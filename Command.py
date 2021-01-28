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
    r = parser.value(command.args['r'])
    g = parser.value(command.args['g'])
    b = parser.value(command.args['b'])
    color = (r, g, b)
    parser.turtle.PenColor(color)

def do_make(command, parser):
    var = command.args['var']
    left = parser.value(command.args['val1'])

    if len(command.args) == 2: # sem operador
        parser.vars[var] = left
    else: # com operador
        right = parser.value(command.args['val2'])
        operator = command.args['operator']
        operation = {'left': left, 'operator': operator, 'right': right}
        result = parser.value(operation)
        parser.vars[var] = result

def do_repeat(command, parser):
    repeat = parser.value(command.args['value'])
    code = command.args['code']
    i = 0

    while i < repeat:
        Command.exec(code, parser)
        i += 1

def do_while(command, parser):
    code = command.args['code']
    value1 = parser.value(command.args['value1'])
    value2 = parser.value(command.args['value2'])
    sign = command.args['sign']

    if sign == '>':
        while value1 > value2:
            Command.exec(code, parser)
            value1 = parser.value(command.args['value1'])
    elif sign == '<':
        while value1 < value2:
            Command.exec(code, parser)
            value1 = parser.value(command.args['value1'])

# IF | IFELSE
def do_if(command, parser):
    code1 = command.args['code1']
    value1 = parser.value(command.args['value1'])
    value2 = parser.value(command.args['value2'])
    sign = command.args['sign']

    if len(command.args) == 4: # IF
        if try_if(sign, value1, value2) == True:
            Command.exec(code1, parser)
        else:
            print("(Command.py) ERRRRROOUU!!!") # https://www.youtube.com/watch?v=qPl_ToZtDoQ
    else: # IFELSE
        code2 = command.args['code2']

        if try_if(sign, value1, value2) == True:
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
        print("(Command.py) Unkown signal!")

def do_to(command, parser):
    funcname = command.args["name"]
    code = command.args["code"]
    params = command.args["args"]
    parser.funcs[funcname] = {"code": code, "args": params}

def do_call(command, parser):
    funcname = command.args["name"]
    if funcname not in parser.funcs:
        print(f"(Command.py) Unknown function '{funcname}'")
        exit(1)

    params = parser.funcs[funcname]["args"]
    code = parser.funcs[funcname]["code"]
    vals = command.args["args"]

    backup_vars = parser.vars.copy()

    for var, val in zip(params, vals):
        parser.vars[var] = parser.value(val)
    Command.exec(code, parser)
    parser.vars = backup_vars.copy()

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
        "to": do_to,
        "call": do_call,
    }

    def __init__(self, command, args=""):
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
