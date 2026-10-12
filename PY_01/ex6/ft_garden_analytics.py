#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        self._height = 0.0
        self._plant_age = 0
        self.growth_rate = 1.0
        self.set_height(height)
        self.set_age(plant_age)
        self.stats = Plant.Statistics()

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

    @staticmethod
    def check_age(pl_age: int) -> bool:
        return pl_age > 365

    def grow(self, days: int = 1) -> None:
        self.set_height(self._height + self.growth_rate * days)
        self.stats.rec_grow()

    def age(self, days: int = 1) -> None:
        self.set_age(self._plant_age + days)
        self.stats.rec_age()

    def show(self) -> str:
        self.stats.rec_show()
        return (f"{self.name.capitalize()}: "
                f"{self._height:.1f}cm, {self._plant_age} days old")

    @classmethod
    def create_anonym(cls) -> "Plant":
        return (cls("Unknown plant", 0.0, 0))

    class Statistics:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def rec_grow(self) -> None:
            self._grow_count += 1

        def rec_age(self) -> None:
            self._age_count += 1

        def rec_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, "
                  f"{self._show_count} show")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    plant.stats.display()


class Flower(Plant):
    def __init__(self, name: str, height: float, plant_age: int,
                 color: str, growth_rate: float) -> None:
        super().__init__(name, height, plant_age)
        self.color = color
        self.growth_rate = growth_rate

    def bloom(self) -> None:
        print(f"{self.show()}")
        print(f" {self.name.capitalize()} is blooming beautifully!")

    def show(self) -> str:
        return (f"{super().show()}\n Color: {self.color}")


class Seed(Flower):
    def __init__(self, name: str, height: float, plant_age: int,
                 days: int, color: str, growth_rate: float,
                 seeds_per_day: float) -> None:
        super().__init__(name, height, plant_age, color, growth_rate)
        self.seeds = 0.0
        self.days = days
        self.seeds_per_day = seeds_per_day

    def bloom(self) -> None:
        super().bloom()
        self.seeds = self.days * self.seeds_per_day

    def seeding(self) -> None:
        print(f" Seeds: {self.seeds:.0f}")
        print(f"[make {self.name.lower()} grow, age and bloom]")
        self.grow(self.days)
        self.age(self.days)
        self.bloom()
        print(f" Seeds: {self.seeds:.0f}")

    def show(self) -> str:
        return (f"{super().show()}")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 plant_age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, plant_age)
        self.trunk_diameter = trunk_diameter
        self.stats: Tree.Statistics = Tree.Statistics()

    def produce_shade(self) -> None:
        print(f"Tree {self.name.capitalize()} now produces a shade "
              f"of {self.get_height():.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")
        self.stats.rec_shade()

    def show(self) -> str:
        return (f"{super().show()}\n Trunk diameter: "
                f"{self.trunk_diameter:.1f}")

    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._grow_shade = 0

        def rec_shade(self) -> None:
            self._grow_shade += 1

        def display(self) -> None:
            super().display()
            print(f" {self._grow_shade} shade")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is {30} more than a year? -> {Plant.check_age(30)}")
    print(f"Is {400} more than a year? -> {Plant.check_age(400)}")

    print("\n=== Flower")
    flower = Flower("Rose", 15.0, 10, "red", 8)
    print(flower.show())
    print(f" {flower.name.capitalize()} has not bloomed yet")
    display_statistics(flower)
    print(f"[asking the {flower.name.lower()} to grow and bloom]")
    flower.grow()
    flower.bloom()
    display_statistics(flower)

    print("\n=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    print(tree.show())
    display_statistics(tree)
    print(f"[asking the {tree.name.lower()} to produce shade]")
    tree.produce_shade()
    display_statistics(tree)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, 20, "yellow", 1.5, 2.1)
    print(sunflower.show())
    print(f" {sunflower.name.capitalize()} has not bloomed yet")
    sunflower.seeding()
    display_statistics(sunflower)

    print("\n=== Anonymous")
    anon = Plant.create_anonym()
    print(anon.show())
    display_statistics(anon)
