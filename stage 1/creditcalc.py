"""
Loan Calculator Stage 1
1. Take user input for loan
2. Take user input for monthly payment
3. Calculate no. of months for repayment
4. Display output
"""



def calc_months(loan, monthly_payment):
    num_months = int(loan / monthly_payment)
    return num_months


def main():
    input_loan = int(input("Enter loan principal:\n"))
    input_monthly_payment = int(input("Enter monthly payment:\n"))
    num_months = calc_months(input_loan, input_monthly_payment)
    print(f"It will take {num_months} months to repay the loan.")

if __name__ == "__main__":
    main()