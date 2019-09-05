"""
name_game.py

Translate the input name to the Name song
"""

import sys

while True:

    try:
        name = input("Please type a name: ")
    except EOFError:
        sys.exit(0)

    rest = name[1:]
    nameGame = name + "," + name + ",bo-b" + rest + "\n"
    nameGame += "Banana-fana fo-f" + rest + "\n"
    nameGame += "Fee-fi-mo-m" + rest + "\n"
    nameGame += name + "!!"
    print(nameGame)
