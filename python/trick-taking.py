import random


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
        self.value = self.RANKS.index(rank)  # 2=0 ... A=12

    def __repr__(self):
        return f"{self.rank}{self.suit[0]}"  # e.g. 10H


class Deck:
    """Represents a standard 52-card deck"""

    def __init__(self):
        self._create_deck()

    def _create_deck(self):
        self.cards = [
            Card(rank, suit)
            for suit in Card.SUITS
            for rank in Card.RANKS
        ]

    def shuffle(self):
        for i in range(len(self.cards)):
            r = random.randint(i, len(self.cards) - 1)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        if not self.cards:
            raise ValueError("Deck is empty")
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def play_card(self, lead_suit):
        """
        Plays a card.
        - If starter (lead_suit is None): play highest card
        - If must follow suit: play highest card of that suit
        - If cannot follow suit: play highest card overall
        """

        # Starter: play highest card
        if lead_suit is None:
            card = max(self.hand, key=lambda c: c.value)

        else:
            matching = [c for c in self.hand if c.suit == lead_suit]

            if matching:
                # Play highest of matching suit
                card = max(matching, key=lambda c: c.value)
            else:
                # No matching suit → play highest overall
                card = max(self.hand, key=lambda c: c.value)

        self.hand.remove(card)
        return card

    def __repr__(self):
        return f"{self.name} (Score: {self.score})"


def play_game():
    deck = Deck()
    deck.shuffle()

    # Create 4 players
    players = [Player(f"Player {i+1}") for i in range(4)]

    # Deal 13 cards to each player
    for _ in range(13):
        for player in players:
            player.hand.append(deck.draw())

    # Random starter
    starter_index = random.randint(0, 3)

    print(f"\nStarting player: {players[starter_index].name}\n")

    # 13 rounds
    for round_num in range(1, 14):
        print(f"--- Round {round_num} ---")

        trick = []
        order = [(starter_index + i) % 4 for i in range(4)]

        # Starter plays first
        starter = players[order[0]]
        lead_card = starter.play_card(None)
        lead_suit = lead_card.suit

        trick.append((starter, lead_card))
        print(f"{starter.name} leads with {lead_card}")

        # Other players play
        for idx in order[1:]:
            player = players[idx]
            card = player.play_card(lead_suit)
            trick.append((player, card))
            print(f"{player.name} plays {card}")

        # Determine winner (highest value of lead suit)
        valid_cards = [
            (player, card)
            for player, card in trick
            if card.suit == lead_suit
        ]

        winner, winning_card = max(valid_cards, key=lambda x: x[1].value)

        # Score rule:
        # winner's value - starter's value
        score = winning_card.value - lead_card.value
        winner.score += score

        print(f"{winner.name} wins the round and earns {score} points\n")

        # Winner leads next round
        starter_index = players.index(winner)

    # Final results
    print("=== Final Scores ===")
    for player in players:
        print(player)

    overall_winner = max(players, key=lambda p: p.score)
    print(f"\n🏆 Winner of the game: {overall_winner.name}")


if __name__ == "__main__":
    play_game()