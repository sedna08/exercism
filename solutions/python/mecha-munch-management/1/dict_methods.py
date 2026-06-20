"""Functions to manage a users shopping cart items."""


def add_item(current_cart: dict, items_to_add) -> dict:
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart


def read_notes(notes) -> dict:
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """
    return dict.fromkeys(notes, 1)


def update_recipes(ideas: dict, recipe_updates) -> dict:
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """
    for idea, recipe in recipe_updates:
        ideas[idea] = recipe
        
    return ideas


def sort_entries(cart: dict) -> dict:
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart: dict, aisle_mapping: dict) -> dict:
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """
    sorted_cart_items = sorted(cart.items(), reverse=True)

    fulfillment_cart = {}
    
    for item, quantity in sorted_cart_items:
        item_details = aisle_mapping[item]
        
        fulfillment_cart[item] = [quantity] + item_details
        
    return fulfillment_cart

def update_store_inventory(fulfillment_cart: dict, store_inventory: dict) -> dict:
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """
    for item,detail in fulfillment_cart.items():
        updated_item_count = store_inventory[item][0] - fulfillment_cart[item][0]
        if updated_item_count > 0:
            store_inventory[item][0] = updated_item_count
        else:
            store_inventory[item][0] = "Out of Stock"
    return store_inventory