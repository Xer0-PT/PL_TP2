# main.py

from Parser import Parser
from Svg import SVG

parser = Parser()
svg = SVG()

svg.createFile()

with open("ex3.logo", mode="r") as fh:
    contents = fh.read()

parser.Parse(contents)

svg.saveFile()


# PROF fala sobre o enunciado na aula do dia 11-12-2020
# Sugestão do PROF, posição inicial -> não começar no (0,0)