my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)]     #range(5) is list = [0,1,2,3,4]

multiply_list = [x * 3 for x in range(5)]
print(multiply_list)

print([n for n in range(10) if n%2 == 0])

people_you_know = ["Rolf", " John", " RINA "]
noramlize_people = [ person.strip().lower() for person in people_you_know]
print(noramlize_people)