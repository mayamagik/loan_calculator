"""
Loan Calculator Stage 3
1. Import argparse and any mathematical functions you need.
2. Create the parser object using argparse.ArgumentParser().
3. Define the accepted arguments using parser.add_argument().
4. Parse the command-line arguments using parser.parse_args().
5. Validate the arguments and determine which parameter needs calculating.
6. Call the appropriate calculation function using the provided values.
7. Create validation rules for parameters (optional)
8. Print the result in the required format.
"""
import argparse
from math import ceil, log

parser = argparse.ArgumentParser(description='Calculate loan payments.')

parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float, required=True)

args = parser.parse_args()

def calc_payment(principal, interest, periods):
    i = interest / (12 * 100)
    monthly_payment = ceil(principal * i * ((1 + i) ** periods) /  (((1 + i) ** periods) - 1))
    print(f"Your monthly payment = {monthly_payment}!")
    return monthly_payment

def calc_periods(principal, monthly_payment, interest):
    i = interest / (12 * 100)
    periods = ceil(log(monthly_payment / (monthly_payment - i * principal), 1 + i))

    years = periods // 12
    months = periods % 12

    if years == 0:
        print(f"It will take {months} {'month' if months == 1 else 'months'} to repay this loan!")
    elif months == 0:
        print(f"It will take {years} {'year' if years == 1 else 'years'} to repay this loan!")
    else:
        year_word = "year" if years == 1 else "years"
        month_word = "month" if months == 1 else "months"
        print(f"It will take {years} {year_word} and {months} {month_word} to repay this loan!")

    return periods

def calc_principal(monthly_payment, periods, interest):
    i = interest / (12 * 100)
    principal = round(monthly_payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1)))
    print(f"Your loan principal = {principal}!")
    return principal



def main():
    values = [args.principal, args.periods, args.payment]

    if sum(value is None for value in values) !=1:
        print("Incorrect parameters")
        return
    if args.interest <= 0:
        print("Incorrect parameters")
        return
    if any(value is not None and value <= 0 for value in values):
        print("Incorrect parameters")
        return

    if args.payment is None:
        calc_payment(args.principal, args.interest, args.periods)
    elif args.periods is None:
        calc_periods(args.principal, args.payment, args.interest)
    elif args.principal is None:
        calc_principal(args.payment, args.periods, args.interest)



if __name__ == "__main__":
    main()