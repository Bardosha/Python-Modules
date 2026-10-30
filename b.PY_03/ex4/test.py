ll = ["sword:1", "potion:5", "shield:2", "armor:3", "helmet:1", "sword:2", "hello", "key:value"]

mes1 = "Quantity error for 'key': invalid literal for int() with base 10: "
mes2 = "Error - invalid parameter "


items: dict[str, int] = {}

for item in ll:
    i = item.split(':')
    if len(i) == 2:
        name = i[0].strip()
        value = i[1].strip()

        if not name or not value:
            print(f"Error - invalid parameter '{item}'")
            continue

        try:
            quantity = int(value)
        except ValueError:
            print(f"Quantity error for {name}: "
                    f"invalid literal for int() with base 10: {value}")
        else:
            if name not in items:
                items[name] = quantity
            else:
                print(f"Redundant item '{name}' - discarding")
    else:
        print(f"Error - invalid parameter '{item}'")

print(items)
print(f"Item list: {list(items.keys())}")

sum_values = sum(list(items.values()))
print(f"Total quantity of the {len(items)} items: "
          f"{sum(list(items.values()))}")

for key in items:
        value = items[key]
        print(f"Item {key} represents {((value/sum_values)*100): .1f}%")
    



# def check_par(args: list[str]) -> dict[str, int]:
#     items: dict[str, int] = {}

#     for item in args[1:]:
#         i = item.split(':')
#         if len(i) == 2:
#             name = i[0].strip()
#             value = i[1].strip()

#             if not name or not value:
#                 print(f"Error - invalid parameter '{item}'")
#                 continue

#             try:
#                 quantity = int(value)
#             except ValueError:
#                 print(f"Quantity error for {name}: "
#                       f"invalid literal for int() with base 10: {value}")
#             else:
#                 if name not in items:
#                     items[name] = quantity
#                 else:
#                     print(f"Redundant item '{name}' - discarding")
#         else:
#             print(f"Error - invalid parameter '{item}'")

#     return items