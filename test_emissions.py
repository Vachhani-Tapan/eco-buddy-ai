from emissions import (
    calculate_footprint,
    calculate_eco_score
)

total, contributors = calculate_footprint(
    transport="Car",
    distance=20,
    electricity=250,
    diet="Non-Vegetarian",
    flights=2
)

score = calculate_eco_score(total)

print("Total:", total)
print("Contributors:", contributors)
print("Eco Score:", score)