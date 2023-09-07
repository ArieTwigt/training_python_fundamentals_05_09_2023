#%%
numbers = [1,2,3,4,5]
# %%
numbers[2]

# %%
names_list = ["Arie", "James"]
print(names_list)


#%%
names_list.append("Bob")
print(names_list)


# %%
if "Bob" in names_list:
    names_list.remove("Bob")

print(names_list)

# %%
numbers_list = [3, 1, 8, 2]
numbers_list.sort()
print(numbers_list)

# %%
numbers_list = [3, 1, 8, 2]
numbers_list.sort(reverse=True)
print(numbers_list)

# %%
names_list = ["0Bob" ,"James", "Arie", "Bob"]
names_list.sort(reverse=True)
print(names_list)

# %%
cities = ["Amsterdam", "Rotterdam", "Amsterdam", "Katwijk"]
cities_unique = list(set(cities))
print(cities_unique)

# %% creating the dictionary
person = {"name": "Arie", 
          "age": 33}


# %%
person = {}
person['name'] = "Arie"
person['age'] = 33

# %%
person['name']
# %%
person['city']

# %%
person.keys()

# %%
person.values()



# %%
person_1 = {"name": "James", 
            "age": 33, 
            "hobbies": ['mountainbiking', 'reading', 'gardening']}

print(person_1)
# %%
person_1['name']
# %%
person_1['hobbies'][1]

# %%
person_2 = {}
person_2['name'] = "Mary"
person_2['age'] = 30
person_2['hobbies'] = ['programming', 'tennis']

#%%
person_3 = {}
person_3['name'] = "Jimmy"
person_3['age'] = 12
person_3['hobbies'] = ['football', 'gaming']

# %%
family_dict = {}
family_dict['name'] = "Jones"
family_dict['people'] = [person_1, person_2, person_3]
family_dict

# %%
family_dict['people'][1]['age']

# %%
family_dict['people'][2]['hobbies'][1]
# %%
