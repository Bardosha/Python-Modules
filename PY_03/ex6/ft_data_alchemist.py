import random


if __name__ == "__main__":
    names = ['Alice', 'bob', 'Charlie', 'dylan',
             'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print("=== Game Data Alchemist ===")
    print(" === List comprehensions")
    print(f"Initial list of players: {names}")

    names_cap = [i.capitalize() for i in names]
    print(f"New list with ALL names capitalized: {names_cap}")

    names_only_cap = [i for i in names if i[0].isupper()]
    print(f"New list of capitalized names ONLY: {names_only_cap}\n")

    print(" === Dictionary comprehensions")
    names_with_scores = {i: random.randint(0, 1000) for i in names_cap}
    print(f"Score dict: {names_with_scores}")

    sum_values = sum(names_with_scores.values())
    average = sum_values/len(names_with_scores)
    print(f"Score average: {average: .2f}")

    higher_scores = {name: score
                     for name, score in names_with_scores.items()
                     if score > average}
    print(f"High scores: {higher_scores}")
