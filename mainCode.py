import random
def main():
    randNumb = random.randint(1,99)
    list = [1, 2, 3]
    for range in list:
        guess = player_guess()
        give_feedback(randNumb, guess)
    print("The number was " + str(randNumb))

def player_guess():
    return input("Guess a number 1-100: ")

def give_feedback(number, guess):
    if (int(guess) > int(number)):
        print("Lower!")
    if (int(guess) < int(number)):
        print("Higher!")
    if (int(guess) == int(number)):
        print("You Win!")

if __name__ == "__main__":
    main()