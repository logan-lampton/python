import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

number_of_names = len(names)
random_number = random.randint(0, number_of_names - 1)
random_name = names[random_number]

print(f"{random_name} is going to buy the meal today!")