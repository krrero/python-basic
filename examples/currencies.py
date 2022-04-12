input = input("Enter the amount in COL: ")

pesos = float(input)

usd_equivalence = 3875

total_usd = round(pesos / usd_equivalence, 2)

message = str(total_usd)

print("You have: $" + message)