from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Thanks(Page):
    def is_displayed(self):
        self.player.participant.finished = True
        return self.player.round_number == Constants.num_rounds

    def vars_for_template(self):
        participant = self.participant
        payoff = participant.payoff

        return {
            "round_to_pay_bonus": participant.vars["round_to_pay_bonus"],
            "payoff_bonus": participant.vars["payoff_bonus_game"],
            "bret_payoff": participant.vars["bret_payoff"],
            "payoff": payoff,
            "real_payoff": payoff.to_real_world_currency(self.session),
            "points_earned": payoff,
        }


page_sequence = [Thanks]
