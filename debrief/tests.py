from otree.api import Currency as c, currency_range, expect

from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Debrief, {"debrief": "majority", "debrief_2": "minority"}
