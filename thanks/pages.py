from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Thanks(Page):
    def is_displayed(self):
        self.player.participant.finished = True
        return self.player.round_number == Constants.num_rounds

    def vars_for_template(self):
        # Pass variables to Thanks page
        cumulative_payoff = self.player.participant.payoff

        return {
            "cumulative_payoff": cumulative_payoff.to_real_world_currency(self.session),
        }


page_sequence = [Thanks]
