#!/usr/bin/env python3
import random


def gen_player_achievements() -> set[str]:
    r_num = random.randint(7, len(achievements))
    return set(random.sample(achievements, r_num))


if __name__ == "__main__":
    achievements = ['Crafting Genius', 'World Savior',
                    'Master Explorer', 'Collector Supreme',
                    'Untouchable', 'Boss Slayer', 'Strategist',
                    'Unstoppable', 'Speed Runner', 'Survivor',
                    'Treasure Hunter', 'First Steps', 'Sharp Mind',
                    'Cupid', 'Lover', 'What are you doing?',
                    'Are you sure?', 'Little Rocket man',
                    'My Kug-Fu is stronger', 'Shard Enthusiast',
                    'Eagle Eyes', 'Not Monkeying around', 'Yes/No/Maybe?',
                    'Serve, Please!', 'Peer into Darkness',
                    'Watching the Watchers', 'Observant', 'Ducky Boss']

    print("=== Achievement Tracker System ===\n")
    alice = gen_player_achievements()
    print(f"Player Alice: {alice}\n")

    bob = gen_player_achievements()
    print(f"Player Bob: {bob}\n")

    charlie = gen_player_achievements()
    print(f"Player Charlie: {charlie}\n")

    dylan = gen_player_achievements()
    print(f"Player Dylan: {dylan}\n")

    print("All distinct achievements: "
          f"{alice.union(bob, charlie, dylan)}\n")

    print("Common achievements: "
          f"{alice.intersection(bob, charlie, dylan)}\n")

    print("Only Alice has: "
          f"{alice.difference(bob.union(charlie, dylan))}")
    print("Only Bob has: "
          f"{bob.difference(alice.union(charlie, dylan))}")
    print("Only Charlie has: "
          f"{charlie.difference(alice.union(bob, dylan))}")
    print("Only Dylan has: "
          f"{dylan.difference(alice.union(bob, charlie))}\n")

    ach = set(achievements)
    print(f"Alice is missing: {ach.difference(alice)}\n")
    print(f"Bob is missing: {ach.difference(bob)}\n")
    print(f"Charlie is missing: {ach.difference(charlie)}\n")
    print(f"Dylan is missing: {ach.difference(dylan)}\n")
