#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0  # *** down
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name.capitalize()}:",
                  "Error, height can't be negative",
                  "\nHeight update rejected")
        else:
            self._height = height
            print(f"\nHeight updated: {height:.0f}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name.capitalize()}:",
                  "Error, age can't be negative",
                  "\nAge update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days\n")

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self.name.capitalize()}:",
              f"{self._height:.1f}cm, {self._age} days old")


if __name__ == "__main__":
    pl1 = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    pl1.show()
    pl1.set_height(25.0)
    pl1.set_age(30)
    pl1.set_height(-5)
    pl1.set_height(-10000)
    pl1.set_age(-3)
    pl1.set_age(-15)
    print("\nCurrent state: ", end="")
    pl1.show()

'''
Это "безопасное значение по умолчанию", которое гарантирует,
что атрибут точно существует, даже если валидатор в set_height()/set_age()
откажется присваивать переданное значение. Это прямо
соответствует формулировке задания:
"leaving data unchanged or creating the plant with default values"
'''
