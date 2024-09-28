import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
#Read the csv file to the data frame
df= pd.read_csv("C:\\Users\\cleme\\Downloads\\2_1_naming_ranges_fixed.csv",encoding_errors="replace")
#Drop the missing values
df.dropna(inplace=True)
#Determine how many cities are there
df["CustomerCity"].value_counts().head(10)
df["CustomerName"].unique()
#Determine how many subcategories there are
df["ProductSubcategory"].value_counts().head(10)
#Of all the orders, how many that went to london were bikes
df[(df["CustomerCity"] == "London") & (df["ProductCategory"] == "Bikes")]
# Group by product color and calculate the average price
df_grouped = df.groupby('ProductColor')['OrderLinePrice'].mean()

# Plot the bar chart
df_grouped.plot(
    kind="bar",
    xlabel="Color of the product.",
    ylabel="Average price of the product",
    title="Color vs Average Price of the product"
)
df["ProductCategory"].value_counts().plot(
    kind="bar",
    xlabel="Product Category",
    ylabel="Amount Sold",
    title="Bar Chart of Product Category vs Amount Sold"
);
Bikes_df = df[df["ProductCategory"]== "Bikes"]
total_bike_sales = Bikes_df["OrderLinePrice"].sum()
total_bike_sales
category_sales = df.groupby("ProductCategory")["OrderLinePrice"].sum()
category_sales
category_sales.plot(
    kind="bar",
    xlabel="Products Categories",
    ylabel="Amount sold in USD",
    title= "Bar Chart showing revenue from sale of Products"
);
Bikes_df= df[df["ProductCategory"] == "Bikes"].groupby("ProductSubcategory")["OrderLinePrice"].sum()
bikes_df = df[df["ProductCategory"] == "Bikes"].head(10)
Profit_for_bikes = bikes_df["Item_Price"] - bikes_df["ItemCost"].head(10)
df_sorted = df.sort_values(by="OrderToDelivery",ascending=True)[["CustomerCity","OrderToDelivery"]]
df.groupby("CustomerCountry")["Quantity"].sum().sort_values(ascending= False)
Oder_by_category= df.groupby(["CustomerCountry","ProductCategory"])["Quantity"].sum()
Oder_by_category
df.groupby("ProductColor")["Quantity"].sum()
df.groupby("CustomerName")["Quantity"].sum()
print(df.groupby("ProductCategory")["OrderLinePrice"].describe())
