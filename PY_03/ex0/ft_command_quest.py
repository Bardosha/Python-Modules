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
        print(f"Total arguments: {len(args)}\n")


'''
- args[1:] - срез/slicing (уберет название программы сразу)
- for i, arg in enumerate(...): автоматически даёт и номер, и значение
'''

if __name__ == "__main__":
    print("=== Command Quest ===")
    pr_arg(sys.argv)
