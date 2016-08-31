#Program: ps1c.py

#FUNCTION DEFINITIONS:
def monthly_interest_finder(balance,interest_rate):

    monthly_payment_lb = '%.2f' % round(float((balance*interest_rate/12.0)), 2)
    monthly_payment_ub = '%.2f' % round(float(balance*(1+(interest_rate/12.0))**12.0)/12.0, 2)

    (final_balance,months_needed,monthly_payment) = mi_bisection_search(balance,interest_rate,float(monthly_payment_lb),float(monthly_payment_ub))

    print "RESULT"
    print "Monthly payment to pay off debt in 1 year: $",monthly_payment
    print "Number of months needed: ",months_needed
    print "Balance: ",final_balance
    
def mi_bisection_search(balance,interest_rate,payment_lb,payment_ub):

    monthly_payment = float('%.2f' % round(float((payment_lb + payment_ub)/2), 2))
    (final_balance,months_needed) = annual_interest_computer_v2(balance,interest_rate,monthly_payment)
    final_balance = float('%.2f' % round(float(final_balance), 2))
    
    if (final_balance <= 0 and final_balance >= -0.2):
        return (final_balance,months_needed,monthly_payment)
    else:
        if (final_balance > 0):
            return mi_bisection_search(balance,interest_rate,monthly_payment,payment_ub)
        elif (final_balance < -0.2):
            return mi_bisection_search(balance,interest_rate,payment_lb,monthly_payment)
        
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
