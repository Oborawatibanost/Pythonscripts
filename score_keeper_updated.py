#Score Keeper Updated


name = input("What is your name?\n: ")
score = int(input("What is your current score?\n: "))
print(" ")
print(f"Welcome {name}")
print("What would you like to do?")
print(" ")
input_score = int(input("1. Add to your score\n: "))
#Once I learn how, I'm going to add a "display score" input
#I've been wanting to be able to save players, and their scores.
#But I'm not there yet :(

if (input_score == 1):
	previous = int(input("What was your previous score?\n: "))
	print(" ")
	score2 = score + 1
	print(f"{name} Your score is now {score2}")
else:
	print("Please provide a valid input")


