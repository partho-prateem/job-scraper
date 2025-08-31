import pandas as pd
df=pd.read_csv("jobs.csv")
df.drop_duplicates(inplace=True)
df.dropna(subset=["title"], inplace=True)
df["company"]=df["company"].str.strip()
df.to_csv("Jobs_cleaned.csv", index=False)
