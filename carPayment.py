"""
Program: carPayment.py 
Author: Russ

Compute car payment. 

Inputs:
    1. Loan amount
    2. down payment
    3. sales tax % 
    4. annual percentage rate 
    5. term of car loan in years 

Outputs: 
    1. Monthly payments 
    2. Total interest amount 
    3. Total loan amount
    4. Yearly Amortization Schedule
"""

# Accept the inputs
carAmount = int(input("Enter the price of the car: $"))
downPayment = int(input("Enter the downpayment: $"))
salesTax = float(input("Enter sales tax %: "))
annualPercent = float(input("Enter the annual percentage rate: "))
years = int(input("Enter the term of car loan in years: "))

# Compute the results
taxPercent = salesTax / 100
ratePercent = annualPercent / 100
months = years * 12 
totalLoan = (carAmount *( 1 + taxPercent )) - downPayment
monthlyPayments = (totalLoan * (ratePercent / 12 )) / ( 1 - ( 1 + ratePercent / 12 ) **  -months)
totalAmount = monthlyPayments * months
totalInterestCost = totalAmount - totalLoan 

# Display the results 
print("")
print("Your monthly payments will be: $", round(monthlyPayments,2))
print("Your total interest will be: $", round(totalInterestCost, 2))
print("The total cost for the loan will be: $", round(totalAmount, 2))

# Display the header for the table
print("")
print("     Yearly Amortization Schedule")
print("%4s%18s%18s" % ("Year", "Mothly Payment" ,"Total Balance"))

# Compute and display the results for each year 
for year in range(1, years + 1):
    balance = totalAmount - (monthlyPayments * 12)
    print("%3d%18.2f%15.2f" % \
        (year, monthlyPayments, balance))	
    totalAmount = balance + 0
    balance -= (monthlyPayments * 12)
    
