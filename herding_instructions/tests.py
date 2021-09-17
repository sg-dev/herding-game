from otree.api import Currency as c, currency_range, expect

from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield (pages.Instructions)
        yield pages.Comprehension, dict(q1='Collaborating players', q2='No', q3='5')



