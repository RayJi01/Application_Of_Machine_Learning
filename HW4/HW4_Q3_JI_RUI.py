# Rui Ji
# ITP 449
# HW4
# Q2
import numpy as np
import matplotlib.pyplot as plt

# Write a program that prompts the user to enter a loan amount , interest rate , and number of years for a car loan.
# Then it prints the monthly payment amount. Loan Amount: 30000.00 Annual Interest Rate: 4.00 Years: 5 Your monthly
# payment is: $552.50 Now plot the monthly subplots. interest paid vs month as well as the principal balance vs month

# ----------------------------Refer to my own HW1 Solutions for this part----------------------------------------------#
loan = float(input("Loan Amount:"))
annualInterestRate = float(input("Annual Interest Rate:"))
monthlyInterestRate = annualInterestRate / 12.0;
years = float(input("Years:"))

pmt_up = loan * (monthlyInterestRate / 100) * (pow((1 + monthlyInterestRate / 100.0), (years * 12)))
pmt_down = pow((1 + monthlyInterestRate / 100.0), (years * 12)) - 1

result = round((pmt_up / pmt_down), 2)

print("Your monthly payment is:" + str(round(result, 2)))

# ----------------------------Calculate the payment and store them in numpy--------------------------------------------#
original_loan = loan
loan_paid_percentage = [100]
loan_paid_balance = [loan]
loan_month = [0]
month_tracker = 1

while loan > 0:
    monthly_interest = loan * (monthlyInterestRate / 100)  # first rule out the increased monthly interest
    principal = result - monthly_interest
    if loan - principal < 0:  # if we succeed in every payment, we just set all loan remaining to 0.
        curr_percentage = 0
        curr_balance = 0
    else:
        curr_percentage = ((loan - principal) / original_loan) * 100
        curr_balance = loan - principal
    loan_paid_percentage.append(curr_percentage)
    loan_paid_balance.append(curr_balance)
    loan_month.append(month_tracker)
    month_tracker += 1
    loan -= principal

y_loan_paid_percentage = np.array(loan_paid_percentage)
y_loan_paid_balance = np.array(loan_paid_balance)
x_month = np.array(loan_month)

# ----------------------------printing the subplots using fig and axs grammar------------------------------------------#
fig, axs = plt.subplots(1, 2, figsize=(15, 5))
axs[0].scatter(x_month, y_loan_paid_percentage, s=10)    # for each plot, using the scatter connect by line plot
axs[0].plot(x_month, y_loan_paid_percentage)
axs[0].set_ylabel('Interest paid')
axs[0].set_xlabel('Month')

axs[1].scatter(x_month, y_loan_paid_balance, s=10)
axs[1].plot(x_month, y_loan_paid_balance)
axs[1].set_ylabel('Loan Balance')
axs[1].set_xlabel('Month')

plt.show()
