from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import math


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


class Decision(Page):
    form_model = "player"
    form_fields = ["decision"]

    def vars_for_template(self):
        me = self.player
        R = Constants.R
        S = Constants.S
        T = Constants.T
        P = Constants.P

        # Last round's info
        if self.player.round_number > 1:
            # Get player's and bot's decision
            me = self.player.in_round(self.player.round_number - 1)

            # Get fraction of defectors
            f_prev = Constants.fractions_ext[me.id_in_group - 1][me.round_number - 1]

            # Number of cooperators and defectors
            n_C = math.ceil((1 - f_prev) * Constants.neigh_size)
            n_D = math.floor(f_prev * Constants.neigh_size)

            my_decision = me.decision
            payoff_from_defectors, payoff_from_cooperators = compute_player_payoff(
                my_decision, n_C, n_D
            )

            me.payoff = payoff_from_defectors + payoff_from_cooperators
        else:  # first round
            me = self.player.in_round(self.player.round_number)
            my_decision = None

            # Get fraction of coops/defs
            f_prev = Constants.fractions_ext[me.id_in_group - 1][me.round_number - 1]

            ## Number of cooperators and defectors
            n_C = math.ceil((1 - f_prev) * Constants.neigh_size)
            n_D = math.floor(f_prev * Constants.neigh_size)

            # Payoffs and bonus
            payoff_from_defectors, payoff_from_cooperators = 0, 0

            me.payoff = 0

        # Opponents
        opponents = []
        for i in range(Constants.neigh_size):
            opponents.append(Constants.opponents_list[me.id_in_group - 1][i])
        opponents.append(max(Constants.opponents_list[me.id_in_group - 1][:20]) + 1)

        # Return to template
        return dict(
            R=R,
            S=S,
            T=T,
            P=P,
            n_C=n_C,
            n_D=n_D,
            def_payoff=payoff_from_defectors,
            coop_payoff=payoff_from_cooperators,
            bonus=Constants.bonus,
            total_bonus=Constants.bonus * n_D,
            last_payoff=me.payoff,
            my_decision=my_decision,
            opponents=opponents,
        )


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
