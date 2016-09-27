# convert_distance.py
#   This program converts kilometers to miles

def main():
    print("This program converts distance in kilometers to miles.")
    kilo = eval(input("Enter the distance in kilometers: "))
    miles = kilo * .62
    print(kilo, "kilometers is", miles, "miles")

main()
