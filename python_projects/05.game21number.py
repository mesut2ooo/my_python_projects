import os
import random

# function to get the integer
def get_integer():
	while True:
		try:
			result = int(input())
		except ValueError:
			print("Wrong , Enter again :" , end=" ")
			continue
		else:
			return result


# clearing the screen
os.system('cls' if os.name == 'nt' else 'clear')

# _______PROGRAM STARTS HERE_______
# asking the user for how many players are playing

print("Hi , Welcome to 21 game")
print("The rules are as follows :\n\t 1.Each player have 3 numbers in each turn\n\t 2.Choosing the first person is random\n\t 3.The first player reaches 21 ,loses")
print("Have fun :)")

print("How many players are you (2--6) : " , end="")
while True:
	players_count = get_integer()
	if players_count < 2 or players_count >6:
		print("Wrong , Between 2 and 6 : " , end="")
		continue
	else:
		break

players_names = []
# getting the names of the players
for i in range(players_count):
	players_names.append(input("Enter player number {} : ".format(i+1)))

# randomizing the names
random.shuffle(players_names)

last_number = 0
while last_number < 21:
	for name in players_names:
		while True: # until we get the right number 
			print(name + " , enter 1/2/3 : ")
			number = get_integer()
			if number > 0 and number < 4:
				break
			else: #  the criteria is not met so do it again
				print("Wrong number! , again : " , end="")
				continue
		last_number += number
		os.system('cls' if os.name == 'nt' else 'clear')
		print("result is : {}".format(last_number))
		# losing
		if last_number >= 21:
			looser = name
			break

print(" player {} lost".format(looser))
# getting numbers from each user
# if the first number is less than the previous last number , ask again
# until reaches 21
