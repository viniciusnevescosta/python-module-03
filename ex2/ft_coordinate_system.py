import math


Coordinates = tuple[float, float, float]


def get_player_pos() -> Coordinates:
    while True:
        raw_coordinates = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        try:
            x_text, y_text, z_text = raw_coordinates.split(",")
        except ValueError:
            print("Invalid syntax")
            continue
        try:
            x = float(x_text)
            y = float(y_text)
            z = float(z_text)
            return (x, y, z)
        except ValueError as error:
            print(f"Invalid coordinate: {error}")


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
    try:
        main()
    except EOFError:
        print("\nCoordinate input ended.")
