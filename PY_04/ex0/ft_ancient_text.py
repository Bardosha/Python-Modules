import sys
import typing


def read_file(filename: str) -> None:
    try:
        file: typing.TextIO = open(filename, "r")
    except FileNotFoundError as fnf:
        print(f"Error opening file {filename}: {fnf}")
        return
    except PermissionError as per:
        print(f"Error opening file {filename}: {per}")
        return

    content = file.read()
    file.close()
    print("---\n")
    print(content)
    print("\n---\n"
          f"File '{filename}' closed")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        filename = sys.argv[1]
        print(f"Accessing file: '{filename}'")
        read_file(filename)
