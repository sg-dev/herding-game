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
            player.payoff = last_payoff
        else:  # first round
            my_decision = None
            payoff_from_defectors, payoff_from_cooperators = '?', '?'
            last_payoff = '?'

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
            total_bonus=Constants.bonus * n_D if my_decision == "C" else 0,
            last_payoff=last_payoff,
            cumulative_payoff=cumulative_payoff,
            my_decision=my_decision,
            RXnC=Constants.R * n_C,
            SXnD=Constants.S * n_D,
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
    timeout_seconds = Constants.simulated_playing_time + 3

    def vars_for_template(self):
        cumulative_payoff = sum([p.payoff for p in self.player.in_all_rounds()])

        # Return to template
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
            my_decision="?",
            RXnC="?",
            SXnD="?",
        )

    def js_vars(self):
        round_number = self.player.round_number
        n_C, n_D = number_strategies_round(round_number)

        # Get how many seconds it took the player to answer
        to_skip = random.randint(0, 14)


        return dict(
            neigh_size=Constants.neigh_size,
            nC=n_C,
            secAnimation=self.timeout_seconds,
            nD=n_D,
            shuffle=True,
            skip=to_skip,
        )


class Debrief(Page):
    form_model = "player"
    form_fields = ["debrief"]

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
