# main.py

from Parser import Parser


parser = Parser()

# Fazer um for para ler vário ficheiros FIXME

with open("teste.logo", mode="r") as fh:
    contents = fh.read()

parser.Parse(contents)

parser.turtle.file.save()

# PROF fala sobre o enunciado na aula do dia 11-12-2020
# Sugestão do PROF, posição inicial -> não começar no (0,0)