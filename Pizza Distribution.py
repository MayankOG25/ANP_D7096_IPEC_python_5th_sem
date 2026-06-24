# Program to find remaining pizza slices after equal distribution

# Input: total slices and number of children
total_slices = int(input("Enter total pizza slices: "))
children = int(input("Enter number of children: "))

# Calculate remaining slices
remaining_slices = total_slices % children

# Output
print("Remaining slices:", remaining_slices)
