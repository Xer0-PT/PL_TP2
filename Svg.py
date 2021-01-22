# svg.py

#import ply.lex as lex

class SVG:
    
    def __init__(self):
        self.filename = "teste.svg"

    def createFile(self):
        fh = open(self.filename, mode="w")
        with fh:
            print('<svg>\n', file=fh)

    def saveFile(self):
        fh = open(self.filename, mode="a")
        with fh:
            print('</svg>', file=fh)        

    def addLine(self, x1, y1, x2, y2):
        fh = open(self.filename, mode="a")
        with fh:
            print(f"""\n<line x1="{x1}" y1="{y1}"
                            x2="{x2}" y2="{y2}"
                            style="stroke: rgb(0, 0, 0);
                            stroke-width: 1px"/>""", file=fh)
