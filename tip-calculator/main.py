print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill?"))
percentage = (int(input("What percentage tip would you like to give? 10, 12, 18, or 20?"))) / 100
number_of_people = int(input("How many people to split the bill?"))
portion_of_bill = total_bill / number_of_people
tip = portion_of_bill * percentage
total_per_person = portion_of_bill + tip
final_payment_per_person = "{:.2f}".format(total_per_person)
print(f"Each person should pay ${final_payment_per_person}")