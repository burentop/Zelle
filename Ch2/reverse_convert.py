# reverse_convert.py
#   A program to convert Fahrenheit to Celsius

def main():
    fahrenheit = eval(input("Enter the Fahrenheit temp: "))
    celsius = (fahrenheit - 32) * (5 / 9)
    print(fahrenheit, "degrees Fahrenheit is", celsius, "degrees Celsius")

main()