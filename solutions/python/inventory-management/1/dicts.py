"""Functions to keep track and alter inventory."""


def create_inventory(items: list) -> dict:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """
    inventory = {}
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

def add_items(inventory: dict, items: list) -> dict:
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def decrement_items(inventory: dict, items: list) -> dict:
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """
    for item in items:
        item_count = inventory.get(item, 0)
        if item_count > 0:
            inventory[item] = item_count - 1
            
    return inventory


def remove_item(inventory: dict, item: str) -> dict:
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """
    inventory.pop(item,0)
    return inventory


def list_inventory(inventory: dict) -> list[tuple]:
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """
    return [(item_name, item_count) for item_name, item_count in inventory.items() if item_count > 0 ]
