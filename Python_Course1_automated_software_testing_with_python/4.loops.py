myvariable = "hello"

for character in myvariable:   #iterables are strings, list, tuples
	print(character)

my_list = [1,3,5,7,9]

for number in my_list:
	print(number ** 2)  #power of 2 = Square of number


user_wants_number = True
while user_wants_number == True:
	print(10)

	user_input=input("Should we print again? (y/n) ")
	if user_input == 'n':
		user_wants_number = False



