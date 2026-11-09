"""
Loan Calculator Stage 4
1. Add parameter type for diff payment option
2. Create diff payment function
3. Validate the arguments and determine which parameter needs calculating.
4. Call the appropriate calculation function using the provided values.
5. Print the result in the required format.

"""
import argparse
from math import ceil, log

parser = argparse.ArgumentParser(description='Calculate loan payments.')

parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--type")

args = parser.parse_args()

def calc_diff(principal, periods, interest):
    i = interest / (12 * 100)
    total_payment = 0

    for month in range(1, periods + 1):
        payment = ceil(principal / periods + i * (principal - principal * (month-1) / periods))

        print(f"Month {month}: payment is {payment}")

        total_payment += payment

    overpayment = total_payment - principal
    print(f"\nOverpayment = {overpayment:g}")

def calc_payment(principal, interest, periods):
    i = interest / (12 * 100)
    monthly_payment = ceil(principal * i * ((1 + i) ** periods) /  (((1 + i) ** periods) - 1))
    print(f"Your annuity payment = {monthly_payment}!")
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

    if args.type not in ("annuity", "diff"):
        print("Incorrect parameters")
        return

    if args.interest is None or args.interest <= 0:
        print("Incorrect parameters")
        return

    if any(value is not None and value <= 0 for value in values):
        print("Incorrect parameters")
        return

    if args.type == "diff":
        if (args.principal is None or
                args.periods is None or
                args.payment is not None):
            print("Incorrect parameters")
            return

        calc_diff(args.principal, args.periods, args.interest)

    elif args.type == "annuity":
        if sum(value is None for value in values) != 1:
            print("Incorrect parameters")
            return

        if args.payment is None:
            payment = calc_payment(
                args.principal, args.interest, args.periods
            )
            overpayment = payment * args.periods - args.principal

        elif args.periods is None:
            i = args.interest / 1200

            if args.payment <= args.principal * i:
                print("Incorrect parameters")
                return

            periods = calc_periods(
                args.principal, args.payment, args.interest
            )
            overpayment = args.payment * periods - args.principal

        elif args.principal is None:
            principal = calc_principal(
                args.payment, args.periods, args.interest
            )
            overpayment = args.payment * args.periods - principal

        print(f"Overpayment = {overpayment:.0f}")



if __name__ == "__main__":
    main()