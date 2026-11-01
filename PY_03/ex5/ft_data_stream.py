from typing import Generator
import random


def gen_event(pl: list[str],
              act: list[str]) -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(pl), random.choice(act))


def consume_event(lioft: list[tuple[str, str]]
                  ) -> Generator[tuple[str, str], None, None]:
    while (lioft):
        del_event = random.choice(lioft)
        lioft.remove(del_event)
        yield del_event


if __name__ == "__main__":
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab",
               "move", "climb", "swim", "release"]

    gen = gen_event(players, actions)
    for i in range(1000):
        event = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    list_of_ten = []
    for i in range(10):
        tup = next(gen)
        list_of_ten.append(tup)
    print(f"Built list of 10 events: {list_of_ten}")

    del_event = consume_event(list_of_ten)
    for deleted in del_event:
        print(f"Got event from list: {deleted}")
        print(f"Remains in list: {list_of_ten}")
