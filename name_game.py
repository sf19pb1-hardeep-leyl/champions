"""
name_game.py

Translate the input name to the Name song
"""

import sys

while True:

    try:
        word = input("Please type a name: ")
    except EOFError:
        sys.exit(0)

    rest = word[1:]
    nameGame = word + "," + word + ",bo-b" + rest + "\n"
    nameGame = nameGame + "Banana-fana fo-f" + rest + "\n"
    nameGame = nameGame + "Fee-fi-mo-m" + rest + "\n"
    nameGame = nameGame + word + "!!"
    print(nameGame)
