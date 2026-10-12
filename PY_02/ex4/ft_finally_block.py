#!/usr/bin/env python3

class PlantError(Exception):
    def __init__(self, message="Unknown Plant Error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("Testing valid plants...")
    print("Opening watering system")
    plants = ["Tomato", "Lettuce", "Carrots"]
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as p:
        print(f"Caught PlantError: {p}")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    print("Opening watering system")
    plants = ["Tomato", "lettuce", "Carrots"]
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as p:
        print(f"Caught PlantError: {p}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
