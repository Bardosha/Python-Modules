#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        self._height = 0.0
        self._plant_age = 0
        self.growth_rate = 1.0
        self.set_height(height)
        self.set_age(plant_age)

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name.capitalize()}:",
                  "Error, height can't be negative",
                  "\nHeight update rejected")
        else:
            self._height = height

    def get_height(self) -> float:
        return self._height

    def set_age(self, plant_age: int) -> None:
        if plant_age < 0:
            print(f"{self.name.capitalize()}:",
                  "Error, age can't be negative",
                  "\nAge update rejected")
        else:
            self._plant_age = plant_age

    def get_age(self) -> int:
        return self._plant_age

    def grow(self) -> None:
        self.set_height(self._height + self.growth_rate)

    def age(self) -> None:
        self.set_age(self._plant_age + 1)

    def show(self) -> str:
        return (f"{self.name.capitalize()}: "
                f"{self._height:.1f}cm, {self._plant_age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 plant_age: int, color: str) -> None:
        super().__init__(name, height, plant_age)
        self.color = color

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to bloom]")
        print(f"{self.show()}")
        print(f" {self.name.capitalize()} is blooming beautifully!")

    def show(self) -> str:
        return (f"{super().show()}\n Color: {self.color}")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 plant_age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, plant_age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces a shade "
              f"of {self.get_height():.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")

    def show(self) -> str:
        return (f"{super().show()}\n Trunk diameter: "
                f"{self.trunk_diameter:.1f}")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, plant_age: int,
                 days: int, harvest_season: str, growth_rate: float) -> None:
        super().__init__(name, height, plant_age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0
        self.days = days
        self.growth_rate = growth_rate

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 0.5  # ???

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5

    def show(self) -> str:
        return (f"{super().show()}\n Harvest season: {self.harvest_season}\n "
                f"Nutritional value: {self.nutritional_value:.0f}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    print(flower.show())
    print(f" {flower.name.capitalize()} has not bloomed yet")
    flower.bloom()

    print("\n=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    print(tree.show())
    tree.produce_shade()

    print("\n=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, 20, "April", 2.1)
    print(vegetable.show())
    print(f"[make tomato grow and age for {vegetable.days} days]")
    for _ in range(vegetable.days):
        vegetable.grow()
        vegetable.age()
    print(vegetable.show())
