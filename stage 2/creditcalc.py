"""
Loan Calculator Stage 2
1. Add extra function as user option
2. Take user input for loan
3. Take user input for no. of months for repayment
4. Calculate repayment amount
5. Display output
"""
from math import ceil


def calc_months(loan, monthly_payment):
    num_months = int(round(loan / monthly_payment))
    return num_months

def calc_payment(loan, months):
    payment = ceil(loan / months)
    last_payment = loan - (months - 1) * payment
    return payment, last_payment

def main():
    input_loan = int(input("Enter loan principal:\n"))
    input_choice = input("What do you want to calculate?\ntype 'm' - for number of monthly payments,\ntype 'p' - for the monthly payment:\n")

    if input_choice == 'm':
        input_monthly_payment = int(input("Enter monthly payment:\n"))
        num_months = calc_months(input_loan, input_monthly_payment)
        print(f"It will take {num_months} months to repay the loan.")

    elif input_choice == 'p':
        input_num_months = int(input("Enter number of months:\n"))
        payment, last_payment = calc_payment(input_loan, input_num_months)
        if last_payment != payment:
            print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
        else:
            print(f"Your monthly payment = {payment}.")



if __name__ == "__main__":
    main()