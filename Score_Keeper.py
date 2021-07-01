print("This is a score keeper\n")


print("1. Add to my score") 
print("2. Display your score\n")
display = int(input("What Would you like to do?\n")) 

# players = [1,2,3,4]
# scores = [1,2,3,4,5,6,7,8,9]

message7 = "Which player are you?\n"


player_number = int(input("Which player are you?\n"))

if (display == 1):
	player_number
elif (display == 2):
	input(message7)
else:
	player_number




message = f"Welcome Player {player_number}!\n"
print(message)
score = input("Did you Score?\n")
message2 = "Good Job!\n"
message3 = "That sucks\n"
message4 = 'Invalid Input: Please input "Yes" or "No"'
message5 = int(input("What was your previous score? \n"))

if (score == "Yes"):
	print(message2)
	message5
	print(f"Your score is now {message5 + 1}")
elif (score == "No"):
	print(message3)
else:
	print(message4)














