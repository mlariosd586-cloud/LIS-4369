def get_requirements():
    print("Developer: Marco Larios-Diaz")
    print("Miles Per Gallon\n")
    print("Program Requirements:")
    print("1. Convert MPG.")
    print("2. Must use float data type for user input and calculation.")
    print("3. Format and round conversion to two decimal places.")
    print("4. Prevent division by zero.\n")

def calculate_mpg():
    print("Input:")
    miles = float(input("Enter miles driven: "))
    
    gallons = float(input("Enter gallons of fuel used: "))
    while gallons <= 0:
        print("Gallons must be greater than 0. Please re-enter.")
        gallons = float(input("Enter gallons of fuel used: "))
    
    mpg = miles / gallons
    
    print("\nOutput:")
    print("{0:,.2f} miles driven and {1:,.2f} gallons used = {2:,.2f} mpg".format(miles, gallons, mpg))