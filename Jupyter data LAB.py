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