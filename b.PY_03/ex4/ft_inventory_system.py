import sys


def check_par(args: list[str]) -> dict[str, int]:
    items: dict[str, int] = {}

    for item in args[1:]:
        i = item.split(':')
        if (len(i) == 2):
            name = i[0].strip()
            value = i[1].strip()

            if (not name or not value):
                print(f"Error - invalid parameter '{item}'")
                continue

            try:
                quantity = int(value)
            except ValueError:
                print(f"Quantity error for '{name}': "
                      f"invalid literal for int() with base 10: '{value}'")
            else:
                if (name not in items):
                    items[name] = quantity
                else:
                    print(f"Redundant item '{name}' - discarding")
        else:
            print(f"Error - invalid parameter '{name}'")

    return (items)

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print("Inventory is empty :(")
    else:
        inventory = check_par(sys.argv)
        print(f"Got inventory: {inventory}")

        print(f"Item list: {list(inventory.keys())}")

        sum_values = sum(list(inventory.values()))
        print(f"Total quantity of the {len(inventory)} items: "
            f"{sum_values}")

        for key in inventory:
            value = inventory[key]
            print(f"Item {key} represents {((value/sum_values)*100): .1f}%")

        max = inventory
        for key in inventory:
            value = inventory[key]

    

'''
strip() - удаляет пробелы "  ааа " = "ааа", "  " = ""
if (not i[0].strip() or not i[1].strip()): если внутри пусто зайди внутрь цикла
'''