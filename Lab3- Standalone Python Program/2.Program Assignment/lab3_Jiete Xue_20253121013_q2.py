cost_of_home=float(input("What is the cost of the home?"))
portion_down_payment=float(input("The percentage of the total cost for a down payment:"))
loan_term_year=float(input("The term of the loan mortgage:"))
yearly_interest_rate=float(input("The yearly interest rate:"))
r=yearly_interest_rate/12
p=cost_of_home*(1-portion_down_payment)
monthly_payment=r*p/((1-(1+r)**(-12*loan_term_year)))
print("The monthly payment is",round(monthly_payment,4))