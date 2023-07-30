"""
    This is a hangman game
    the player have 6 guesses to find the desires word
    if not
    sorry the poor person is going to die
"""

import os
import random
import time

# drawing the template and the dieing man
def Hanging_Template(status = 0):
    os.system("cls") # first clearing the screen and the followings are stages
    if status == 0:
        print("*******************************")
        print("**                           **")
        print("**                           **")
        print("**                           **")
        print("**                           **")
        print("**                           **")
        print("**                           **")
        print("*******************************")

    elif status == 1:
        print("*******************************")
        print("**                           **")
        print("**                           **")
        print("**                           **")
        print("**                           **")
        print("**                           **")
        print("**     |||||                 **")
        print("*******************************")

    elif status == 2:
        print("*******************************")
        print("**                           **")
        print("**                           **")
        print("**                           **")
        print("**                           **")
        print("**   __________              **")
        print("**    ||||||                 **")
        print("*******************************")

    elif status == 3:
        print("*******************************")
        print("**                           **")
        print("**      ||                   **")
        print("**      ||                   **")
        print("**      ||                   **")
        print("**   ___||_____              **")
        print("**    ||||||                 **")
        print("*******************************")

    elif status == 4:
        print("*******************************")
        print("**      ____________         **")
        print("**      ||                   **")
        print("**      ||                   **")
        print("**      ||                   **")
        print("**   ___||_____              **")
        print("**    ||||||                 **")
        print("*******************************")

    elif status == 5:
        print("*******************************")
        print("**      ____________         **")
        print("**      ||                   **")
        print("**      ||         0         **")
        print("**      ||       --|--       **")
        print("**   ___||_____   /_\        **")
        print("**    ||||||      |||        **")
        print("*******************************")

    elif status == 6:
        print("*******************************")
        print("**      ____________         **")
        print("**      ||         |         **")
        print("**      ||         0         **")
        print("**      ||       --|--       **")
        print("**   ___||_____    /\   _    **")
        print("**    ||||||           //_   **")
        print("*******************************")
    
    else:
        print("wrong input!")

# the category menu
def Menu():
    os.system("cls")
    print("choose a category by typing it's number : ")
    print("******************")
    print("* 1.IT           *") 
    print("* 2.Automobiles  *")
    print("* 3.Appliances   *")
    print("* 4.Books        *")
    print("* 5.Movies       *")
    print("* 6.TV Shows     *")
    print("******************")
    print(">> " , end="")
    return Get_Integer()

# getting the integer between 1 and 6
def Get_Integer():
    while True:
        try:
            result =int(input())
        except ValueError:
            print("Error, input a number (1-6) >>  " , end="")
            continue
        
        if result <= 0 or result > 6:
            print("No, between 1 adn 6 >>  " , end="")
            continue
        else:
            return result

#to get a single char and turn it to upper
def Get_Char():
    while True:
        char = input()
        if len(char) > 1:
            print("please enter a  single character >> " , end="")
            continue
        elif len(char) == 0:
            print("You've enterd nothing >> " , end="")
            continue
        elif not char.isalpha():
            print("This is a number , we want a charcter >> " , end="")
            continue
        else:
            return char.upper()
       
# finding the random word by category number
def Random_Word(category_number):
    if category_number == 1:
        return random.choice(Word.it)
    elif category_number == 2:
        return random.choice(Word.automobile)
    elif category_number == 3:
        return random.choice(Word.appliance)
    elif category_number == 4:
        return random.choice(Word.books)
    elif category_number == 5:
        return random.choice(Word.movies)
    elif category_number == 6:
        return random.choice(Word.TV_shows)
    
# hidden is "----- ------" and the shown is "HARRY POTTER" and entered_char is "T" so the result will be "----- --TT--"
def New_Hidden_Word(shown="" , hidden="" , entered_char=""):
    # turn them into list so we can change them
    result = list(hidden)
    shown = list(shown)

    if entered_char not in shown:
        return "".join(result)
    else:
        while True:
            try:
                result[shown.index(entered_char)] = entered_char # replacing the first occurence
                shown[shown.index(entered_char)] = "-" #deleting the first occurence in original word
            except ValueError:
                break

        return "".join(result)
        
# a class for words , like a database
class Word:
    it = ['IOS', 'CRYPTO', 'ALGORITHM', 'DEVELOPER', 'ANDROID', 'GOOGLE', 'WINDOWS', 'BIG DATA', 'ARTIFICIAL INTELLIGENCE', 'LAPTOP', 'PC', 'CYBERSECURITY', 'BLOCKCHAIN', 'MACHINE LEARNING', 'CLOUD', 'VIRTUAL REALITY', 'LINUX', 'WIKIPEDIA', 'MAC', 'BLURAY', 'WEB', 'INTERNET OF THINGS', 'CODING', 'PHONE', 'INTERNET', 'HARD DRIVE', 'PYTHON', 'DVD', 'SSD']
    automobile = ['BUMPER', 'EXHAUST', 'BODY', 'CLUTCH', 'TIRE', 'FUEL FILTER', 'AXLE', 'IGNITION', 'CAMSHAFT', 'TIMING BELT', 'VALVE', 'ALTERNATOR', 'CHASSIS', 'TRUNK', 'DIFFERENTIAL', 'SUSPENSION', 'GAUGES', 'RADIATOR', 'CRANKSHAFT', 'FUEL PUMP', 'FENDER', 'CARBURETOR', 'ENGINE', 'AIR FILTER', 'TURN SIGNAL', 'STEERING', 'OIL FILTER', 'HOOD', 'WHEEL', 'DASHBOARD', 'BRAKES', 'TAILLIGHT', 'GRILLE', 'MIRROR', 'PISTON', 'GEARBOX', 'CYLINDER', 'TRANSMISSION', 'SPARK PLUG', 'HEADLIGHT', 'BATTERY']
    appliance = ['ESPRESSO MACHINE', 'HUMIDIFIER', 'COFFEE MAKER', 'CURLING IRON', 'ELECTRIC TOOTHBRUSH', 'TOASTER', 'GRILL', 'REFRIGERATOR', 'ELECTRIC SKILLET', 'DISHWASHER', 'OVEN', 'JUICER', 'PRESSURE COOKER', 'MIXER', 'ELECTRIC KNIFE', 'VACUUM CLEANER', 'DEHUMIDIFIER', 'FAN', 'RICE COOKER', 'ELECTRIC CAN OPENER', 'BLENDER', 'FONDUE POT', 'HEATER', 'STOVE', 'MICROWAVE', 'DEEP FRYER', 'HAIR DRYER', 'WAFFLE MAKER', 'WASHING MACHINE', 'AIR FRYER', 'DRYER', 'AIR CONDITIONER', 'ELECTRIC KETTLE', 'ELECTRIC GRILL', 'BREAD MAKER', 'POPCORN MAKER', 'IRON', 'FOOD PROCESSOR', 'SLOW COOKER']
    books = ['THE COUNT OF MONTE CRISTO', 'MACBETH', 'THE SUN ALSO RISES', 'HARRY POTTER AND THE PHILOSOPHERS STONE', 'LES MISERABLES', 'THE GREAT GATSBY', 'HARRY POTTER AND THE GOBLET OF FIRE', 'THE PICTURE OF DORIAN GRAY', 'THE ODYSSEY', 'THE OLD MAN AND THE SEA', 'BRAVE NEW WORLD', 'THE DIVINE COMEDY', 'CRIME AND PUNISHMENT', 'ANIMAL FARM', 'ROMEO AND JULIET', 'DON QUIXOTE', 'THE HITCHHIKERS GUIDE TO THE GALAXY', 'THE CANTERBURY TALES', 'THE BROTHERS KARAMAZOV', 'THE STRANGER', 'KING LEAR', 'HARRY POTTER AND THE DEATHLY HALLOWS', 'PRIDE AND PREJUDICE', 'THE ILIAD', 'THE SOUND AND THE FURY', 'HARRY POTTER AND THE ORDER OF PHOENIX', 'THE TRIAL', 'THE METAMORPHOSIS', 'THE DIARY OF ANNE FRANK', 'PARADISE LOST', 'THE COLOR PURPLE', 'THE LORD OF THE RINGS', 'THE BOOK THIEF', 'ONE HUNDRED YEARS OF SOLITUDE', 'HARRY POTTER AND THE HALF BLOOD PRINCE', 'TO THE LIGHTHOUSE', 'THE CATCHER IN THE RYE', 'A CLOCKWORK ORANGE', 'THE AENEID', 'HARRY POTTER AND THE PRISONER OF AZKABAN', 'HAMLET', 'THE IDIOT', 'WAR AND PEACE', 'THE PRINCESS BRIDE', 'HARRY POTTER AND THE CHAMBER OF SECRETS', 'TO KILL A MOCKINGBIRD']
    movies = ['THE DARK KNIGHT', 'THE LION KING', 'THE MATRIX', 'THE AVENGERS', 'THE THING', 'CITY OF GOD', 'THE TERMINATOR', 'APOCALYPSE NOW', 'THE FLY', 'THE GREEN MILE', 'INCEPTION', 'THE SHAWSHANK REDEMPTION', 'GLADIATOR', 'SAVING PRIVATE RYAN', 'SCHINDLERS LIST', 'PREDATOR', 'GUARDIANS OF THE GALAXY', 'DOCTOR STRANGE', 'THE DARK KNIGHT RISES', 'JUSTICE LEAGUE', 'BATMAN BEGINS', 'THOR', 'THE SILENCE OF THE LAMBS', 'THE RAID', 'SEVEN SAMURAI', 'ALIEN', 'FORREST GUMP', 'THE USUAL SUSPECTS', 'THE PRESTIGE', 'INTERSTELLAR', 'STAR WARS', 'PULP FICTION', 'ALIENS', 'OCEANS ELEVEN', 'THE INCREDIBLE HULK', 'AVATAR', 'OCEANS THIRTEEN', 'WONDER WOMAN', 'GOODFELLAS', 'THE DIRTY DOZEN', 'FIGHT CLUB', 'IRON MAN', 'THE PIANIST', 'PANS LABYRINTH', 'THE GODFATHER', 'DIE HARD', 'OCEANS TWELVE', 'THE DEPARTED', 'LIVE FREE OR DIE HARD', 'JAWS', 'SEVEN', 'AMERICAN HISTORY X']
    TV_shows = ['THE OFFICE', 'VEEP', 'SEX AND THE CITY', 'THE AMERICANS', 'GAME OF THRONES', 'BUFFY THE VAMPIRE SLAYER', 'NARCOS', 'THE MARVELOUS MRS MAISEL', 'BREAKING BAD', 'STRANGER THINGS', 'THE CROWN', 'BOARDWALK EMPIRE', "THE HANDMAID'S TALE", 'THE WIRE', 'THE BIG BANG THEORY', 'CURB YOUR ENTHUSIASM', 'MAD MEN', 'THE SOPRANOS', 'HOUSE OF CARDS', 'THE WEST WING', 'THE WALKING DEAD', 'WESTWORLD', 'THE GOOD PLACE', 'ITS ALWAYS SUNNY IN PHILADELPHIA', 'THE SIMPSONS', 'HOMELAND', 'BLACK MIRROR', 'THE QUEENS GAMBIT', 'BETTER CALL SAUL', "THE QUEEN'S GAMBIT", 'THE HANDMAIDS TALE', 'ORANGE IS THE NEW BLACK', 'LOST', 'FRIENDS', 'TRUE DETECTIVE', 'TWIN PEAKS']

#starting the program and choosing the category
print("Welcome to this game\nchoose a category and you have 6 guess to prevent the poor guy from hanging by a cruel king")

# making the random guess word and it's hidden version
flag = True
while flag:
    guess_word = Random_Word(Menu())
    hidden_word = []
    for i in guess_word:
        if i == " ":
            hidden_word.append(" ")
        else:
            hidden_word.append("-")
    hidden_word = "".join(hidden_word)
    entered_characters = []
    state = 0
    right_guesses = 6

    while True:
        if hidden_word == guess_word or right_guesses == 0:
            break
        # printing the template and the scene
        Hanging_Template(state)
        
        # printing the entered characters and the hidden word
        print(hidden_word)
        print("Up until now , you've entered : " , end="")
        for char in entered_characters:
            print(char , end=" ")
        print()

        # getting the character from the user
        print("You have {} guesses left >> ".format(right_guesses) , end="")
        entered_characters.append(Get_Char())

        # if the entered character is in the word
        if entered_characters[-1] in guess_word:
            print(":) RIGHT")
            hidden_word = New_Hidden_Word(guess_word , hidden_word , entered_characters[-1])
            time.sleep(2)

        # if the hidden character is not in the word
        else:
            print("!! WRONG CHARACTER")
            right_guesses -= 1
            state += 1
            time.sleep(2)
        
    if hidden_word == guess_word:
        Hanging_Template(state)
        print("Yeah you've done it , congrats")
    else:
        Hanging_Template(6)
        print("Sorry the poor guy died because of you")
        print("The word was {}".format(guess_word))

    #going another round or not
    print("You wanna play again (y/n) : " , end="")
    while True:
        yes_or_no = input()

        if yes_or_no == "y":
            print("OK , let's go buddy")
            flag = True
            break
        elif yes_or_no == "n":
            print("Hope to see you soon")
            flag = False
            break
        else :
            print("You've entered wrong character")

