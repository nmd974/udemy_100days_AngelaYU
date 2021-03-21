print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill ? $"))
people_number = int(input("How many people to split the bill ?"))
percentage = int(input("What percentage tip would you like to give ?"))

calcul = (total_bill/people_number) + ((total_bill/people_number)*(percentage/100))

print(f"Each people have to paid : {round(calcul, 2)}")