import random

# Initialize deck and shuffle
def create_deck():
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    return [f"{rank} of {suit}" for rank in ranks for suit in suits]

def deal_cards(deck, num_cards):
    return [deck.pop() for _ in range(num_cards)]

# Check for pairs in hand
def check_for_pairs(hand):
    rank_counts = {}
    pairs = []
    for card in hand:
        rank = card.split(" ")[0]
        if rank in rank_counts:
            pairs.append(rank)
            hand.remove(card)
            hand.remove(next(c for c in hand if c.startswith(rank)))
        else:
            rank_counts[rank] = 1
    return pairs

# Display player's hand
def display_hand(hand):
    return ", ".join(hand)

# Check winner
def determine_winner(player_pairs, computer_pairs):
    if len(player_pairs) > len(computer_pairs):
        return "You win!"
    elif len(player_pairs) < len(computer_pairs):
        return "Computer wins!"
    return "It's a tie!"

# Main game logic
def go_fish():
    # Setup
    deck = create_deck()
    random.shuffle(deck)
    
    player_hand = deal_cards(deck, 7)
    computer_hand = deal_cards(deck, 7)
    
    player_pairs = check_for_pairs(player_hand)
    computer_pairs = check_for_pairs(computer_hand)
    
    print("\nWelcome to Go Fish!")
    print("Pairs already found won't appear in your hand.\n")
    
    # Main game loop
    while deck and (player_hand or computer_hand):
        # Player's turn
        print(f"Your hand: {display_hand(player_hand)}")
        print(f"Your pairs: {', '.join(player_pairs) or 'None'}")
        
        if not player_hand:
            print("You have no cards left!")
            break
        
        asked_rank = input("Ask for a rank (e.g., 'A', '10', 'K'): ").strip()
        player_has = any(card.startswith(asked_rank) for card in player_hand)
        computer_has = any(card.startswith(asked_rank) for card in computer_hand)
        
        if computer_has:
            print(f"Computer gives you all its {asked_rank}s!")
            for card in [c for c in computer_hand if c.startswith(asked_rank)]:
                player_hand.append(card)
                computer_hand.remove(card)
            player_pairs += check_for_pairs(player_hand)
        else:
            print("Go Fish!")
            if deck:
                new_card = deck.pop()
                player_hand.append(new_card)
                print(f"You drew: {new_card}")
                player_pairs += check_for_pairs(player_hand)
        
        # Computer's turn
        if not computer_hand:
            print("Computer has no cards left!")
            break
        
        computer_ask = random.choice(computer_hand).split(" ")[0]
        print(f"\nComputer asks for: {computer_ask}")
        if any(card.startswith(computer_ask) for card in player_hand):
            print(f"You give all your {computer_ask}s to the computer.")
            for card in [c for c in player_hand if c.startswith(computer_ask)]:
                computer_hand.append(card)
                player_hand.remove(card)
            computer_pairs += check_for_pairs(computer_hand)
        else:
            print("Computer goes fishing!")
            if deck:
                new_card = deck.pop()
                computer_hand.append(new_card)
                computer_pairs += check_for_pairs(computer_hand)
    
    # Game Over
    print("\nGame over!")
    print(f"Your pairs: {', '.join(player_pairs) or 'None'}")
    print(f"Computer pairs: {', '.join(computer_pairs) or 'None'}")
    print(determine_winner(player_pairs, computer_pairs))

if __name__ == "__main__":
    go_fish()

