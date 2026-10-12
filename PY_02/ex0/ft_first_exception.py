#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    for value in ["25", "abc", "-00000", "43asd789", "-777-77+6"]:
        print(f"Input data is '{value}'")
        try:
            res = input_temperature(value)
        except ValueError as v:
            print(f"Caught input_temperature error: {v}\n")
        else:
            print(f"Temperature is now {res}°C\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
