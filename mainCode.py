import random
def main():
    playagain()

def playagain():
    randNumb = random.randint(1,99)
    list = [1, 2, 3]
    for range in list:
        guess = player_guess()
        give_feedback(randNumb, guess)
    print("The number was " + str(randNumb))
    restart()

def player_guess():
    return input("Guess a number 1-100: ")

def give_feedback(number, guess):
    if (int(guess) > int(number)):
        print("Lower!")
    if (int(guess) < int(number)):
        print("Higher!")
    if (int(guess) == int(number)):
        print("You Win!")
        if (input("Would you like to play again? ") == "yes"):
            print("play again")
            playagain()
        if (input("Would you like to play again? ") == "no"):
            print("bye")

def restart():
    restartVar = input("Would you like to play again? ")
    if (restartVar == "yes"):
        playagain()
    elif (restartVar == "no"):
        print("Adios!")
    else:
        print("?")
        restart()

if __name__ == "__main__":
    main()