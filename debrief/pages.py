from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Debrief(Page):
    form_model = "player"
    form_fields = ["debrief", "debrief_2"]

    def vars_for_template(self):
        cumulative_payoff = sum([p.payoff for p in self.player.in_all_rounds()])

        # Return to template
        return dict(
            R=Constants.R,
            S=Constants.S,
            T=Constants.T,
            P=Constants.P,
            bonus=Constants.bonus,
        )

    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds


page_sequence = [Debrief]
