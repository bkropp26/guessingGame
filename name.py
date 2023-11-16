import random

def main():  
    randomnumber(random.randint(1,99))
    guess = input

def randomnumber(GenerateRandom):
    input("Guess Number 1-100")
import random

def main():  
    randomnumber(random.randint(1,99))


def randomnumber(GenerateRandom):
    input("User 1 Guess Number 1-100")
    if (int(guess) == GenerateRandom):
        print("Right on!")
    if(int(guess) > GenerateRandom):
        print("To high!")
    if(int(input) < GenerateRandom):
        print("To Low!")
    else:
        print(GenerateRandom + "Play again?")
    



if __name__ == '__main__':
    main()