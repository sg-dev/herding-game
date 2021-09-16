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
import itertools


author = 'Matteo Russo'

doc = """
Repeated multi-player Prisoner's Dilemma implementation with arbitrary payoffs and tax rate.
"""

num_all_players = 32


class Constants(BaseConstants):
    name_in_url = 'repeated_multi'
    players_per_group = None
    num_rounds = 5
    trials = 2

    # Payoffs
    R = c(5) # Both cooperating
    S = c(3) # The one cooperating and the other defecting
    T = c(10) # The one defecting and the other cooperating
    P = c(4) # Both defecting

    # Neighborhood size
    neigh_size = 20

    # Tax rates and lists
    tax_rates = [0, 0.25, 0.5, 0.75]
    lists = [[0.00, 0.25, 0.5, 0.75, 1.00],  [0.25, 0.25, 0.25, 0.25, 0.25],\
             [0.75, 0.75, 0.75, 0.75, 0.75], [1.00, 0.75, 0.5, 0.25, 0.00]]

    # Assign tax rate and fraction of defectors (Cartesian Product)
    # init_list = [[0, 0.5], [0.00, 0.25, 0.5, 0.75, 1.00]]
    alpha_f = []
    # for element in itertools.product(*init_list):
    #     alpha_f.append(element)
    for t in tax_rates:
        for l in lists:
            alpha_f.append([t, l])

    ext_factor = trials
    #print(ext_factor, ": ext_factor")
    alpha_f_list = alpha_f * ext_factor
    #print(alpha_f_list, ": before shuffling")
    random.shuffle(alpha_f_list)
    #print(alpha_f_list, ": after shuffling")

    # assigned players
    all_participants = list(range(500))
    opponents_list = []
    for n in range(num_all_players): 
        random.shuffle(all_participants)
        opponents_list.append(all_participants[:21])

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
    debrief = models.StringField()
