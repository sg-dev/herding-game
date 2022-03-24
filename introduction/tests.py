from otree.api import Currency as c, currency_range, expect

from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):

        yield pages.Instructions_setting
        yield pages.Instructions_points
        yield pages.Instructions_example_round
        yield pages.Instructions_next_steps
        yield (pages.Attention1, {"q1": 1, "q2": 8, "q3": 2, "q4": 1, "q5": 1})
        yield pages.Start_game
