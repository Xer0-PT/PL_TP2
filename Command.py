# Command.py

#from Turtle import Turtle


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

def do_make_1(command, parser):
    var = command.args['var']
    value = parser.value(command.args['number'])
    parser.vars[var] = value

def do_make_2(command, parser):
    var1 = command.args['var1']
    var2 = command.args['var2']
    op = command.args['operator']
    value = parser.value(command.args['number'])
    for i, var1 in parser.vars[]:
        

    parser.vars[var] = value


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
        "make_1": do_make_1,
        "make_2": do_make_2,
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
