import marimo

__generated_with = "0.23.3"
app = marimo.App(width="columns")


@app.cell(column=0)
def _():
    from collections import Counter, namedtuple
    from dataclasses import dataclass
    from pprint import pprint
    from random import shuffle

    import marimo as mo

    return Counter, dataclass, mo, namedtuple, pprint, shuffle


@app.cell
def _(namedtuple):
    Card = namedtuple("Card", ["rank", "suit"])
    return (Card,)


@app.cell
def _(Card, Counter, mo, pprint):
    class Deck:
        """Parent class of a deck of cards, characterized by ranks and suits."""

        ranks = ["1", "2", "3", "4"]
        suits = ["A", "B", "C", "D"]

        def __init__(self):
            self._cards = [
                Card(rank, suit) for suit in self.suits for rank in self.ranks
            ]
            self.dealt_cards = []

        def __len__(self):
            return len(self.cards)

        def __str__(self):
            return f"Deck(suits={self.suits}, ranks={self.ranks})"

        def __repr__(self):
            return f"Deck(suits={self.suits}, ranks={self.ranks})"

        def __getitem__(self, position):
            return self.cards[position]

        def __setitem__(self, ind, val):
            self.cards[ind] = val

        def __add__(self, other):
            return self.cards + other.cards

        @property
        def cards(self):
            return self._cards

        def deal(self):
            dealt_card = self.cards.pop()
            self.dealt_cards.append(dealt_card)
            return dealt_card

        def deal_cards(self, number_of_cards):
            for _ in range(number_of_cards):
                self.deal()

        def reveal_deck(self):
            for card in self.cards:
                pprint(card)

        def show_deck(self):
            return mo.tree(self.cards)

        def show_deck_2(self):
            return mo.accordion(
                dict(
                    (
                        (str(index), card)
                        for index, card in enumerate(self.cards, start=1)
                    )
                ),
                multiple=True,
            )

    class French52Deck(Deck):
        face_cards = "JQKA"
        number_cards = "23456789T"
        ranks = number_cards + face_cards
        suits = "♠♥♦♣"

    class CardCount:
        def __init__(self, deck: Deck):
            self.deck = deck
            self._counts = self._count_deck()

        def _count_deck(self):
            only_ranks = [card.rank for card in self.deck.cards]

            return Counter(only_ranks)

        @property
        def counts(self):
            return self._counts

        def __repr__(self):
            return f"CardCount({dict(self._counts)}"

        def __lt__(self, other):
            return self.counts < other.counts

    return CardCount, Deck, French52Deck


@app.cell
def _(Deck, dataclass):
    @dataclass
    class Player:
        name: str | int
        deck: Deck

        def show_hand(self):
            self.deck.show_deck()

        def deal_cards(self, number_of_cards: int = 1):
            self.deck.deal_cards(number_of_cards)   # type: ignore[attr-defined]

    return (Player,)


@app.cell
def _(CardCount, Deck, French52Deck, Player, shuffle):
    class Game:
        def __init__(
            self,
            players: int | list[str] = ["Iringó", "Margó"],
            cards_to_burn: int = 15,
            deck_type: Deck = French52Deck,
        ):
            self.players = self._create_players(players, deck_type)
            self.cards_to_burn = cards_to_burn
            self.deck_type = deck_type
            self.player_ranking = None

        def _create_players(self, players, deck_type):
            if isinstance(players, int):
                player_names = [f"Player_{ind}" for ind in range(1, players + 1)]
            else:
                player_names = players

            return [Player(name=name, deck=deck_type()) for name in player_names]

        def play_game(self):
            self._shuffle_decks()
            self._burn_cards()
            self._rank_players()
            self._finish_game()

        def _shuffle_decks(self):
            for player in self.players:
                shuffle(player.deck)

        def _burn_cards(self):
            for player in self.players:
                player.deal_cards(self.cards_to_burn)

        def _rank_players(self):
            player_counts = [
                (CardCount(player.deck), ind, player)
                for ind, player in enumerate(self.players, start=1)
            ]
            print(player_counts.sort(reverse=True))

            return self.player_ranking

        def _finish_game(self):
            pass

    return (Game,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    decorated = [(student.grade, i, student) for i, student in enumerate(student_objects)]
    decorated.sort()
    [student for grade, i, student in decorated]               # undecorate
    [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    """)
    return


@app.cell
def _():
    return


@app.cell(column=1)
def _(French52Deck, Player):
    player_1 = Player(name="Iringó", deck=French52Deck())
    player_2 = Player(name="Margó", deck=French52Deck())
    return (player_1,)


@app.cell
def _(player_1):
    player_1
    return


@app.cell
def _(Card):
    c = Card(2, "A")
    return (c,)


@app.cell
def _(c):
    c
    return


@app.cell
def _(player_1):
    player_1.deck.show_deck()
    return


@app.cell
def _(French52Deck):
    deck = French52Deck()
    return (deck,)


@app.cell
def _(deck):
    print(deck.cards)
    return


@app.cell
def _(CardCount, French52Deck):
    d = French52Deck()
    cnt = CardCount(d)
    return (cnt,)


@app.cell
def _(cnt):
    cnt
    return


@app.cell
def _(cnt):
    dict(cnt._counts)
    return


@app.cell
def _(Game):
    g = Game()
    return (g,)


@app.cell
def _(g):
    ls = g.play_game()
    return


@app.cell
def _(g):
    g.players
    return


@app.cell
def _(g):
    g.players[0].deck.show_deck()
    return


@app.cell
def _(g, shuffle):
    shuffle(g.players[0].deck)
    return


@app.cell
def _(g):
    g.players[0].deck.show_deck()
    return


@app.cell
def _(g):
    print(g.player_ranking)
    return


@app.cell
def _(Game):
    gg = Game(6)
    return (gg,)


@app.cell
def _(gg):
    print(gg.players[0].name)
    print(gg.players[0].deck.reveal_deck())
    return


@app.cell
def _(gg):
    gg.play_game()
    return


@app.cell
def _(gg):
    print(gg.players[0].name)
    print(gg.players[0].deck.reveal_deck())
    print(len(gg.players[0].deck))
    return


@app.cell
def _(gg):
    print(gg.players)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
