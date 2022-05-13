from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


def number_strategies_round(round_number):
    n_D = Constants.strategy_schedule[round_number]
    n_C = Constants.neigh_size - n_D

    return n_C, n_D


class Decision(Page):
    form_model = "player"
    form_fields = ["decision", "time_spent"]

    @staticmethod
    def compute_player_payoff(own_choice, n_collaborators, n_defectors):
        payoff_from_defectors = 0
        payoff_from_cooperators = 0
        if own_choice == "A":
            payoff_from_cooperators += n_collaborators * Constants.R
            payoff_from_defectors += n_defectors * Constants.S
            payoff_from_defectors += n_defectors * Constants.bonus
        elif own_choice == "B":
            payoff_from_defectors += n_defectors * Constants.P
            payoff_from_cooperators += n_collaborators * Constants.T
        else:
            raise ValueError("Invalid choice")

        return payoff_from_defectors, payoff_from_cooperators

    def vars_for_template(self):
        player = self.player
        round_number = self.player.round_number
        n_C, n_D = number_strategies_round(round_number - 1)

        # Last round's info
        if player.round_number > 1:
            my_decision = player.in_round(self.player.round_number - 1).decision
            payoff_from_defectors, payoff_from_cooperators = self.compute_player_payoff(
                my_decision, n_C, n_D
            )

            last_payoff = payoff_from_defectors + payoff_from_cooperators
            player.set_payoff(last_payoff)
        else:  # first round
            my_decision = None
            payoff_from_defectors, payoff_from_cooperators = "?", "?"
            last_payoff = "?"
            player.set_payoff(0)

        cumulative_payoff = sum([p.payoff for p in self.player.in_all_rounds()])

        # Return to template
        return dict(
            R=Constants.R,
            S=Constants.S,
            T=Constants.T,
            P=Constants.P,
            n_C=n_C,
            n_D=n_D,
            def_payoff=payoff_from_defectors,
            coop_payoff=payoff_from_cooperators,
            bonus=Constants.bonus,
            total_bonus=Constants.bonus * n_D if my_decision == "A" else 0,
            last_payoff=last_payoff,
            cumulative_payoff=cumulative_payoff,
            my_decision=my_decision,
            RXnC=Constants.R * n_C,
            SXnD=Constants.S * n_D,
            TXnC=Constants.T * n_C,
            PXnD=Constants.P * n_D,
            is_in_deception_regime=self.session.config["deception"],
        )

    def js_vars(self):
        round_number = self.player.round_number - 1
        n_C, n_D = number_strategies_round(round_number)
        return dict(
            neigh_size=Constants.neigh_size,
            nC=n_C,
            secAnimation=0.2,
            nD=n_D,
            shuffle=False,
            skip=0,
        )


class ResultsWaitPage(Page):

    def get_timeout_seconds(self):
        player = self.player
        session = player.session
        return session.config["simulated_play_time"] + 3

    def vars_for_template(self):
        cumulative_payoff = sum([p.payoff for p in self.player.in_all_rounds()])
        # Return to template
        round_number = self.player.round_number
        if round_number >= 1:
            my_decision = self.player.in_round(round_number).decision
        else:
            my_decision = None

        return dict(
            R=Constants.R,
            S=Constants.S,
            T=Constants.T,
            P=Constants.P,
            n_C="?",
            n_D="?",
            def_payoff="?",
            coop_payoff="?",
            bonus=Constants.bonus,
            total_bonus="?",
            last_payoff="?",
            cumulative_payoff=cumulative_payoff,
            my_decision=my_decision,
            RXnC="?",
            SXnD="?",
            round_to_pay=self.player.participant.vars["round_to_pay_bonus"],
            is_in_deception_regime=self.session.config["deception"],
        )

    def js_vars(self):
        round_number = self.player.round_number
        n_C, n_D = number_strategies_round(round_number)

        # Get how many seconds it took the player to answer
        to_skip = random.randint(0, 14)

        return dict(
            neigh_size=Constants.neigh_size,
            nC=n_C,
            secAnimation=self.get_timeout_seconds(),
            nD=n_D,
            shuffle=True,
            skip=to_skip,
        )


class Results(Page):
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

    def vars_for_template(self):
        participant = self.participant
        bonus_game_points = participant.vars["payoff_bonus_game"]

        bonus_round_paid = participant.vars["round_to_pay_bonus"]

        return {
            "bonus_game_points": bonus_game_points,
            "round_to_pay_bonus": bonus_round_paid,
        }

page_sequence = [Decision, ResultsWaitPage, Results]
