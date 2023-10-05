def interest_calculator(principal, apr, years):
    header = "This is a monthly payment loan calculator "

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12

    try:
        monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))
    except ZeroDivisionError:
        monthly_payment = 0.0
    
    monthly_payment = 0.0 if monthly_payment < 0 else monthly_payment
    
    return " The monthly payment for this loan is: %.2f " % monthly_payment
