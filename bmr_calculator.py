weight = int(input("What is your weight in kg?: "))
height = int(input("What is your height in cm?: "))
age = int(input("What is your age? "))

bmr = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
sedentary = bmr * 1.2
lightly_active = bmr * 1.375
moderately_active = bmr * 1.55
active = bmr * 1.725
very_active = bmr * 1.9

print(f"Your BMR is {bmr}\n")
print("BMR is how many calories your body needs to maintain your current weight.")
print("However, to get a more accurate reading we need to calculate your AMR")
print("How active are you?")
activity_level = int(input(("1. Sedentary\n2. Lightly Active\n3. Moderately Active\n4. Active\n5. Very Active\n: ")))
print(" ")
goal = int(input("What is your goal?\n1. Gain weight\n2. Lose weight\n: "))
print(" ")

if (activity_level == 1):
	print(f"Your AMR is {sedentary}")
	print("You are sedentary. Consider upping your physical activity")
	print(" ")
	goal
	if (goal == 1):
		user_calories = int(input("How many calories have you had so far today?\n: "))
		print(" ")
		if (user_calories > sedentary):
			print("Good job, your are on track to meet your goals!")
		else:
			print("Consider upping your calorie intake. Remember, calories in calories out")
	elif (goal == 2):
		user_calories = int(input("How many calories have you had so far today?\n: "))
		print(" ")
		if (user_calories < sedentary):
			print("You're on the right track. Make sure to stay under your AMR")
		else:
			print("You're over your AMR, try to limit your calorie intake. Remember, calories in calories out")


elif (activity_level == 2):
	print(f"Your AMR is {lightly_active}")
	print("You are lightly active.")
	print("This means you do light exercise 1-2 times per week.")
	print("Consider upping your physical activity.")
	print(" ")
	goal
	if (goal == 1):
		user_calories = int(input("How many calories have you had so far today?\n: "))
		print(" ")
		if (user_calories > lightly_active):
			print("Good job, your on track to meet your goals. Just dont eat too much")
		else:
			print("Consider upping your calorie intake. Remember calories in calories out")
	elif (goal == 2):
		user_calories = int(input("How many calories have you had so far today?\n: "))
		print(" ")
		if (user_calories < lightly_active):
			print("You're over your AMR, try to limit your calorie intake. Remember, calories in calories out")


elif (activity_level == 3):
	print(f"Your AMR is {moderately_active}")
	print("You are moderately active")
	print("This means you do moderate physical activity 3-4 times per week.")
	print("You have a good amount of physical activity!")
	print(" ")
	goal
	if (goal == 1):
		user_calories = int(input("How many calories have you had so far today?\n: "))
		print(" ")
		if (user_calories > moderately_active):
			print("Good job, your on track to meet your goals. Just dont eat too much")
		else:
			print("Consider upping your calorie intake. Remember calories in calories out")
	elif (goal == 2):
		user_calories = int(input("How many calories have you had so far today?\n: "))
		print(" ")
		if (user_calories < moderately_active):
			print("You're over your AMR, try to limit your calorie intake. Remember, calories in calories out")


elif (activity_level == 4):
	print(f"Your AMR is {active}")
	print("You are active")
	print("This means you maintain a solid amount of physical activity")
	print("Good job!")
	print(" ")
	goal
	if (goal == 1):
		user_calories = int(input("How many calories have you had so far today?\n: "))
		print(" ")
		if (user_calories > active):
			print("Good job, your on track to meet your goals. Just dont eat too much")
		else:
			print("Consider upping your calorie intake. Remember, calories in calories out")
	elif (goal == 2):
		user_calories = int(input("How many calories have you had so far today?\n: "))
		print(" ")
		if (user_calories < active):
			print("You're over your AMR, try to limit your calorie intake. Remember, calories in calories out")


elif (activity_level == 5):
	print(f"Your AMR is {very_active}")
	print("You are very active")
	print("Great job!")
	print(" ")
	goal
	if (goal == 1):
		user_calories = int(input("How many calories have you had so far today?\n: "))
		print(" ")
		if (user_calories > very_active):
			print("Good job, your on track to meet your goals. Just dont eat too much")
		else:
			print("Consider upping your calorie intake. Remember calories in calories out")
	elif (goal == 2):
		user_calories = int(input("How many calories have you had so far today?\n: "))
		print(" ")
		if (user_calories < very_active):
			print("You're over your AMR, try to limit your calorie intake. Remember, calories in calories out")

else:
	print("Please provide a valid input")





