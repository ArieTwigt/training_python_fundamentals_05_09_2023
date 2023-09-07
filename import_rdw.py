#%%
import requests

kenteken = input("Voer kenteken in:\n").upper()

endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={kenteken}"

response = requests.get(endpoint)

# %%
data = response.json()

# %%
print(data[0])
# %%
