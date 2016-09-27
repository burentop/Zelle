# convert_meter.py
#   Converts a distance in meters to feet.

def main():
    print("This program converts a distance in meters to feet.")
    meters = eval(input("Enter a distance in meters: "))
    feet = meters * 3.28084
    print(meters, "meters is", feet, "feet")

main()
