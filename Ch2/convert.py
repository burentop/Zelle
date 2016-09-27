# convert.py
#   A program to convert Celsius temps to Fahrenheit

def main():
    print("Celsius", "Fahrenheit", sep="          ")
    for i in range(11):
        celsius = i * 10
        fahrenheit = 9/5 * celsius + 32
        print(celsius, fahrenheit, sep="               ")

main()