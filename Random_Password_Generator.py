# It is 07/02/2021 - I created this code very, very early on in my Python learning.
# Most of this code is from other people - sorry - and it doesn't even really work how I want it.
# All code from this script on is written completely 100% by me.
# I'm keepeing this up just to show where I was at

import random
import array

Max_len = 5

Digits = ["0" "1" "2" "3" "4" "5" "6" "7" "8" "9"]

Lowercase = ["a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p" "q" "r" "s" "t" "u" "v" "w" "x" "y" "z"]

Uppercase = ["A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N" "O" "P" "Q" "R" "S" "T" "U" "V" "W" "X" "Y" "Z"]

Symbols = ["!" "@" "#" "$" "%" "^" "&" "*" "(" ")" "`" "~" "-" "_" "+" "=" "[" "]" "{" "}" "|"]

Combined = Digits + Lowercase + Uppercase + Symbols

rand_digit = random.choice(Digits)
rand_upper = random.choice(Uppercase)
rand_lower = random.choice(Lowercase)
rand_symbol = random.choice(Symbols)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

for x in range(Max_len - 4):
	temp_pass = temp_pass + random.choice(Combined)
	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)

password = ""

for x in temp_pass_list:
	password = password + x
print(password)
