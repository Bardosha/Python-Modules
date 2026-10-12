#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message="Unknown Garden Error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown Plant Error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown Water Error") -> None:
        super().__init__(message)


def check_temperature(temperature: int) -> None:
    if temperature > 40:
        raise PlantError("The tomato plant is wilting!")
    else:
        print("Temperature is ok!")


def check_tank(liter: float) -> None:
    if liter < 5:
        raise WaterError("Not enough water in the tank!")
    else:
        print("Tank volume is ok!")


def test_garden_errors() -> None:
    print("Testing PlantError...")
    try:
        check_temperature(50)
    except PlantError as p:
        print(f"Caught PlantError: {p}\n")

    print("Testing WaterError...")
    try:
        check_tank(3)
    except WaterError as w:
        print(f"Caught WaterError: {w}\n")

    print("Testing catching all garden errors...")
    try:
        check_temperature(70)
    except GardenError as g:
        print(f"Caught GardenError: {g}")
    try:
        check_tank(1)
    except GardenError as g:
        print(f"Caught GardenError: {g}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_garden_errors()
