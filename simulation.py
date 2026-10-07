import numpy as np


# =========================================================
# MOSQUITO — INSECTICIDE RESISTANCE
# =========================================================

def run_mosquito_simulation(pesticide, temperature, food, urbanization,
                            initial_population=800, carrying_capacity=12000,
                            initial_trait_frequency=0.15, generations=50):

    resistance_frequency = initial_trait_frequency
    population = [initial_population]
    trait_frequency = [resistance_frequency]
    fitness_values = []

    for _ in range(generations):
        previous_population = population[-1]
        previous_resistance = trait_frequency[-1]

        pesticide_pressure = pesticide / 100

        susceptible_fitness = 1 - 0.85 * pesticide_pressure
        resistant_fitness = (1 - 0.25 * pesticide_pressure) * 0.95

        # Temperature is represented as a normalized environmental condition.
        temperature_factor = 1 - ((temperature - 50) / 40) ** 2
        temperature_factor = max(0, temperature_factor)

        food_factor = 0.6 + 0.4 * (food / 100)
        urbanization_factor = 1 - 0.2 * (urbanization / 100)

        mean_fitness = (
            (1 - previous_resistance) * susceptible_fitness
            + previous_resistance * resistant_fitness
        )

        r = 0.30 * temperature_factor * food_factor * urbanization_factor * mean_fitness
        fitness_values.append(r)

        new_resistance = previous_resistance * resistant_fitness / mean_fitness
        new_resistance = np.clip(new_resistance, 0, 1)
        trait_frequency.append(new_resistance)

        new_population = previous_population + r * previous_population * (
            1 - previous_population / carrying_capacity
        )
        population.append(max(0, new_population))

    return np.arange(generations + 1), np.array(population), np.array(trait_frequency), fitness_values[-1]
# =========================================================
# WHITE CLOVER — CYANOGENESIS
# =========================================================

def run_clover_simulation(temperature, herbivory, moisture, urbanization,
                          initial_population=800, carrying_capacity=12000,
                          initial_trait_frequency=0.45, generations=50):

    cyanogenic_frequency = initial_trait_frequency
    population = [initial_population]
    trait_frequency = [cyanogenic_frequency]
    fitness_values = []

    for _ in range(generations):
        previous_population = population[-1]
        previous_frequency = trait_frequency[-1]

        frost_pressure = temperature / 100
        herbivore_pressure = herbivory / 100

        # Cyanogenesis has a defensive benefit when herbivores are common.
        defence_benefit = 0.35 * herbivore_pressure

        # Cyanogenesis also carries an abiotic cost under cold conditions.
        frost_cost = 0.30 * frost_pressure

        cyanogenic_fitness = 1 + defence_benefit - frost_cost
        acyanogenic_fitness = 1.0

        mean_fitness = (
            previous_frequency * cyanogenic_fitness
            + (1 - previous_frequency) * acyanogenic_fitness
        )

        moisture_factor = 0.7 + 0.3 * (moisture / 100)
        urban_factor = 1 - 0.10 * (urbanization / 100)

        r = 0.20 * moisture_factor * urban_factor * mean_fitness
        fitness_values.append(r)

        new_frequency = previous_frequency * cyanogenic_fitness / mean_fitness
        new_frequency = np.clip(new_frequency, 0, 1)
        trait_frequency.append(new_frequency)

        new_population = previous_population + r * previous_population * (
            1 - previous_population / carrying_capacity
        )
        population.append(max(0, new_population))

    return np.arange(generations + 1), np.array(population), np.array(trait_frequency), fitness_values[-1]

# =========================================================
# ANOLE LIZARD — URBAN TOEPAD ADAPTATION
# =========================================================

def run_anole_simulation(urbanization, surface_smoothness, temperature, humidity,
                         initial_population=800, carrying_capacity=12000,
                         initial_trait_frequency=0.20, generations=50):

    toepad_frequency = initial_trait_frequency
    population = [initial_population]
    trait_frequency = [toepad_frequency]
    fitness_values = []

    for _ in range(generations):
        previous_population = population[-1]
        previous_frequency = trait_frequency[-1]

        urban_pressure = urbanization / 100
        smooth_surface = surface_smoothness / 100

        # Adhesive toepads are more useful on smooth urban surfaces.
        selection_pressure = urban_pressure * smooth_surface
        adapted_fitness = 1 + 0.25 * selection_pressure
        typical_fitness = 1.0

        mean_fitness = (
            previous_frequency * adapted_fitness
            + (1 - previous_frequency) * typical_fitness
        )

        # Temperature and humidity affect overall population performance.
        temperature_factor = 1 - ((temperature - 50) / 40) ** 2
        temperature_factor = max(0, temperature_factor)

        humidity_factor = 0.7 + 0.3 * (humidity / 100)

        r = 0.18 * temperature_factor * humidity_factor * mean_fitness
        fitness_values.append(r)

        new_frequency = previous_frequency * adapted_fitness / mean_fitness
        new_frequency = np.clip(new_frequency, 0, 1)
        trait_frequency.append(new_frequency)

        new_population = previous_population + r * previous_population * (
            1 - previous_population / carrying_capacity
        )
        population.append(max(0, new_population))

    return np.arange(generations + 1), np.array(population), np.array(trait_frequency), fitness_values[-1]
# =========================================================
# PEPPERED MOTH — INDUSTRIAL MELANISM
# =========================================================

def run_moth_simulation(
    pollution,
    predator_pressure,
    habitat_darkness,
    food,
    initial_population=800,
    carrying_capacity=12000,
    initial_trait_frequency=0.30,
    generations=50
):
    """
    Peppered moth model.
    Trait: Melanic (dark) coloration.

    Pollution and habitat darkness influence camouflage.
    Predator pressure determines the strength of selection.
    Food availability affects population growth.
    """

    melanic_frequency = initial_trait_frequency
    population = [initial_population]
    trait_frequency = [melanic_frequency]
    fitness_values = []

    for generation in range(1, generations + 1):
        previous_population = population[-1]
        previous_frequency = trait_frequency[-1]

        pollution_level = pollution / 100
        predator_level = predator_pressure / 100
        habitat_level = habitat_darkness / 100
        food_level = food / 100

        # Combine the two environmental indicators of background darkness.
        environmental_darkness = 0.6 * pollution_level + 0.4 * habitat_level

        # Moderate industrial environments already provide some advantage
        # to melanism; very light environments favour pale moths.
        camouflage_bias = environmental_darkness - 0.35

        # Predation controls how strongly camouflage affects survival.
        selection_strength = 0.8 * predator_level

        melanic_fitness = 1 + camouflage_bias * selection_strength
        pale_fitness = 1 - camouflage_bias * selection_strength

        mean_fitness = (
            previous_frequency * melanic_fitness
            + (1 - previous_frequency) * pale_fitness
        )

        new_frequency = previous_frequency * melanic_fitness / mean_fitness
        new_frequency = np.clip(new_frequency, 0, 1)

        # Food supports reproduction and survival.
        food_factor = 0.2 + 0.8 * food_level

        # Predation reduces overall population survival.
        predation_mortality = 0.20 * predator_level

        r = 0.22 * food_factor * mean_fitness - predation_mortality
        fitness_values.append(r)

        trait_frequency.append(new_frequency)

        new_population = previous_population + r * previous_population * (
            1 - previous_population / carrying_capacity
        )
        new_population = max(0, new_population)

        population.append(new_population)

    generations_array = np.arange(0, generations + 1)

    return generations_array, np.array(population), np.array(trait_frequency), fitness_values[-1]
# =========================================================
# MAIN SIMULATION DISPATCHER
# =========================================================

def run_simulation(species, **kwargs):

    if "Mosquito" in species:
        return run_mosquito_simulation(
            kwargs["pesticide"], kwargs["temperature"],
            kwargs["food"], kwargs["urbanization"]
        )

    elif "White Clover" in species:
        return run_clover_simulation(
            kwargs["temperature"], kwargs["herbivory"],
            kwargs["moisture"], kwargs["urbanization"]
        )

    elif "Anole Lizard" in species:
        return run_anole_simulation(
            kwargs["urbanization"], kwargs["surface_smoothness"],
            kwargs["temperature"], kwargs["humidity"]
        )

    elif "Peppered Moth" in species:
        return run_moth_simulation(
            kwargs["pollution"], kwargs["predator_pressure"],
            kwargs["habitat_darkness"], kwargs["food"]
        )

    raise ValueError("Unknown species selected.")