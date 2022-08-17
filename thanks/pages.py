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
        bonus_game_points = participant.vars["payoff_bonus_game"]
        bret_game_points = participant.vars["bret_payoff"]
        game_points = participant.payoff
        real_participation_fee = self.session.config["participation_fee"]
        real_game_payoff = game_points.to_real_world_currency(self.session)
        total_real_payout = real_game_payoff + real_participation_fee

        bonus_round_paid = participant.vars["round_to_pay_bonus"]

        if "prolific_completion_url" in self.session.vars:
            completion_url = self.session.vars["prolific_completion_url"]
        else:
            completion_url = None

        return {
            "bonus_game_points": bonus_game_points,
            "round_to_pay_bonus": bonus_round_paid,
            "bret_game_points": bret_game_points,
            "game_points": game_points,
            "game_payoff": real_game_payoff,
            "real_participation_fee": real_participation_fee,
            "total_real_payout": total_real_payout,
            "prolific_completion_url": completion_url,
        }


page_sequence = [Thanks]
