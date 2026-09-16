def get_requirements():
    print("Developer: Marco Larios-Diaz")
    print("IT/ICT Student Percentage\n")
    print("Program Requirements:")
    print("1. Find number of IT/ICT students in class.")
    print("2. Calculate IT/ICT Student Percentage.")
    print("3. Must use float data type (to facilitate right-alignment).")
    print("4. Format, right-align numbers, and round to two decimal places.")
    print("5. Prevent division by zero.\n")

def calculate_percentages():
    print("Input:")
    it_students = float(input("Enter number of IT students: "))
    ict_students = float(input("Enter number of ICT students: "))
    
    total = it_students + ict_students
    while total == 0:
        print("\nTotal students cannot be 0. Re-enter values:")
        it_students = float(input("Enter number of IT students: "))
        ict_students = float(input("Enter number of ICT students: "))
        total = it_students + ict_students
    
    it_pct = (it_students / total) * 100
    ict_pct = (ict_students / total) * 100
    
    print("\nOutput:")
    print("{0:<16} {1:>8.2f}".format("Total Students:", total))
    print("{0:<16} {1:>7.2f}%".format("IT Students:", it_pct))
    print("{0:<16} {1:>7.2f}%".format("ICT Students:", ict_pct))