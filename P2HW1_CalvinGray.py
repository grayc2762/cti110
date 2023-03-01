# This program calculates and displays travel expenses
# 28-FEB-2023
# CTI-110P2HW1-Travel Expense
# Calvin Gray

print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter the budget: "))
print()
name = (input("Enter your travel destination: "))
print()
gas = float(input("How much do you think you will spend on gas:"))
print()
Accomodation = float(input("Approximately,how much will you need for Accomodation:"))
print() 
food = float(input("how much do you think you will need for food: "))
print()
print("-"*12,"Travel Expenses",12*"-") 
print("Location:" ,name)
print
print("initial Budget:        $" + str(budget) + "." )
print()
print("Fuel:                 $" + str(gas) + ".")
print("Accomodation:          $" + str(Accomodation) + ".")
print()
print("food:                 $" + str(food) + "." )
print()
balance = budget - gas - food - Accomodation
#print(remaining Balance:" ,Balance)
print("Remaining Balance:   $" + str(gas) + ".") ,format(balance,',.Of') 
