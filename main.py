def main():
    generate_random_number()
    guess = player_guess()
    give_feedback(26, guess)
    play_game()

def generate_random_number():
    secret_number = #random number generator code elijah is working on

def player_guess():
    return input("Guess a number 1-100: ")

def give_feedback(secret_number, guess):
    if (int(guess) > secret_number):
        print("Lower!")
    if (int(guess) < secret_number):
        print("Higher!")
    if (int(guess) == secret_number):
        print("You Win!")

def play_game():

#ryan is working on this

if __name__ == "__main__":
    main()