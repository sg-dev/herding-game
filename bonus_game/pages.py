from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import math




class Decision(Page):
    form_model = "player"
    form_fields = ["decision"]

    @staticmethod
    def compute_player_payoff(own_choice, n_collaborators, n_defectors):
        payoff_from_defectors = 0
        payoff_from_cooperators = 0
        if own_choice == "C":
            payoff_from_cooperators += n_collaborators * Constants.R
            payoff_from_defectors += n_defectors * Constants.S
            payoff_from_defectors += n_defectors * Constants.bonus
        elif own_choice == "D":
            payoff_from_defectors += n_defectors * Constants.P
            payoff_from_cooperators += n_collaborators * Constants.T
        else:
            raise ValueError("Invalid choice")

        return payoff_from_defectors, payoff_from_cooperators



    def number_strategies_last_round(self):
        me = self.player
        n_D = Constants.strategy_schedule[me.round_number-1]
        n_C = Constants.neigh_size - n_D

        return n_C, n_D

    def vars_for_template(self):
        player = self.player
        n_C, n_D = self.number_strategies_last_round()

        # Last round's info
        if player.round_number > 1:
            my_decision = player.in_round(self.player.round_number-1).decision
            payoff_from_defectors, payoff_from_cooperators = self.compute_player_payoff(
                my_decision, n_C, n_D
            )

            last_payoff = payoff_from_defectors + payoff_from_cooperators
            player.payoff = last_payoff
        else:  # first round
            my_decision = None
            payoff_from_defectors, payoff_from_cooperators = 0, 0
            last_payoff = 0

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
            total_bonus=Constants.bonus * n_D if my_decision == "C" else 0,
            last_payoff=last_payoff,
            my_decision=my_decision,
            RXnC = Constants.R * n_C,
            SXnD = Constants.S * n_D,
        )

    def js_vars(self):
        n_C, n_D = self.number_strategies_last_round()
        return dict(neigh_size=Constants.neigh_size, nC=n_C, secAnimation=3)

class ResultsWaitPage(Page):
    timeout_seconds = 1  # Change as you wish (for realistic view purposes)


class Debrief(Page):
    form_model = "player"
    form_fields = ["debrief"]

    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds


class Thanks(Page):
    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds

    def vars_for_template(self):
        # Pass variables to Thanks page
        if self.player.debrief == "0-10%" or self.player.debrief == "76-100%":
            final_message = "The correct answer is 30%, so you were a bit far off :( Good one anyway!"
        elif self.player.debrief == "11-25%" or self.player.debrief == "51-75%":
            final_message = (
                "The correct answer is 30%, so close but not yet there :| Nice try!"
            )
        else:
            final_message = (
                "Yes, you are right: the correct tax rate is 30% :) Great one!"
            )

        cumulative_payoff = 0
        for t in range(Constants.num_rounds):
            me = self.player.in_round(self.player.round_number - t)
            cumulative_payoff += me.payoff

        return dict(message=final_message, cumulative_payoff=cumulative_payoff)


page_sequence = [Decision, ResultsWaitPage, Debrief, Thanks]
