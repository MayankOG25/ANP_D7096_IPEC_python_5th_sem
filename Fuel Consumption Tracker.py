# Program to calculate average mileage of a car

# Input: Total distance traveled (km) and fuel consumed (liters)
distance = float(input("Enter the total distance traveled (in km): "))
fuel = float(input("Enter the fuel consumed (in liters): "))

# Calculation: Mileage = distance / fuel
if fuel != 0:
    mileage = distance / fuel
    print("Mileage of the car = ", mileage, "km/l")
else:
    print("Fuel consumed cannot be zero!")

