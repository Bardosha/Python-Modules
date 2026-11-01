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
          f"File '{filename}' closed\n")

    print("Transform data:\n"
          "---\n")
    new_lines: list[str] = []
    lines = content.splitlines()
    for lin in lines:
        new_lines.append(lin + "#")
        print(f"{lin}" + '#')
    print("\n---")

    new_filename = input("Enter new file name (or empty): ")
    if new_filename == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_filename}'")
        try:
            new_file: typing.TextIO = open(new_filename, "w")
        except OSError as error:
            print(f"Error creating file '{new_filename}': {error}")
            return

        try:
            for lin in new_lines:
                new_file.write(lin + "\n")
        except OSError as error:
            print(f"Error writing to file '{new_filename}': {error}")
            return
        finally:
            new_file.close()
        print(f"Data saved in file '{new_filename}'")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        filename = sys.argv[1]
        print(f"Accessing file: '{filename}'")
        read_file(filename)
