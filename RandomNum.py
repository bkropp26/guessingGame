import random

def main():  
    list = [1, 2, 3]
    for range in list:
        Ran = randomnumber()
        guess = player_guess()
        give_feedback(26, guess)


def randomnumber():
    return(random.randint(1,99))

def player_guess():
    return input("Guess a number 1-100: ")

def give_feedback(num, guess):
    if (int(guess) > num):
        print("Lower!")
    if (int(guess) < num):
        print("Higher!")
    if (int(guess) == num):
        print("You Win!")



if __name__ == '__main__':
    main()