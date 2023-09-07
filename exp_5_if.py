# %%
age = 19

if age < 18:
    print("Helaas geen alcohol")
    print("Neem cola")
else:
    print("Proost")

print("Rest van de code")

# %%
cities_list = ['Amsterdam', 'Rotterdam', 'Deventer', 'Leiden']

new_city = "Amsterdam"

if new_city not in cities_list:
    print(cities_list)
    cities_list.append(new_city)
    print(f"Added {new_city} to list")
    print(cities_list)
else:
    print(f"City {new_city} already in the list")

# %%
name = "Arie"

if "a" in name.lower():
    print("yes")

# %%
person = {}
person['name'] = "Jim"
person['age'] = 15

print(person)

# %%
if person['name'] == "Jim" or person['age'] > 18:
    print("Proost")
    
# %%
target_amount = 1000

current_amount = 0

while current_amount < target_amount:
    print(f"Current amount is {current_amount}")
    current_amount += 0
    print(f"New amount is {current_amount}")

# %%
