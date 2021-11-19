import pandas as pd

# df = pd.read_csv("wines_cleaned.csv")
df = pd.read_csv("../wines.csv")
# df = pd.DataFrame(df)
# print(df.size)
df = df.sample(n=50000, random_state=1)

df.to_csv("filtered_wines.csv")
