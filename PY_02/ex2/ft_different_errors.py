#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        7/0
    elif operation_number == 2:
        open('text.txt')
    elif operation_number == 3:
        '7' + 7
    else:
        7 + 7 + 7


def test_error_types() -> None:
    for op_n in range(5):
        print(f"Testing operation {op_n}...")
        try:
            garden_operations(op_n)
        except ValueError as v:
            print(f"Caught ValueError: {v}")
        except ZeroDivisionError as z:
            print(f"Caught ZeroDivisionError: {z}")
        except FileNotFoundError as f:
            print(f"Caught FileNotFoundError: {f}")
        except TypeError as t:
            print(f"Caught TypeError: {t}")
        else:
            print("Operation completed successfully")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
