def ft_count_harvest_recursive():
    har_day = int(input("Days until harvest: "))
    rec_count(har_day, 1)


def rec_count(har_day, cur_day):
    if cur_day <= har_day:
        print(f"Day {cur_day}")
        rec_count(har_day, cur_day + 1)
    else:
        print("Harvest time!")
