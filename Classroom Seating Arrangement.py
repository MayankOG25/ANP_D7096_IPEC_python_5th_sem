# Program to calculate complete rows

# Input: total students and students per row
total_students = int(input("Enter total number of students: "))
students_per_row = int(input("Enter number of students per row: "))

# Calculate number of complete rows
complete_rows = total_students // students_per_row

# Output result
print("Number of complete rows:", complete_rows)
