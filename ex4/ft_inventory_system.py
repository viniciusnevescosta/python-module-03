import sys


def parse_inventory(parameters: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for parameter in parameters:
        parts = parameter.split(":")
        if len(parts) != 2 or parts[0] == "" or parts[1] == "":
            print(f"Error - invalid parameter '{parameter}'")
            continue
        item = parts[0]
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue
        try:
            quantity = int(parts[1])
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")
            continue
        inventory[item] = quantity
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")
    if len(sys.argv) == 1:
        print("Usage: python3 ft_inventory_system.py <item:quantity> ...")
        return
    inventory = parse_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")
    items = list(inventory.keys())
    print(f"Item list: {items}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")

    if not items or total == 0:
        print("Inventory has no quantities to analyze")
    else:
        most_abundant = items[0]
        least_abundant = items[0]
        for item in items:
            percentage = round(inventory[item] / total * 100, 1)
            print(f"Item {item} represents {percentage}%")
            if inventory[item] > inventory[most_abundant]:
                most_abundant = item
            if inventory[item] < inventory[least_abundant]:
                least_abundant = item
        print(
            f"Item most abundant: {most_abundant} with quantity "
            f"{inventory[most_abundant]}"
        )
        print(
            f"Item least abundant: {least_abundant} with quantity "
            f"{inventory[least_abundant]}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
