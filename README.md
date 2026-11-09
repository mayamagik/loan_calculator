# Loan Calculator

A Python command-line application for calculating loan repayments using **annuity** (fixed monthly payment) or **differentiated** (decreasing monthly payment) methods.

Built as a four-stage project in the [Hyperskill](https://hyperskill.org/) Python learning track.

## Features

- Calculate a fixed monthly annuity payment from the principal, term, and annual interest rate.
- Calculate the number of months needed to repay a loan based on a monthly payment.
- Calculate the loan principal supported by a specified payment and term.
- Generate a month-by-month schedule of differentiated payments.
- Calculate total overpayment (amount paid above the original principal).
- Check command-line arguments for missing, incompatible, or non-positive values.

## Technologies

- Python 3
- `argparse` for command-line arguments
- `math` (`ceil` and `log`) for financial calculations

No third-party packages are required.

## How to run

1. Clone or download the repository.
2. Open a terminal in the folder containing the final `creditcalc.py` file.
3. Run a command using the examples below.

```bash
python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
```

If running from the root of the original Hyperskill project structure, the script may be located at `Loan Calculator/task/creditcalc/creditcalc.py`. Quote the path because it contains a space:

```powershell
python ".\Loan Calculator\task\creditcalc\creditcalc.py" --type=diff --principal=1000000 --periods=10 --interest=10
```

## Command-line arguments

| Argument | Description |
| --- | --- |
| `--type` | Loan payment type: `annuity` or `diff` (required) |
| `--principal` | Loan amount |
| `--payment` | Monthly payment amount (annuity only) |
| `--periods` | Repayment term in months |
| `--interest` | Annual interest rate as a percentage (required) |

For **differentiated payments**, provide `--principal`, `--periods`, and `--interest`; do not provide `--payment`.

For **annuity payments**, provide `--interest` and **exactly two** of `--principal`, `--payment`, and `--periods`. The calculator works out the missing value.

## Examples

### 1. Differentiated payments

```bash
python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
```

The calculator prints a payment for each month and the total overpayment. The principal portion is constant, while the interest portion decreases as the outstanding balance falls.

### 2. Calculate an annuity payment

```bash
python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
```

The calculator prints the fixed monthly payment, rounded up to a whole unit, and the total overpayment.

### 3. Calculate the repayment period

```bash
python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
```

The calculator prints the repayment duration in years and/or months and the total overpayment.

### 4. Calculate the loan principal

```bash
python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
```

The calculator prints the estimated loan principal and the total overpayment.

## Project development

The application was developed progressively across four Hyperskill stages:

1. **Stage 1:** Calculate the repayment duration for a basic, interest-free loan.
2. **Stage 2:** Add monthly payment calculations and handle the final payment.
3. **Stage 3:** Introduce `argparse` and interest-based annuity calculations.
4. **Stage 4:** Support differentiated payments, input validation, and overpayment calculations.

## Notes

- Interest is supplied as an **annual percentage rate**, then converted to a monthly rate for the calculations.
- Payment amounts are rounded up using `math.ceil`; outputs are simplified estimates rather than bank-grade amortization schedules.
- The program prints `Incorrect parameters` for invalid combinations or non-positive supplied values.

## Learning outcomes

This project provided practice with Python functions, loops, conditional logic, mathematical formulas, input validation, and building a command-line interface with `argparse`.
