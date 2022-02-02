from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Thanks(Page):
    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds

    def vars_for_template(self):
        # Pass variables to Thanks page
        cumulative_payoff = 0
        for t in range(Constants.num_rounds):
            me = self.player.in_round(self.player.round_number - t)
            cumulative_payoff += me.payoff

        return dict(cumulative_payoff=cumulative_payoff)


page_sequence = [Thanks]
