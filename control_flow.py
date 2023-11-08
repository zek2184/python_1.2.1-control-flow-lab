# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

def vowels_cons():
	letter = input('Enter a letter: ')
	vowels = set(vowels.lower() for vowels in ("a","e","i","o","u"))
	if letter.lower() in vowels:
		print(f'The letter is a vowel {letter}')
	else:
		print(f'The letter is a consonant {letter}')

vowels_cons()

# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.


def phrase_checker():
	while True:
		phrase = input('Enter a phrase(type Q to skip this question): ')
		if phrase.lower() != 'q':
			checker = len(phrase)
			print(f'Len is {checker}')
		elif phrase.lower() == 'q':
			break 
			
phrase_checker() 



# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3


dog_age = input("Enter your dog's age: ")
try: 
	int_age = int(dog_age)
	if int_age <= 2:
		int_age *= 10
		print(f"The dog's age in dog year is {int_age}")
	elif int_age > 2:
		int_age *= 7
		print(f"The dog's age in dog year is {int_age}")
except ValueError:
	print(f'Enter integer value.')


# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
 
print('Enter the lengths of three side of a triangle:')
a = (input('a: '))
b = (input('b: '))
c = (input('c: '))

# Convert str to int
x, y, z = int(a), int(b), int(c)

if (x == y == z):

	msg = "A triangle with sides of %s is a equilateral triangle"
	print_msg = input(msg % (f"{a}, {b}, {c}"))

elif (x == z):
	
        msg = "A triangle with sides of %s is a Isosceles triangle"
        print_msg = input(msg % (f"{a}, {b}, {c}"))

elif (x > y > z) or (x < y < z) :

        msg = "A triangle with sides of %s is a Scalene triangle"
        print_msg = input(msg % (f"{a}, {b}, {c}"))

# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):

limit = 50
count, n = 0, 0
n1, n2 = 0,1 

while count <= limit:
	print(f"term:{count} / number: {n}")
	if n == 0:
		n +=1
	elif n >= 1:
		n_next = n1 + n2
		n1 = n2
		n2 = n_next
		n = n2
	count += 1


# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month  = input('Enter the month of the year (Jan - Dec): ')
day = input('Enter the day of the month: ')
int_day = int(day)
months = set(months.lower() for months in ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"))


if month.lower() in months:
	
	if month.lower() == "dec" and (int_day >= 21 and int_day <=31):
		print(f'{month} {day} is in winter')
	elif month.lower() == "jan":
		print(f'{month} {day} is in winter')
	elif month.lower() == "feb":
		print(f'{month} {day} is in winter')
	elif month.lower() == "mar" and int_day <= 19:
		print(f'{month} {day} is in winter')
	if month.lower() == "mar" and (int_day >= 20 and int_day <=31):
		print(f'{month} {day} is in spring')
	elif month.lower() == "apr":
		print(f'{month} {day} is in spring')
	elif month.lower() == "may":
		print(f'{month} {day} is in spring')
	elif month.lower() == "jun" and int_day <= 19:
		print(f'{month} {day} is in spring')
	if month.lower() == "jun" and (int_day >= 20 and int_day <=31):
		print(f'{month} {day} is in summer')
	elif month.lower() == "jul":
		print(f'{month} {day} is in summer')
	elif month.lower() == "aug":
		print(f'{month} {day} is in summer')
	elif month.lower() == "sep" and int_day <= 21:
		print(f'{month} {day} is in summer')
	if month.lower() == "sep" and (int_day >= 22 and int_day <=31):
		print(f'{month} {day} is in fall')
	elif month.lower() == "oct":
		print(f'{month} {day} is in fall')
	elif month.lower() == "nov":
		print(f'{month} {day} is in fall')
	elif month.lower() == "dec" and int_day <= 20:
		print(f'{month} {day} is in fall')
