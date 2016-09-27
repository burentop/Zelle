# futval.py
#   A program to compute the value of an investment
#   carried 10 years into the FutureWarning

def main():
    print("This program calculates the future value")
    print("of a multi-year investment, compounded n periods per year.")

    principal = eval(input("How much is the initial investment: "))
    apr = eval(input("Enter the annual interest rate: "))
    duration = eval(input("How many years will you keep the investment: "))
    periods = eval(input("How many periods per year is interest compounded: "))

    for i in range(duration * periods):
        principal = principal * (1 + (apr / periods))

    print("The value in", duration, "years is:", principal)

main()
