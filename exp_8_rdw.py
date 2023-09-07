#%%
import requests
import pandas

#%%
selected_brand = input("Choose a brand:\n").upper()

# %%
endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={selected_brand}"

#%%
response = requests.get(endpoint)

#%%
data = response.json()

#%%
len(data)


#%%
df = pandas.DataFrame(data)

#%%
df

#%%
df.to_csv(f"data/export_{selected_brand}.csv", sep=";", index=False)
