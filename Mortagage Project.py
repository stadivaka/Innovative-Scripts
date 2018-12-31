# Input: mortgage amount, annual interest, number of years for the loan period
# Output: mortgage payment schedule
# Algorithm:
#

# First Step: Print a greeting sentence at the beginning, and introduce the program!
print("\n\n\t\t\t\t\tWELCOME TO THE MORTGAGE PAYMENT GENERATOR")
print("\t\tThis program calculates the monthly mortgage payment and generates a mortgage payment schedule\n")

# Second Step: Ask the user for the mortgage amount, annual interest, and
#             the number of years for the loan period!
# Third Step: Convert the data type from (string) to (float) & (integer)!
mortgageAmount = float(input("Enter the Mortgage Amount in Dollars: $"))
annualInterest = float(input("Enter the Annual Interest Rate: %"))
yearsTotal = int(input("Enter the No. of Years for the Loan Period: "))

# Fourth Step: Do the math by calculating the monthly interst and the number
#              of the monthly payments!
monthlyInterest = annualInterest / 1200
monthlyPayments = yearsTotal * 12

# Fifth Step: Multiply (1 + R) by itself N times using a for loop!
X = 1 + monthlyInterest
for i in range(1, monthlyPayments):
    X *= 1 + monthlyInterest

# Sixth Step: Calculate the monthly mortgage payment using the formula!
monthlyPay = mortgageAmount * monthlyInterest * X / (X - 1)

# Seventh Step: Declare the amount of interest so far which is zero, and
#               then we will add to it in the coming for loop!
totalInterest = 0
BI = mortgageAmount

# Eighth step: Print an appropriate heading and organize your table!
print("\n\n\nYour payment schedule is as follows:\n")
print("\tPayment No.", "\t\tInterest", "\t\tPrincipal", "\t\tBalance\n")

# Ninth Step: Use a for a loop to calculate the interest, principal, and
#             balance for each monthly payment!
for j in range(1, monthlyPayments + 1):
    interest = BI * monthlyInterest
    prin = monthlyPay - interest
    balance = BI - prin
    BI = balance
    totalInterest = totalInterest + interest
    j = str(j)
    # Tenth Step: Right justify all the numbers ganerated in each column, and
    #               print all the numbers in dollars and cents!
    print("{:>14s} {:>25.2f} {:>24.2f} {:>21.2f}".format(j, interest, prin, balance))

# Eleventh Step: Calculate the total payment by the user!
totalPayment = totalInterest + mortgageAmount

# Twelvth Step: Print all the information regarding the user payments!
print("\nHere is all the information regarding your mortgage payments:\n")
print("The Mortgage Amount: $" + "{0:.2f}".format(mortgageAmount))
print("The Annual Interest Rate: %" + "{0:.2f}".format(annualInterest))
print("The Loan Period: ", yearsTotal, "Years, which is exactly ", monthlyPayments, "Months.")
print("The Monthly Mortgage Payment: $" + "{0:.2f}".format(monthlyPay))

# Thirteenth Step: Output the total interest paid and the total payment
#                  in dollars and cents as well
print("The Total Interest Paid: $" + "{0:.2f}".format(totalInterest))
print("The Total Payment Paid: $" + "{0:.2f}".format(totalPayment))