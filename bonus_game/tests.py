from otree.api import Currency as c, currency_range, expect
from otree.bots import Submission
from . import pages
from ._builtin import Bot
from .models import Constants
import random

from time import sleep


class PlayerBot(Bot):
    def play_round(self):
        # Choose random action between cooperate/defect
        coin_flip = ["C", "D"]
        decision = random.choice(coin_flip)
        # sleep(timeout_seconds)
        yield pages.Decision, dict(decision=decision, time_spent=0)
        yield Submission(pages.ResultsWaitPage, check_html=False)


