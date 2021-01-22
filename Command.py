# Command.py

#from Turtle import Turtle


def go_forward(command, parser):
    length = parser.value(command.args)
    parser.turtle.Forward(length)
    

class Command:
    # Dispatch Table!
    dispatch_table = {
        "forward": go_forward,
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
