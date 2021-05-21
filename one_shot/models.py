from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random


author = 'Matteo Russo'

doc = """
Prisoner's Dilemma implementation with arbitrary payoffs and tax rate.
"""

num_all_players = 4


class Constants(BaseConstants):
    name_in_url = 'one_shot'
    players_per_group = None
    num_rounds = 1

    # Payoffs
    R = c(5) # Both cooperating
    S = c(3) # The one cooperating and the other defecting
    T = c(10) # The one defecting and the other cooperating
    P = c(4) # Both defecting

    # Assign tax rate
    # Tax rates
    alpha = [0, 0.5]
    ext_factor = num_all_players // len(alpha)
    #print(ext_factor, ": ext_factor")
    tax_list = alpha * ext_factor
    #print(tax_list, ": before shuffling")
    random.shuffle(tax_list)
    #print(tax_list, ": after shuffling")

class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.CharField(
        choices=['C', 'D'],
        doc="""This player's decision""",
        widget=widgets.RadioSelect()
    )
