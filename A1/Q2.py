import os
from random import randint

if __name__ == "__main__":
    while True:
        os.system("clear")

        dice_num = randint(1, 6)
        print("You rolled a", dice_num)

        user_inp = input("Enter q to quit!\n")
        if user_inp.lower() == "q":
            break

    print("Thanks for playing!")
