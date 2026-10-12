#!/usr/bin/env python3

class Plant:
    def __init__(
            self, name: str, height: float,
            plant_age: int, hei_grow: float) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age
        self.hei_grow = hei_grow

    def grow(self) -> None:
        self.height += self.hei_grow

    def age(self) -> None:
        self.plant_age += 1

    def show(self) -> None:
        n_cap = self.name.capitalize()
        print(f"{n_cap}: {round(self.height, 1)}cm, {self.plant_age} days old")


def growth(plant: Plant) -> None:
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.grow()
        plant.age()
        plant.show()


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25.0, 30, 0.8),
        Plant("Sunflower", 80.0, 45, 1.3),
        Plant("Cactus", 15.0, 120, 0.3)
    ]
    for plant in plants:
        initial_height = plant.height
        print("=== Garden Plant Growth ===")
        plant.show()
        growth(plant)
        weekly_growth = round(plant.height - initial_height, 1)
        print(f"Growth this week: {weekly_growth}cm\n")
