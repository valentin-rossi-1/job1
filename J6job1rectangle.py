"""Écrire un programme qui affiche dans la console un rectangle avec des « - »
et des « | » en fonction des paramètres d’entrées, (width, height), par
exemple :
draw_rectangle(10, 3) :
"""

def rectangle(width,height):
        print('|' + '-' * (width - 2) + '|')
        for i in range(height-2):
            print("|" + " "*(width-2) + "|")
        print('|'+'-'*(width-2)+'|')
rectangle (8,3)

def rectangle(width,height):
        print('|' + '-' * (width - 2) + '|')
        for i in range(height-2):
            print("|" + " "*(width-2) + "|")
        if height > 1:
              print("|"+"-"*(width-2)+"|")
rectangle (8,3)
