class Human:
    def __init__(self, chips):
        self.chips = chips
        self.hand = None
        self.community_cards = []
        self.flop_cards = None
        self.turn_cards = None
        self.river_cards = None
        self.position = -1

    def new_game(self, num_players, position):
        self.position = position
    
    def deal(self, hand, bet_hist, pot):
        self.hand = hand
        return int(input(str(self.hand) + ' Pre-flop: '))

    def flop(self, flop_cards, bet_hist, pot):
        if len(self.community_cards) != 3:
            self.community_cards.extend(flop_cards)
        self.flop_cards = flop_cards[:]

        return int(input(str(self.hand) + ' Flop - ' + str(self.community_cards) + ' :'))

    def turn(self, turn_cards, bet_hist, pot):
        if len(self.community_cards) != 4:
            self.community_cards.append(turn_cards)
        self.turn_cards = turn_cards

        return int(input(str(self.hand) + ' Turn - ' + str(self.community_cards) + ' :'))

    def river(self, river_cards, bet_hist, pot):
        if len(self.community_cards) != 5:
            self.community_cards.append(river_cards)
        self.river_cards = river_cards

        return int(input(str(self.hand) + ' River - ' + str(self.community_cards) + ' :'))

    def end_game(self, bet_history, winner, hand, pot):
        result = ""
        if (winner == self.position):
            result += "You Win | "
        else:
            result += "You Lose | "
        result = result + "Pot size: " + str(pot) + " | "
        if (hand == []):
            result = result + "Winning hand: Not revealed"
        else:
            result = result + "Winning hand: " + str(hand[winner])
        print result