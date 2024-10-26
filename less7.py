import random

fuel_using = float(input("Введіть середню витрату палива (літри на 100 км): "))

route_length = random.randint(50, 500)

fuel_price_per_liter = 6.5

expected_fuel_needed = (route_length / 100) * fuel_using

trip_cost = expected_fuel_needed * fuel_price_per_liter

print(f"Випадкова довжина маршруту: {route_length} км")
print(f"Очікувана витрата палива: {expected_fuel_needed:.2f} літрів")
print(f"Орієнтовна вартість поїздки: {trip_cost:.2f} злотих")

# :.2f використовується для форматування рядків
# : — це вказівник на початок інструкції форматування для числа.
# .2 — це вказівка на те, що після десяткової коми повинно бути 2 знаки.
# f — означає, що число форматуватиметься як число з плаваючою комою (англ. float).
# print(f - означає, що всередині рядка можна використовувати змінні чи вирази, які будуть замінені на їх значення.
