import pandas as pd

df = pd.read_csv("wines_cleaned.csv")

df = pd.DataFrame(df)
df = df.sample(n=50000, random_state=1)

df.to_csv("filtered_wines.csv")
