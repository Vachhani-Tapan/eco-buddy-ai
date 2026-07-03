VALID_TRANSPORT = {"Car", "Bike", "Public Transport", "Walking"}
VALID_DIET = {"Vegetarian", "Non-Vegetarian"}
MAX_DISTANCE = 500
MAX_ELECTRICITY = 10000
MAX_FLIGHTS = 365


def calculate_footprint(
    transport,
    distance,
    electricity,
    diet,
    flights
):
    if transport not in VALID_TRANSPORT:
        raise ValueError(
            f"Invalid transport '{transport}'. Must be one of: {', '.join(sorted(VALID_TRANSPORT))}"
        )
    if diet not in VALID_DIET:
        raise ValueError(
            f"Invalid diet '{diet}'. Must be one of: {', '.join(sorted(VALID_DIET))}"
        )

    distance = max(0.0, min(float(distance), MAX_DISTANCE))
    electricity = max(0.0, min(float(electricity), MAX_ELECTRICITY))
    flights = max(0, min(int(flights), MAX_FLIGHTS))

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