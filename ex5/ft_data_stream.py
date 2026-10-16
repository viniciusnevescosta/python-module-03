import random
from typing import Generator


Event = tuple[str, str]


def gen_event() -> Generator[Event, None, None]:
    players = ("alice", "bob", "charlie", "dylan")
    actions = (
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "use",
        "release",
    )
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(events: list[Event]) -> Generator[Event, None, None]:
    while events:
        index = random.randrange(len(events))
        yield events.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    stream = gen_event()
    for index in range(1000):
        player, action = next(stream)
        print(f"Event {index}: Player {player} did action {action}")

    events = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
