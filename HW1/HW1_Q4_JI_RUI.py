# Rui Ji
# ITP 449
# HW1
# Question 4

# Write a program that prompts the user to enter a loan amount, annual interest rate, and number of years for a car
# loan. Then it prints the monthly payment amount.
# Loan Amount: 30000.00
# Annual Interest Rate: 4.00
# Years: 5
# Your monthly payment is: $552.50

loan = float(input("Loan Amount:"))
annualInterestRate = float(input("Annual Interest Rate:"))
monthlyInterestRate = annualInterestRate/12.0;
years = float(input("Years:"))

pmt_up = loan * (monthlyInterestRate/100) * (pow((1 + monthlyInterestRate/100.0), (years * 12)))
pmt_down = pow((1 + monthlyInterestRate/100.0), (years * 12)) - 1

result = pmt_up / pmt_down

print("Your monthly payment is:" + str(round(result, 2)))
