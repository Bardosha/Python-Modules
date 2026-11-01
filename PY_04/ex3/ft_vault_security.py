def secure_archive(filename: str, action: str = "r",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "r":
            with open(filename, "r") as file:
                file_content = file.read()
            return True, file_content

        elif action == "w":
            with open(filename, "w") as file:
                file.write(content)
            return True, "Content successfully written to file"

        else:
            return False, f"Invalid action: {action}"

    except OSError as error:
        return False, str(error)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    result = secure_archive("regular_file.txt")
    print(result)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("new.txt", "w", result[1]))