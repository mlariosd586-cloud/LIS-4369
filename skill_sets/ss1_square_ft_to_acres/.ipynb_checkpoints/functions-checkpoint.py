SQ_FEET_PER_ACRE = 43560

def get_requirements():
    print("Developer: Marco Larios-Diaz")
    print("Square Feet to Acres\n")
    print("Program Requirements:")
    print("1. Research: number of square feet to acre of land.")
    print("2. Must use float data type for user input and calculation.")
    print("3. Format and round conversion to two decimal places.\n")

def calculate_sqft_to_acre():
    print("Input:")
    sq_ft = float(input("Enter square feet: "))
    acres = sq_ft / SQ_FEET_PER_ACRE
    
    print("\nOutput:")
    print("{0:,.2f} square feet = {1:,.2f} acres".format(sq_ft, acres))