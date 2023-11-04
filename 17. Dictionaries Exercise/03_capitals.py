countries = input().split(", ")
capitals = input().split(", ")

# zip_usage = dict(zip(countries, capitals))

comprehension = {countries[index]: capitals[index] for index in range(len(countries))}

for country, capital in comprehension.items():
    print(f"{country} -> {capital}")
