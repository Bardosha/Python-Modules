import sys


def pr_arg(args: list[str]) -> None:
    if len(args) == 1:
        print(f"Program name: {args[0]}\n"
              f"No arguments provided!\n"
              f"Total arguments: {len(args)}\n")

    else:
        print(f"Program name: {args[0]}\n"
              f"Arguments received: {len(args) - 1}")
        for i in range(1, len(args)):
            print(f"Argument {i}: {args[i]}")
        # count = 1
        # for arg in args[1:]:
        #     print(f"Argument {count}: {arg}")
        #     count += 1
        print(f"Total arguments: {len(args)}\n")


if __name__ == "__main__":
    print("=== Command Quest ===")
    pr_arg(sys.argv)
