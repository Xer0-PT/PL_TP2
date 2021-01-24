# main.py

from Parser import Parser

parser = Parser()

with open("teste.logo", mode="r") as fh:
    contents = fh.read()

parser.Parse(contents)

parser.turtle.file.save()
