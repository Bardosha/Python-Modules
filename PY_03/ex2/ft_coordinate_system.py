import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coor = input("Enter new coordinates as floats in format 'x,y,z': ")
        coor_spl = coor.split(',')
        if len(coor_spl) != 3:
            print("Invalid syntax.")
            continue
        try:
            temp_list: list[float] = []
            for sym in coor_spl:
                c = float(sym)
                temp_list.append(c)
        except ValueError as v:
            print(f"Error on parameter '{sym}': {v}")
        else:
            return (temp_list[0], temp_list[1], temp_list[2])


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    f_c = get_player_pos()
    print(f"Got a first tuple: {f_c}\n"
          f"It includes: X={f_c[0]}, Y={f_c[1]}, Z={f_c[2]}\n"
          "Distance to center: "
          f"{round(math.sqrt(f_c[0]**2 + f_c[1]**2 + f_c[2]**2), 4)}")

    print("\nGet a second set of coordinates")
    s_c = get_player_pos()
    squ = (s_c[0] - f_c[0])**2 + (s_c[1] - f_c[1])**2 + (s_c[2] - f_c[2])**2
    print("Distance between the 2 sets of coordinates: "
          f"{round(math.sqrt(squ), 4)}")
