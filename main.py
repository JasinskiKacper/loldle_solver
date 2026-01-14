import pandas as pd 

champions = 'data/champions.json'

df = pd.read_json(champions)

print(df)