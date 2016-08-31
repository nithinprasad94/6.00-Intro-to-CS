#Program: ps1b.py

#FUNCTION DEFINITIONS:
def monthly_interest_finder(balance,interest_rate):

    fixed_monthly_payment = 0
    final_balance = balance
    months_needed = 0
    
    while(final_balance > 0):
        fixed_monthly_payment += 10
        (final_balance,months_needed) = annual_interest_computer_v2(balance,interest_rate,fixed_monthly_payment)
        
    print "RESULT"
    print "Monthly payment to pay off debt in 1 year: $",fixed_monthly_payment
    print "Number of months needed: ",months_needed
    print "Balance: ",final_balance
        
def annual_interest_computer_v2(balance,interest_rate,monthly_amount):

    total_paid = 0
    months_needed = 0

    i = 1
    
    while (i <= 12 and balance >= 0):

        (principle_paid,new_balance) = monthly_interest_computer_v2(balance,interest_rate,monthly_amount)
       
        balance = balance - principle_paid

        if balance <= 0:
            months_needed = i

        i += 1

    return (balance,months_needed)

def monthly_interest_computer_v2(balance,interest_rate,monthly_amount):
    interest_on_balance = balance*interest_rate/12
    principle_paid = '%.2f' % round((float(monthly_amount)-interest_on_balance), 2)
    new_balance = '%.2f' % round(balance-float(principle_paid), 2)

    return (float(principle_paid),float(new_balance))

#MAIN PROGRAM:

#Get input from user
balance = raw_input("Enter the outstanding balance on your credit card: ")
interest_rate = raw_input("Enter the annual credit card interest rate as a decimal: ")

monthly_interest_finder(float(balance),float(interest_rate))
