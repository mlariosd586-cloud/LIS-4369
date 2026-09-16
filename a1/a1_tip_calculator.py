"""
Tip Calculator
Developer: Marco Larios-Diaz
Course: LIS4369
Semester: Fall 2026
"""

print("Tip Calculator\n")

print("Program Requirements:")
print("1. Must use float data type for user input (except, 'Party Number').")
print("2. Must round calculations to two decimal places.")
print("3. Must format currency with dollar sign, and two decimal places.\n")

print("User Input:")
meal_cost = float(input("Cost of meal: "))
tax_percent = float(input("Tax percent: "))
tip_percent = float(input("Tip percent: "))
people_num = int(input("Party number: "))

# Calculate tax, tip, and total amounts
tax_amount = round(meal_cost * (tax_percent / 100), 2)
due_amount = round(meal_cost + tax_amount, 2)
tip_amount = round(due_amount * (tip_percent / 100), 2)
total = round(due_amount + tip_amount, 2)
split = round(total / people_num, 2)

# Display formatted results
print("\nProgram Output:")
print("Subtotal:\t", "${:,.2f}".format(meal_cost))
print("Tax:\t\t", "${:,.2f}".format(tax_amount))
print("Amount Due:\t", "${:,.2f}".format(due_amount))
print("Gratuity:\t", "${:,.2f}".format(tip_amount))
print("Total:\t\t", "${:,.2f}".format(total))
print("Split (" + str(people_num) + "):\t", "${:,.2f}".format(split))
