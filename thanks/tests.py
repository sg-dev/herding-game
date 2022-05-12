from otree.api import Currency as c
from otree.bots import Submission

from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Thanks
