import sys

instructions = "How many times have Liverpool been European Champions? You get 5 attempts"

print(instructions)
i = 0
while  i <= 4:
    guess = input("Go ahead: ")
    n = int(guess)
    if n == 6:
        print("Correct!")
        for i in range(9):
            print("You'll Never Walk Alone")
        sys.exit(0)
    print("Wrong")
    i += 1 
print("The correct answer is 6.")
sys.exit(0)
