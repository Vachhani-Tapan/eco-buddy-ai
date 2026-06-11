def calculate_footprint(
    transport,
    distance,
    electricity,
    diet,
    flights
):
    """
    Returns:
    total_footprint (kg CO₂/year),
    contributors (dictionary)
    """

    contributors = {}

    # Transport emissions (kg CO₂ per km)
    transport_factors = {
        "Car": 0.21,
        "Bike": 0.0,
        "Public Transport": 0.08,
        "Walking": 0.0
    }

    transport_emission = (
        transport_factors[transport] *
        distance *        # km per day
        365               # yearly estimate
    )

    contributors["Transport"] = round(transport_emission, 2)

    # Electricity
    # Approx: 0.82 kg CO₂ per kWh
    electricity_emission = electricity * 0.82 * 12
    contributors["Electricity"] = round(electricity_emission, 2)

    # Diet (annual estimate)
    diet_factors = {
        "Vegetarian": 1000,
        "Non-Vegetarian": 1800
    }

    diet_emission = diet_factors[diet]
    contributors["Diet"] = diet_emission

    # Flights
    # Approx 250 kg CO₂ per flight
    flight_emission = flights * 250
    contributors["Flights"] = flight_emission

    total = sum(contributors.values())

    return round(total, 2), contributors

def calculate_eco_score(total_footprint):
    """
    Higher score = better sustainability
    """

    if total_footprint <= 2000:
        return 95
    elif total_footprint <= 3000:
        return 80
    elif total_footprint <= 4000:
        return 65
    elif total_footprint <= 5000:
        return 50
    else:
        return 35