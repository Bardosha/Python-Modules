#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    tem = int(temp_str)
    if tem <= 0:
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")
    elif tem >= 40:
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    return tem


def test_temperature() -> None:
    for value in ["25", "abc", "100", "-50"]:
        print(f"Input data is '{value}'")
        try:
            res = input_temperature(value)
        except ValueError as v:
            print(f"Caught input_temperature error: {v}\n")
        else:
            print(f"Temperature is now {res}°C\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
