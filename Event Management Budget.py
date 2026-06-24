# Program to calculate amount per participant

# Input: Total Event Cost and Number of Participants
total_cost = float(input("Enter total event cost: "))
participants = int(input("Enter number of participants: "))

# Calculation: Amount per participant
amount_per_participant = total_cost / participants

# Output
print("Amount per participant = ₹", amount_per_participant)
