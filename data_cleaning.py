import pandas as pd

df = pd.read_csv("wines.csv")

states = df.loc[df["country"] == "US"]
# states = df["country"]

df = pd.DataFrame(states)
df.to_csv("wines_cleaned.csv")
print(df.size)
# states.pd.DataFrame.to_csv("wines_cleaned.csv")
