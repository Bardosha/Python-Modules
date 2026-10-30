import sys


def score_calc(args: list[str]) -> None:
    message = ("No scores provided. Usage: python3 "
               "ft_score_analytics.py <score1> <score2> ...")
    if len(args) == 1:
        print(message)
        return

    score_int = []
    invalid = []

    for x in args[1:]:
        try:
            score_int.append(int(x))
        except ValueError:
            invalid.append(x)

    if invalid:
        for el in invalid:
            print(f"Invalid parameter: '{el}'")
        if len(invalid) == len(args[1:]):
            print(message)
            return

    players = len(score_int)
    total = sum(score_int)
    maxi = max(score_int)
    mini = min(score_int)
    print(f"Scores processed: {score_int}\n"
          f"Total players: {players}\n"
          f"Total score: {total}\n"
          f"Average score: {total / players}\n"
          f"High score: {maxi}\n"
          f"Low score: {mini}\n"
          f"Score range: {maxi - mini}\n")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_calc(sys.argv)
