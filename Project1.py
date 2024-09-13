import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("C:\\Users\\cleme\\Downloads\\order_details (1).csv")
df.dropna(axis = 1,inplace= True)
df[["year","month","nonsense"]] = df["created_at"].str.split("-",expand=True)
df.drop(columns=["nonsense","created_at"],inplace=True)
df[["year","month"]] = df[["year","month"]].astype(float)
print(df.head())