house_0_dict = {
    "price_approx_usd": 115910.26,
    "surface_covered_in_m2": 128,
    "rooms": 4,
}
# Print `house_0_dict` type
print("house_0_dict type:", type(house_0_dict))
# Get output of `house_0_dict`
print(house_0_dict)
house_0_dict["price_per_m2"] = house_0_dict["price_approx_usd"] / house_0_dict["surface_covered_in_m2"]
print(house_0_dict)
houses_rowwise = [
    {
        "price_approx_usd": 115910.26,
        "surface_covered_in_m2": 128,
        "rooms": 4,
    },
    {
        "price_approx_usd": 48718.17,
        "surface_covered_in_m2": 210,
        "rooms": 3,
    },
    {
        "price_approx_usd": 28977.56,
        "surface_covered_in_m2": 58,
        "rooms": 2,
    },
    {
        "price_approx_usd": 36932.27,
        "surface_covered_in_m2": 79,
        "rooms": 3,
    },
    {
        "price_approx_usd": 83903.51,
        "surface_covered_in_m2": 111,
        "rooms": 3,
    },
]
# Print `houses_rowwise` object type
print("houses_rowwise type:", type(houses_rowwise))
# Print `houses_rowwise` length
print("houses_rowwise length:", len(houses_rowwise))
# Get output of `houses_rowwise`
print(houses_rowwise)
# Create for loop to iterate through `houses_rowwise`
    # For each observation, add "price_per_m2" key-value pair
for house in houses_rowwise:
    house["price_per_m2"] = house["price_approx_usd"] / house["surface_covered_in_m2"]
houses_rowwise
# Print `houses_rowwise` object type
print("houses_rowwise type:", type(houses_rowwise))
# Print `houses_rowwise` length
print("houses_rowwise length:", len(houses_rowwise))
# Get output of `houses_rowwise`
print(houses_rowwise)
# Declare `house_prices` as empty list
house_prices = []
# Iterate through `houses_rowwise`
for house in houses_rowwise:
    house_prices.append(house["price_approx_usd"])
    # For each house, append "price_approx_usd" to `house_prices`
print(house_prices)

# Calculate `mean_house_price` using `house_prices`
mean_house_price = sum(house_prices) / len(house_prices)

# Print `mean_house_price` object type
print("mean_house_price type:", type(mean_house_price))

# Get output of `mean_house_price`
print(mean_house_price)
houses_columnwise = {
    "price_approx_usd": [115910.26, 48718.17, 28977.56, 36932.27, 83903.51],
    "surface_covered_in_m2": [128.0, 210.0, 58.0, 79.0, 111.0],
    "rooms": [4.0, 3.0, 2.0, 3.0, 3.0],
}

# Print `houses_columnwise` object type
print("houses_columnwise type:", type(houses_columnwise))

# Get output of `houses_columnwise`
print(houses_columnwise)
mean_house_price = sum(houses_columnwise["price_approx_usd"]) / len(houses_columnwise["price_approx_usd"])

# Print `mean_house_price` object type
print("mean_house_price type:", type(mean_house_price))