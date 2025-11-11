# 1. Declare and assign the variables here:
shuttle_name = 'Destination'
shuttle_speed_mph = 17500
distance_to_mars_km = 225000000
distance_to_moon_km = 38400
MILES_PER_KM = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line. 
print(type(shuttle_name))
print(type(shuttle_speed_mph))
print(type(distance_to_mars_km))
print(type(distance_to_moon_km))
print(type(MILES_PER_KM))

# Code your solution to exercises 3 and 4 here:
distance_to_mars_miles = distance_to_mars_km * MILES_PER_KM
distance_to_moon_miles = distance_to_moon_km * MILES_PER_KM
hours_to_mars = distance_to_mars_miles / shuttle_speed_mph
hours_to_moon = distance_to_moon_miles / shuttle_speed_mph
days_to_mars = hours_to_mars / 24
days_to_moon = hours_to_moon / 24


# Code your solution to exercise 5 here

print("It will take", days_to_mars, "days to reach Mars.")
print("It will take", days_to_moon, "days to reach the Moon.")

# name = input("Enter your name: ")
# Print a greeting
# print("Hello,", name, "! Welcome to Python programming.")

name = input("Enter your name: ")
# Print a greeting
print(f"Hello, {name}! Welcome to Python programming.") 

