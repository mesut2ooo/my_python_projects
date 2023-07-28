import math
import random

# to get the limits of the range and calculating the guessing counts
def take_bounds():
    while True:
        #if user enters anything but integers
        while True:
            try:
                upper_bound = int(input("Enter the upper range :  "))
                lower_bound = int(input("Enter the lower range :  "))
            except ValueError:
                print("What you've entered is not a base 10 integer , try again")
            except Exception:
                print("oop's, i dont know, something went wrong , try again : ")
            else:
                break
        
        #upper bound must be more than lower bound
        if upper_bound < 0 or lower_bound < 0:
            print("The numbers shouldn't be negative , try again")
        elif upper_bound < lower_bound:
            print("upper range should be less than lower range , try again")
            continue
        elif lower_bound == upper_bound:
            print("lower and upper ranges should not be equal , try again")
            continue
        elif upper_bound-lower_bound == 1:
            print("This is ridiculus , there is no number between those , what's you wanna guess , enter again")
        else: # everything is alright
            break
    
    # how many counts user have
    guess_counts = round(math.ceil(math.log2(upper_bound - lower_bound)))
    return upper_bound , lower_bound , guess_counts #this function , returns 3 integers

# for taking an integer
def take_int():
    while True:
        try:
            result = int(input())
        except ValueError:
            print("This isn't a number , again : ")
        else:
            return result
    
#for taking y or n characters
def take_char():
    while True:
            char = input()
            if char == "y":
                return True
            elif char == "n":
                return False
            else:
                print("y or n : ")

print("***********************\n"+"Welcome to my guessing game")
#flags from round 2
same_bounds_again = False

while True:
    if not same_bounds_again:
        #taking the data that we need
        upper , lower , guesses = take_bounds()
    random_number = random.randint(lower , upper) # making up a random integer

    print("So , you have {} guesses: ".format(guesses))

    # take the guesses and win or loose
    for counter in range(1 , guesses+1):
        print("guess the number between {} and {} :  ".format(lower , upper))
        guessed_number = take_int()

        if guessed_number == random_number:
            print("$ $ $ $ $ $ $\nThat's right , you won\n$ $ $ $ $ $ $")
            print("That's maybe a pure luck ,You wanna give it another shot (y/n) : ")
            break
        elif guessed_number > random_number:
            print("************\nYou guessed high")
        else:
            print("************\nYou guessed small")
        print("************\nDude, you have {} shots left".format(guesses-counter))
    else:
        print("You've lost baby!!!! , the number was {}".format(random_number))
        print("haha , You wanna play again looser (y/n) :  ")

    #going another round or not
    yes_or_no = take_char()

    if yes_or_no:
        print("OK , let's go buddy")
        print("you want the same bounds?")
        same_bounds_again = take_char()
    else:
        print("Hope to see you soon")
        break
