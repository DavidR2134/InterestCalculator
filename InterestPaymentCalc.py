import pyfiglet
from calendar import monthrange
import sys



def calculateInterest(interest, balance):
    interest = interest / 100
    interest = interest / 365

    monthlyInterest = interest * balance

    return monthlyInterest

def calculateMonthlyInterestRate(monthlyInterest, daysInMonth):
    total = monthlyInterest * daysInMonth

    return total

def determineMonthBalance(interest, balance, payment):
    total = balance - (payment - interest)

    return total

def displayInfo(total, interest, payment, currentMonth, currentYear):
    while total > 0:
        daysInMonth = monthrange(currentYear, currentMonth)[1]
        i = calculateInterest(interest, total)
        interestPayment = calculateMonthlyInterestRate(i,daysInMonth)
        
        monthlyBalance.append(total)
        monthlyInterest.append(interestPayment)
        total = determineMonthBalance(interestPayment, total, payment)
        if currentMonth == 12:
            currentYear += 1
            currentMonth = 1
        else:
            currentMonth += 1

    print("-"*60)
    for i in range(len(monthlyBalance)):
        print(f"Month {i+1} Balance: ${round(monthlyBalance[i],2)}\nInterest: ${round(monthlyInterest[i],2)}")
        print("-"*60)

def createCSV(monthlyBalance, monthlyInterest):
    with open("payments.csv", 'a') as f:
        f.write("Month,Monthly Balance,Monthly Interest\n")
        for i in range(len(monthlyBalance)):
            f.write(f"{i+1}, {round(monthlyBalance[i],2)}, {round(monthlyInterest[i],2)}\n")

def getsumofInterest(monthlyInterest):
    t = 0
    for i in range(len(monthlyInterest)):
        t = t + monthlyInterest[i]

    return round(t, 2) 

cont = True
while cont == True:
    currentYear = 2023
    currentMonth = 1
    daysInMonth = monthrange(currentYear, currentMonth)[1]
    monthlyBalance = []
    monthlyInterest = []
    text = "Interest Calculator!"

    ascii_text = pyfiglet.figlet_format(text)

    print(ascii_text)

    total = float(input("How much do you owe: "))
    interest = float(input("Please enter your interest rate: "))
    payment = float(input("How much do you pay a month: "))
    interestPayment = calculateMonthlyInterestRate(calculateInterest(interest, total),daysInMonth)
    if interestPayment > payment:
            print("Your payments are not enough to cover the accumulated interest. Try increasing the payments.")
            wait = input("Please press enter to continue...\n")
            continue
    else:
        displayInfo(total, interest, payment, currentMonth, currentYear)
        print(f"Total interest paid: ${getsumofInterest(monthlyInterest)}")

        checkCsv = input("\nWould you like a .csv file to be generated? y/n: ")

        if checkCsv.lower() == 'y':
            createCSV(monthlyBalance, monthlyInterest)
        else:
            print("\nOkay, thanks!")

        
        c = input("Would you like to continue? y/n: ")
        if c.lower() == 'n':
            cont = False