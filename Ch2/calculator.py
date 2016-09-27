# calculator.py
#   Simulates an interactive calculator

def main():
    print("This program will calculate valid expressions.")
    for i in range(100):
        answer = eval(input("Enter a valid mathematical expression: "))
        print("The answer is", answer)

main()
