import sys
import typing


def read_file(filename: str) -> None:
    try:
        file: typing.TextIO = open(filename, "r")
    except OSError as error:
        print(f"[STDERR] Error opening file '{filename}': "
              f"{error}", file=sys.stderr)
        return

    try:
        content = file.read()
    except OSError as error:
        print(f"[STDERR] Error reading file '{filename}': "
              f"{error}", file=sys.stderr)
        return
    finally:
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
        new_line = lin + "#"
        new_lines.append(new_line)
        print(new_line)
    print("\n---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename = sys.stdin.readline().strip()
    if new_filename == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_filename}'")
        try:
            new_file: typing.TextIO = open(new_filename, "w")
        except OSError as error:
            print(f"[STDERR] Error opening file '{new_filename}': "
                  f"{error}", file=sys.stderr)
            print("Data not saved.")
            return

        try:
            for lin in new_lines:
                new_file.write(lin + "\n")
        except OSError as error:
            print(f"[STDERR] Error writing file '{new_filename}': "
                  f"{error}", file=sys.stderr)
            print("Data not saved.")
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
