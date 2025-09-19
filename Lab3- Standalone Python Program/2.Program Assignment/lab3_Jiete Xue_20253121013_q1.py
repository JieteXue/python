cost_of_home=float(input("What is the cost of the home?"))
portion_down_payment=float(input("The percentage of the total cost for a down payment:"))
loan_term_year=float(input("The term of the loan mortgage:"))
monthly_payment=cost_of_home*(1-portion_down_payment)/12/loan_term_year
print("The monthly payment is",round(monthly_payment,4))
