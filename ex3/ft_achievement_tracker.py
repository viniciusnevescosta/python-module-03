import random


ACHIEVEMENTS = (
    "First Steps",
    "Master Explorer",
    "Boss Slayer",
    "Treasure Hunter",
    "Speed Runner",
    "Survivor",
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Unstoppable",
    "Collector Supreme",
    "Sharp Mind",
    "Hidden Path Finder",
    "Untouchable",
)


def gen_player() -> set[str]:
    amount = random.randint(6, 9)
    achievements = set(random.sample(ACHIEVEMENTS[:-1], amount))
    achievements.add("Untouchable")
    return achievements


def gen_player_achievements() -> set[str]:
    return gen_player()


def main() -> None:
    players = {
        "Alice": gen_player(),
        "Bob": gen_player(),
        "Charlie": gen_player(),
        "Dylan": gen_player(),
    }

    print("=== Achievement Tracker System ===")
    for name, achievements in players.items():
        print(f"\nPlayer {name}: {achievements}")

    all_distinct: set[str] = set()
    for achievements in players.values():
        all_distinct = all_distinct.union(achievements)
    print(f"\nAll distinct achievements: {all_distinct}")

    common = set(ACHIEVEMENTS)
    for achievements in players.values():
        common = common.intersection(achievements)
    print(f"\nCommon achievements: {common}")

    for name, achievements in players.items():
        others: set[str] = set()
        for other_name, other_achievements in players.items():
            if other_name != name:
                others = others.union(other_achievements)
        print(f"Only {name} has: {achievements.difference(others)}")

    complete_set = set(ACHIEVEMENTS)
    print()
    for name, achievements in players.items():
        print(f"{name} is missing: {complete_set.difference(achievements)}")


if __name__ == "__main__":
    main()
