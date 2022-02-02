from otree.api import Currency as c, currency_range, expect
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        # Choose random action between cooperate/defect
        coin_flip = ["C", "D"]
        decision = random.choice(coin_flip)
        yield pages.Decision, dict(decision=decision)
        # expect('Both of you chose to Cooperate', 'in', self.html)
        # expect(self.player.payoff, Constants.both_cooperate_payoff)
        yield pages.Results
