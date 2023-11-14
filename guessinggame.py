import random

def main():
    randomnumber()
    again=str(input("Do you want to play again yes/no?"))
    if again == "yes":
        input("Enter a number between 1-100")
    if again == "no":
        print("thank you for playing")
    


def randomnumber():
    random.randint(1,99)
    return()




if __name__ == "__main__":
 main()