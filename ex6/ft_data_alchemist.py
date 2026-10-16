import random


def main() -> None:
    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    capitalized_players = [name.capitalize() for name in players]
    already_capitalized = [name for name in players if name[:1].isupper()]
    scores = {name: random.randint(0, 1000) for name in capitalized_players}
    average = sum(scores.values()) / len(scores) if scores else 0.0
    high_scores = {name: score for name, score in scores.items()
                   if score > average}

    print("=== Game Data Alchemist ===")
    print(f"\nInitial list of players: {players}")
    print(f"New list with all names capitalized: {capitalized_players}")
    print(f"New list of capitalized names only: {already_capitalized}")
    print(f"\nScore dict: {scores}")
    print(f"Score average is {round(average, 2)}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
