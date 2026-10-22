import random 



cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


def draw_card(total):
    """Generators a random number from the 'cards. array and adds it to a 'hand'.
    
    Args:
        total (int): Cards in hand 

    Returns:
        total (int): Updated sum of hand 
    """
    total += random.choice(cards)
    return total 

def starting_hand():
    """Gets the first sum of the hand given to the player/dealer

    Returns: 
        first_hand (int) = sum of first two cards drawn
    """
    first_hand = draw_card(draw_card(0))
    return first_hand

def twenty1_checker(hand):
    """Checks to see if sum is at 21 for immediate game end

    Args:
        hand (int): current sum of hand given

    Returns:
        True(bool): Hand is at 21
        False(bool): Hand is not at 21 
    """
    if hand == 21:
        return True
    else:
        return False

def user_turn(userHand):
    """User draw cards until satisfied with their hand. \
    if user happens to hit 21 they immediately win. \
    if user happens to go over 21 they immediately lose.
    
    Args:
        userHand (int): User's current hand

    Returns:
        userHand (int): User's updated hand after their turn 

    Raises: 
        SystemExit: If the player goes over 21 
    """
    # User's turn
    while userHand < 21:
        if twenty1_checker(userHand): 
            print("You win!")
            exit(0)
        choice = input("\nHit or Stand? (H|h or S|s):  ")
        if choice == "h" or choice == "H": 
            userHand = draw_card(userHand)
            print(f"Your hand: {userHand}")
            if userHand > 21: 
                print("\nBusted")
                exit(0)
        elif choice == "s" or choice == "S":
            break
        else:
            print("Invalid choice") 
    return userHand

def determine_winner(userHand, dealerHand):
    """Deterwine winner of User and Dealer. \
    Dealer will do their final turn IF they are below 17
    Whoever is closer to 21 without going over wins.

    Args:
        userHand(int): User's hand
        dealerHand (int): Dealer's hand
    """
    userHand = user_turn(userHand)

    while dealerHand < 17:
        dealerHand = draw_card(dealerHand)
    print(f"Dealer's hand: {dealerHand}")

    if dealerHand > 21 or userHand > dealerHand:
        print("You win!")
    elif userHand == dealerHand:
        print("Tie.")
    else:
        print("You lose!")
    



def system():
    """User can start gambling for FREE if correct input is given
    
    Raises:
        SystemExit: If user's or dealer's opening hand is 21
    """
    startGame = input("Welcome! Ready to play\n Insert Y|y to play: ")
    if startGame == "y" or startGame == "Y": 
            userHand = starting_hand()
            print(f"Your hand: {userHand}")
            if twenty1_checker(userHand):
                print("You Win!")
                exit(0)

            dealerHand = starting_hand()
            print(f"Dealer's hand: {dealerHand}")
            if twenty1_checker(dealerHand):
                print("You lose!")
                exit(0)

            determine_winner(userHand, dealerHand)


if __name__ == "__main__":
    system()