"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.
        1. 'J', 'Q', or 'K' = 10
        2. 'A' (ace card) = 1
        3. '2' - '10' = numerical value.
    """
    if card in {'J', 'Q', 'K', '10'}:
        return 10
    if card == 'A':
        return 1
    if card in {'2', '3', '4', '5', '6', '7', '8', '9'}:
        return int(card)
    return 0


def higher_card(card_one: str, card_two: str) -> str | tuple:
    """Determine which card has a higher value in the hand."""
    val_one = value_of_card(card_one)
    val_two = value_of_card(card_two)
    
    if val_one > val_two:
        return card_one
    if val_two > val_one:
        return card_two
    return (card_one, card_two)


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for an upcoming ace card (1 or 11).
    An ace already present in the hand counts as 11 points.
    """
    # Calculate the current hand score, treating an existing Ace as 11 points
    val_one = 11 if card_one == 'A' else value_of_card(card_one)
    val_two = 11 if card_two == 'A' else value_of_card(card_two)
    
    # If the current hand already has an Ace, a second Ace must be worth 1 point to avoid busting
    if card_one == 'A' and card_two == 'A':
        current_hand_value = 12 
    else:
        current_hand_value = val_one + val_two

    # If adding 11 would push the hand over 21, the upcoming Ace must be worth 1 point
    if current_hand_value + 11 > 21:
        return 1
    return 11


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack' (exactly 21)."""
    # Blackjack requires one Ace and one 10-value card
    has_ace = card_one == 'A' or card_two == 'A'
    has_ten_value = value_of_card(card_one) == 10 or value_of_card(card_two) == 10
    
    # Ensure it's not a pair of Aces (which is 12 or 2, not 21)
    return has_ace and has_ten_value and (card_one != card_two)


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet (totals 9, 10 or 11)."""
    # For double downs, if a hand has an Ace, it can be counted as 1 or 11 depending on preference.
    # Standard rules look at the hard or soft total of the first two cards.
    val_one = value_of_card(card_one)
    val_two = value_of_card(card_two)
    hand_total = val_one + val_two
    
    return 9 <= hand_total <= 11