class Card:
    """Represents a single playing card, including jokers."""
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, rank, suit=None):
        if rank == 'JOKER':
            self.rank = None
            self.suit = None
            self.value = -1  # special value for jokers
            self.is_joker = True
            return

        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}")

        self.rank = rank
        self.suit = suit
        self.value = self.RANKS.index(rank)
        self.is_joker = False

    def __repr__(self):
        if self.is_joker:
            return "JOKER"
        return f"{self.rank}{self.suit[0]}"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        return hash((self.rank, self.suit))


class PokerHand:
    """Represents a 5-card poker hand, supporting jokers."""

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

        self.cards = sorted(cards, key=lambda c: c.value if c.value >= 0 else 13, reverse=True)
        self.hand_type, self.tie_breaker = self._evaluate_hand()

    def _get_value_counts(self):
        counts = {}
        for c in self.cards:
            if not c.is_joker:
                counts[c.value] = counts.get(c.value, 0) + 1
        return counts

    def _is_flush(self):
        suits = [c.suit for c in self.cards if not c.is_joker]
        num_jokers = sum(1 for c in self.cards if c.is_joker)

        suit_counts = {}
        for s in suits:
            suit_counts[s] = suit_counts.get(s, 0) + 1

        if not suit_counts:
            return None  # All jokers? can't determine flush suit
        max_suit_count = max(suit_counts.values())
        if max_suit_count + num_jokers >= 5:
            # flush possible
            return max(suit_counts, key=suit_counts.get)
        return None

    def _is_straight(self):
        values = sorted([c.value for c in self.cards if not c.is_joker])
        num_jokers = sum(1 for c in self.cards if c.is_joker)
        if not values:
            return None  # All jokers can't form a specific straight

        # Try all possible straights high->low
        for high in range(12, 3, -1):
            needed = set(range(high, high - 5, -1))
            missing = needed - set(values)
            if len(missing) <= num_jokers:
                return high

        # Wheel straight A-2-3-4-5
        needed = {12, 0, 1, 2, 3}
        missing = needed - set(values)
        if len(missing) <= num_jokers:
            return 3  # high card = 5
        return None

    def _evaluate_hand(self):
        value_counts = self._get_value_counts()
        counts_sorted = sorted(value_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
        counts = [c for _, c in counts_sorted]
        tie_breaker = tuple([v for v, _ in counts_sorted])

        is_flush = self._is_flush()
        straight_high = self._is_straight()
        num_jokers = sum(1 for c in self.cards if c.is_joker)

        # Straight Flush
        if straight_high is not None and is_flush:
            return ('Straight Flush', (straight_high,))

        # Four of a Kind
        if counts and (counts[0] + num_jokers >= 4):
            return ('Four of a Kind', tie_breaker)

        # Full House
        if counts and (counts[0] + num_jokers >= 3) and (len(counts) > 1 and counts[1] + num_jokers >= 2 or num_jokers > 0):
            return ('Full House', tie_breaker)

        # Flush
        if is_flush:
            values = sorted([c.value for c in self.cards if not c.is_joker], reverse=True)
            return ('Flush', tuple(values))

        # Straight
        if straight_high is not None:
            return ('Straight', (straight_high,))

        # Three of a Kind
        if counts and (counts[0] + num_jokers >= 3):
            return ('Three of a Kind', tie_breaker)

        # Two Pair
        if counts.count(2) + (1 if num_jokers else 0) >= 2:
            return ('Two Pair', tie_breaker)

        # One Pair
        if counts.count(2) + (1 if num_jokers else 0) >= 1:
            return ('One Pair', tie_breaker)

        # High Card
        values = sorted([c.value for c in self.cards if not c.is_joker], reverse=True)
        return ('High Card', tuple(values))

    def get_rank(self):
        return self.HAND_RANKINGS[self.hand_type]

    def __str__(self):
        return f"{self.hand_type}: {' '.join(str(c) for c in self.cards)}"

    def __lt__(self, other):
        if self.get_rank() != other.get_rank():
            return self.get_rank() < other.get_rank()
        return self.tie_breaker < other.tie_breaker

    def __gt__(self, other):
        if self.get_rank() != other.get_rank():
            return self.get_rank() > other.get_rank()
        return self.tie_breaker > other.tie_breaker

    def __eq__(self, other):
        return self.get_rank() == other.get_rank() and self.tie_breaker == other.tie_breaker