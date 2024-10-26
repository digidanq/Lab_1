distance = float(input("Enter the distance traveled (in kilometers): "))  
fuel_consumption_per_100km = float(input("Enter the average fuel consumption (in liters per 100 km): "))  

fuel_price_per_liter = 6.5  

total_fuel_consumption = (distance / 100) * fuel_consumption_per_100km


estimated_travel_cost = total_fuel_consumption * fuel_price_per_liter

print(f"The expected fuel consumption for the trip is: {total_fuel_consumption:.2f} liters.")
print(f"The estimated travel costs are: {estimated_travel_cost:.2f} PLN.")