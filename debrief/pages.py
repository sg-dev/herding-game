from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Debrief(Page):
    form_model = "player"
    form_fields = ["debrief", "debrief2"]

    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds


page_sequence = [Debrief]
