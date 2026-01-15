#this program will calculate the tip based on the bill amount and tip percentage and split the bill among a number of people
print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))
# tip_amount = bill * (tip_percentage / 100)
total_bill = bill * ((tip_percentage/100)+1)
bill_per_person = total_bill / num_people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")   