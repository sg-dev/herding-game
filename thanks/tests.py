from otree.api import Currency as c, currency_range, expect
from otree.bots import Submission

from bonus_game.pages import Thanks
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        pass
