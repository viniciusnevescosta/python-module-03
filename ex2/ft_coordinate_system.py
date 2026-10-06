import math


Coordinates = tuple[float, float, float]


def get_player_pos() -> Coordinates:
    while True:
        raw_coordinates = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        parameters = raw_coordinates.split(",")
        if len(parameters) != 3:
            print("Invalid syntax")
            continue
        values: list[float] = []
        valid = True
        for parameter in parameters:
            try:
                values.append(float(parameter))
            except ValueError as error:
                print(f"Error on parameter '{parameter.strip()}': {error}")
                valid = False
                break
        if valid:
            return (values[0], values[1], values[2])


def distance(first: Coordinates, second: Coordinates) -> float:
    return math.sqrt(
        (second[0] - first[0]) ** 2
        + (second[1] - first[1]) ** 2
        + (second[2] - first[2]) ** 2
    )


def main() -> None:
    center = (0.0, 0.0, 0.0)
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    print(f"Distance to center: {round(distance(first, center), 4)}")

    print("\nGet a second set of coordinates")
    second = get_player_pos()
    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(distance(first, second), 4)}"
    )


if __name__ == "__main__":
    main()
