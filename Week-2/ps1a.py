#Program: ps1a.py

#FUNCTION DEFINITIONS:
def annual_interest_computer(balance,interest_rate,monthly_rate):

    total_paid = 0
    
    for i in range(1,13):
        print "Month: ",i

        (monthly_payment,principle_paid,new_balance) = monthly_interest_computer(balance,interest_rate,monthly_rate)
        total_paid += (monthly_payment)
        
        print "Minimum monthly payment: $",monthly_payment
        print "Principle paid: $",principle_paid
        print "Remaining balance: $",new_balance

        balance = balance - principle_paid
        
    print "RESULT"
    print "Total amount paid: $",total_paid
    print "Remaining balance: $",balance
    
def monthly_interest_computer(balance,interest_rate,monthly_rate):
    interest_on_balance = balance*interest_rate/12
    monthly_payment = '%.2f' % round(balance*monthly_rate, 2)
    principle_paid = '%.2f' % round((float(monthly_payment)-interest_on_balance), 2)
    new_balance = '%.2f' % round(balance-float(principle_paid), 2)

    return (float(monthly_payment),float(principle_paid),float(new_balance))

#MAIN PROGRAM:

#Get input from user
balance = raw_input("Enter the outstanding balance on your credit card: ")
interest_rate = raw_input("Enter the annual credit card interest rate as a decimal: ")
monthly_rate = raw_input("Enter the minimum monthly payment rate as a decimal: ")

annual_interest_computer(float(balance),float(interest_rate),float(monthly_rate))
