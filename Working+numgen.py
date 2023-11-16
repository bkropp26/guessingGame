import random
def main():
    playagain()
    randomnumber()
def playagain():
    restartVar = "yes"
    secretnumber = randomnumber()
    list = [1, 2, 3]
    while restartVar == "yes":
        for range in list:
            guess = player_guess()
            give_feedback(secretnumber, guess)
        print("The number was " + str(secretnumber))
        restartVar = input("Would you like to play again? ")

def player_guess():
    return input("Guess a number 1-100: ")


def randomnumber():
    return(random.randint(1,99))

def give_feedback(randomnumber, guess):
    if (int(guess) > int(randomnumber)):
        print("Lower!")
    if (int(guess) < int(randomnumber)):
        print("Higher!")
    if (int(guess) == int(randomnumber)):
        print("You Win!")
        if (input("Would you like to play again? ") == "yes"):
            print("play again")
            playagain()
        if (input("Would you like to play again? ") == "no"):
            print("bye")

if __name__ == "__main__":
    main()