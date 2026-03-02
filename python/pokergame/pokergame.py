class Card:
    """Represents a single playing card"""
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    
    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        
        self.rank = rank
        self.suit = suit
        self.value = self.RANKS.index(rank)  # 2=0, 3=1, ..., A=12
    
    def __repr__(self):
        return f"{self.rank}{self.suit[0]}"  # e.g., "5H"
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
    
    def __hash__(self):
        return hash((self.rank, self.suit))


class PokerHand:
    """Represents a poker hand of 5 cards"""
    
    HAND_RANKINGS = {
        'Straight Flush': 8,
        'Four of a Kind': 7,
        'Full House': 6,
        'Flush': 5,
        'Straight': 4,
        'Three of a Kind': 3,
        'Two Pair': 2,
        'One Pair': 1,
        'High Card': 0
    }
    
    def __init__(self, cards):
        if len(cards) != 5:
            raise ValueError("A poker hand must contain exactly 5 cards")
        
        # Check for duplicates
        if len(set(cards)) != 5:
            raise ValueError("Hand contains duplicate cards")
        
        self.cards = sorted(cards, key=lambda c: c.value, reverse=True)
        self.hand_type, self.tie_breaker = self._evaluate_hand()
    
    def _get_value_counts(self):
        """Return dictionary of value -> count"""
        value_counts = {}
        for card in self.cards:
            value_counts[card.value] = value_counts.get(card.value, 0) + 1
        return value_counts
    
    def _is_flush(self):
        """Check if all cards have the same suit"""
        return len(set(card.suit for card in self.cards)) == 1
    
    def _is_straight(self):
        """Check if cards form a consecutive sequence. Returns highest card value."""
        values = sorted([card.value for card in self.cards])
        
        # Check normal straight
        if values == list(range(values[0], values[0] + 5)):
            return values[-1]  # Return highest card
        
        # Check for A-2-3-4-5 (wheel straight - Ace is low)
        # A=12, 2=0, 3=1, 4=2, 5=3
        if values == [0, 1, 2, 3, 12]:
            return 3  # In wheel, 5 is the high card (value 3)
        
        return None
    
    def _evaluate_hand(self):
        """
        Evaluate and return (hand_type, tie_breaker)
        tie_breaker is a tuple of values used to break ties between same hand types
        """
        value_counts = self._get_value_counts()
        
        # Sort by count (descending), then by value (descending)
        sorted_groups = sorted(value_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
        counts = [count for _, count in sorted_groups]
        
        is_flush = self._is_flush()
        straight_high = self._is_straight()
        
        # Tie breaker will be tuple of card values in order of importance
        # For most hands, this is the grouped cards by count, then kickers
        tie_breaker = tuple(value for value, _ in sorted_groups)
        
        # Straight Flush
        if straight_high is not None and is_flush:
            return ('Straight Flush', (straight_high,))
        
        # Four of a Kind
        if counts == [4, 1]:
            return ('Four of a Kind', tie_breaker)
        
        # Full House
        if counts == [3, 2]:
            return ('Full House', tie_breaker)
        
        # Flush
        if is_flush:
            # All cards matter, sorted by value descending
            tie_breaker = tuple(sorted([c.value for c in self.cards], reverse=True))
            return ('Flush', tie_breaker)
        
        # Straight
        if straight_high is not None:
            return ('Straight', (straight_high,))
        
        # Three of a Kind
        if counts == [3, 1, 1]:
            return ('Three of a Kind', tie_breaker)
        
        # Two Pair
        if counts == [2, 2, 1]:
            return ('Two Pair', tie_breaker)
        
        # One Pair
        if counts == [2, 1, 1, 1]:
            return ('One Pair', tie_breaker)
        
        # High Card
        tie_breaker = tuple(sorted([c.value for c in self.cards], reverse=True))
        return ('High Card', tie_breaker)
    
    def get_rank(self):
        """Return numerical rank of hand (higher is better)"""
        return self.HAND_RANKINGS[self.hand_type]
    
    def __str__(self):
        cards_str = ' '.join(str(card) for card in self.cards)
        return f"{self.hand_type}: {cards_str}"
    
    def __lt__(self, other):
        """Compare two hands"""
        # First compare by hand type
        if self.get_rank() != other.get_rank():
            return self.get_rank() < other.get_rank()
        
        # Same hand type - compare tie breakers
        return self.tie_breaker < other.tie_breaker
    
    def __gt__(self, other):
        """Compare two hands"""
        if self.get_rank() != other.get_rank():
            return self.get_rank() > other.get_rank()
        return self.tie_breaker > other.tie_breaker
    
    def __eq__(self, other):
        """Check if hands are equal"""
        return self.get_rank() == other.get_rank() and self.tie_breaker == other.tie_breaker

import random

class Deck:
    """Represents a standard 52-card deck"""
    
    def __init__(self):
        self._create_deck()
    
    def _create_deck(self):
        """Create a fresh 52-card deck"""
        self.cards = [
            Card(rank, suit)
            for suit in Card.SUITS
            for rank in Card.RANKS
        ]
    
    def shuffle(self):
        """Shuffle the deck in place"""
        for i in range(len(self.cards)):
            r = random.randint(i, range(len(self.cards)))
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    def draw(self, num=1):
        """
        Draw one or more cards from the top of the deck.
        Returns a single Card if num=1,
        otherwise returns a list of Cards.
        """
        if num < 1:
            raise ValueError("Must draw at least one card")
        
        if num > len(self.cards):
            raise ValueError("Not enough cards left in deck")
        
        if num == 1:
            return self.cards.pop()
        
        return [self.cards.pop() for _ in range(num)]
    
    def reset(self):
        """Reset to a full shuffled deck"""
        self._create_deck()
        self.shuffle()
    
    def __len__(self):
        """Return number of cards remaining"""
        return len(self.cards)
    
    def __repr__(self):
        return f"Deck({len(self.cards)} cards remaining)"
    
# Utility Functions
def parse_card(card_str):
    """Parse a card string like '5H' or '10D' into a Card object"""
    if len(card_str) < 2:
        raise ValueError(f"Invalid card string: {card_str}")
    
    suit_map = {'H': 'Hearts', 'D': 'Diamonds', 'C': 'Clubs', 'S': 'Spades'}
    
    suit_char = card_str[-1].upper()
    rank = card_str[:-1]
    
    if suit_char not in suit_map:
        raise ValueError(f"Invalid suit: {suit_char}")
    
    return Card(rank, suit_map[suit_char])


def parse_hand(hand_str):
    """Parse a hand string like '5H 10D JC QS KH' into a PokerHand"""
    card_strings = hand_str.strip().split()
    cards = [parse_card(cs) for cs in card_strings]
    return PokerHand(cards)


# Test Cases
def run_tests():
    print("=" * 60)
    print("POKER HAND EVALUATOR - TEST CASES")
    print("=" * 60)
    
    # Basic hand type tests
    test_hands = [
        ("5H 6H 7H 8H 9H", "Straight Flush"),
        ("5H 5D 5C 5S 9H", "Four of a Kind"),
        ("5H 5D 5C 9S 9H", "Full House"),
        ("2H 5H 7H 9H KH", "Flush"),
        ("5H 6D 7C 8S 9H", "Straight"),
        ("5H 5D 5C 8S 9H", "Three of a Kind"),
        ("5H 5D 9C 9S KH", "Two Pair"),
        ("5H 5D 7C 9S KH", "One Pair"),
        ("2H 5D 7C 9S KH", "High Card"),
        ("AH 2H 3H 4H 5H", "Straight Flush"),  # Wheel
    ]
    
    print("\n1. Hand Type Recognition:")
    print("-" * 60)
    for hand_str, expected in test_hands:
        hand = parse_hand(hand_str)
        status = "✓" if hand.hand_type == expected else "✗"
        print(f"{status} {hand}")
        if hand.hand_type != expected:
            print(f"   Expected: {expected}, Got: {hand.hand_type}")
    
    # Tie-breaking tests
    print("\n2. Tie-Breaking (Same Hand Type):")
    print("-" * 60)
    
    tie_tests = [
        ("4H 4D 4C 4S 9H", "AH AD AC AS 9H", "Four of a Kind: Aces > Fours"),
        ("5H 5D 5C 9S 9H", "KH KD KC QS QH", "Full House: Kings full > Fives full"),
        ("5H 5D 7C 9S KH", "AH AD 7C 9S KH", "One Pair: Aces > Fives"),
        ("2H 5D 7C 9S KH", "2D 5C 7S 9H AH", "High Card: Ace high > King high"),
        ("5H 6H 7H 8H 9H", "9D 10D JD QD KD", "Straight Flush: K-high > 9-high"),
        ("5H 5D 9C 9S KH", "5C 5S 9H 9D AH", "Two Pair: Same pairs, Ace kicker > King"),
    ]
    
    for hand1_str, hand2_str, description in tie_tests:
        hand1 = parse_hand(hand1_str)
        hand2 = parse_hand(hand2_str)
        
        if hand2 > hand1:
            status = "✓"
        else:
            status = "✗"
        
        print(f"{status} {description}")
        print(f"   Hand 1: {hand1}")
        print(f"   Hand 2: {hand2}")
        print(f"   Winner: {'Hand 2' if hand2 > hand1 else 'Hand 1'}")
        print()
    
    # Sorting test
    print("\n3. Sorting Multiple Hands:")
    print("-" * 60)
    hands = [
        parse_hand("2H 5D 7C 9S KH"),  # High Card
        parse_hand("5H 5D 7C 9S KH"),  # One Pair
        parse_hand("AH AD AC AS 9H"),  # Four of a Kind
        parse_hand("5H 5D 5C 9S 9H"),  # Full House
        parse_hand("4H 4D 4C 4S 9H"),  # Four of a Kind (lower)
    ]
    
    sorted_hands = sorted(hands, reverse=True)
    print("Hands sorted from best to worst:")
    for i, hand in enumerate(sorted_hands, 1):
        print(f"{i}. {hand}")


def interactive_demo():
    """Interactive demo for testing hands"""
    print("\n" + "=" * 60)
    print("INTERACTIVE POKER HAND EVALUATOR")
    print("=" * 60)
    print("Enter a hand (e.g., '5H 10D JC QS KH')")
    print("Format: Rank (2-10,J,Q,K,A) + Suit (H,D,C,S)")
    print("Type 'compare' to compare two hands")
    print("Type 'quit' to exit\n")
    
    while True:
        try:
            cmd = input("Enter command or hand: ").strip()
            if cmd.lower() == 'quit':
                break
            
            if cmd.lower() == 'compare':
                hand1_str = input("Enter first hand: ").strip()
                hand2_str = input("Enter second hand: ").strip()
                
                hand1 = parse_hand(hand1_str)
                hand2 = parse_hand(hand2_str)
                
                print(f"\nHand 1: {hand1}")
                print(f"Hand 2: {hand2}")
                
                if hand1 > hand2:
                    print("Winner: Hand 1\n")
                elif hand2 > hand1:
                    print("Winner: Hand 2\n")
                else:
                    print("Tie!\n")
            else:
                hand = parse_hand(cmd)
                print(f"Result: {hand}")
                print(f"Tie-breaker values: {hand.tie_breaker}\n")
            
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    # Run automated tests
    run_tests()
    
    # Optional: Run interactive demo
    # Uncomment the line below to enable interactive mode
    # interactive_demo()