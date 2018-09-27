def who_do_you_know():
	people = input("Enter the names of people you know, separated by commas:")
	people_list = people.split(",")
	# people_without_spaces = []
	# for person in people_list:
	# people_without_spaces.append(person.strip())
	people_without_spaces = [person.strip() for person in people_list]
	
	return  people_without_spaces

def ask_user():
	person = input("Enter a name of someone you know: ")
	if person in who_do_you_know():
		print("You know {}!".format(person))

ask_user()