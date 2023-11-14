def main():
    list = [1, 2, 3]
    for range in list:
        guess = player_guess()
        give_feedback(26, guess)

def player_guess():
    return input("Guess a number 1-100: ")

def give_feedback(secret_number, guess):
    if (int(guess) > secret_number):
        print("Lower!")
    if (int(guess) < secret_number):
        print("Higher!")
    if (int(guess) == secret_number):
        print("You Win!")

if __name__ == "__main__":
    main()