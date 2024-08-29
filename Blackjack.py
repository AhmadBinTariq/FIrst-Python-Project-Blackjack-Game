import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_card():
    """
    This function returns a random card from the predefined list of cards.

    Parameters:
    None

    Returns:
    int: A random card from the list.
    """
    card = cards[random.randint(0, len(cards) - 1)]
    return card


def calculate_score(list_of_cards):
    """
    This function calculates the score of a given list of cards.
    If the score exceeds 21 and there is an 'Ace' in the list, it converts the 'Ace' from 11 to 1.

    Parameters:
    list_of_cards (list): A list of integers representing the cards.

    Returns:
    int: The calculated score.
    """
    score = 0
    for card in list_of_cards:
        score += card
    if score > 21:
        if 11 in list_of_cards:
            score -= 11
            score += 1
            list_of_cards[0].remove(11)
            list_of_cards[0].append(1)
    return score


def Game_Fin(condition):
    """
    This function prints the final result of the game.

    Parameters:
    condition (str): A string indicating the result of the game ("Win", "Lost", "Draw").

    Returns:
    None
    """
    print(f"Your cards are {player_card} and score is {player_score}")
    print(f"Computer's cards are {computer_card} and score is {computer_score}")
    print(f"You {condition}!")


continue_game = 'y'
while continue_game == 'y':
    player_card = [get_card(), get_card()]
    computer_card = [get_card(), get_card()]

    player_score = calculate_score(player_card)
    computer_score = calculate_score(computer_card)
    print(f"Computer's one card is {computer_card[0]}")
    game_finished = False
    while not game_finished:
        print(f"Your cards: {player_card} and your score is {player_score}")
        opt = input("Enter 'y' to get another card or 'n' to check:")
        if opt == 'y':
            player_card.append(get_card())
            if calculate_score(player_card) > 21:
                game_finished = True
                print("You exceeded 21!")
                Game_Fin("Lost")
            if computer_score < 17:
                computer_card.append(get_card())
                if calculate_score(computer_card) > 21:
                    game_finished = True
                    print("Computer exceeded 21!")
                    Game_Fin("Won")
        else:
            game_finished = True
            if computer_score < player_score:
                game_finished = True
                Game_Fin("Win")
            elif player_score < computer_score:
                game_finished = True
                Game_Fin("Lost")
        player_score = calculate_score(player_card)
        computer_score = calculate_score(computer_card)
    continue_game = input("Do you want to play again?(y/n)")