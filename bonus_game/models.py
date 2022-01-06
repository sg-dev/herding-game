from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
)

import random

doc = """
The Bonus game docs
"""

num_all_players = 60


class Constants(BaseConstants):
    name_in_url = "bonus_game"
    players_per_group = None
    num_rounds = 7
    trials = 2 * num_all_players

    # Payoffs
    R = c(5)  # Both cooperating
    S = c(0)  # The one cooperating and the other defecting
    T = c(8)  # The one defecting and the other cooperating
    P = c(1)  # Both defecting

    # Bonus for cooperators
    bonus = c(4)

    # Neighborhood size
    neigh_size = 20

    # Fraction of defectors
    fractions = [
        [0.8, 0.6, 0.5, 0.4, 0.3, 0.3, 0.3],
        [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
        [0.8, 0.6, 0.5, 0.4, 0.3, 0.2, 0.2],
    ]

    # Create extended lists of fractions and randomly assing them
    fractions_ext = fractions * trials
    random.shuffle(fractions_ext)

    # For graphics
    # Randomly assigned numbers to players (fixed for the whole game)
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
        choices=["C", "D"],
        doc="""This player's decision""",
        widget=widgets.RadioSelect(),
    )
    debrief = models.StringField(
        choices=[
            ["0-10%", "0-10%"],
            ["11-25%", "11-25%"],
            ["26-50%", "26-50%"],
            ["51-75%", "51-75%"],
            ["76-100%", "76-100%"],
        ],
        # label='The collected taxes (public pot) is redistributed among:',
        widget=widgets.RadioSelect,
    )
