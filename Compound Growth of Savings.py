# Program to calculate money value after doubling every year

# Input: initial amount and number of years
initial_amount = int(input("Enter initial amount: "))
years = int(input("Enter number of years: "))

# Calculate final amount (doubles every year)
final_amount = initial_amount * (2 ** years)

# Output
print("Final amount after", years, "years:", final_amount)
