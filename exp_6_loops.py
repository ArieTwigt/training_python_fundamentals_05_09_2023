#%%
cities_list = ['Amsterdam', 'Rotterdam', 'Utrecht', 'Katwijk']

# %%
print(cities_list[0])
print(cities_list[1])
print(cities_list[2])
print(cities_list[3])


# %%
for i in cities_list:
    print(i)
    print("-"*5)
# %%
print(cities_list)

# %%
import math

diameters_list = [10, 20, 30, 40, 50, 60]

sizes_list = []

for diameter in diameters_list:

    radius = diameter / 2

    size = math.pow(radius, 2) * math.pi

    print(size)

    sizes_list.append(size)


# %%
