from random import randint


def higher_lower():
    num = randint(1, 10)

    while True:
        guess = int(input("Choose a number "))
        if guess > num:
            print("Lower!")
        elif guess < num:
            print("Higher!")
        else:
            print("Correct")
            break


if __name__ == "__main__":
    higher_lower()
