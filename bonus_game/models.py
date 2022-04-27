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

    simulated_playing_time = 5

    # Payoffs
    R = c(6)  # Both cooperating
    S = c(0)  # The one cooperating and the other defecting
    T = c(10)  # The one defecting and the other cooperating
    P = c(0)  # Both defecting

    # Bonus for cooperators
    bonus = c(4)

    # Neighborhood size
    neigh_size = 20

    # Fraction of defectors
    strategy_schedule = [18, 14, 12, 10, 8, 6, 6, 6, 6, 6]

    # Create extended lists of fractions and randomly assing them

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
    time_spent = models.FloatField()
    decision = models.CharField(
        choices=["C", "D"],
        doc="""This player's decision""",
        widget=widgets.RadioSelect(),
    )

    # debrief = models.StringField(
    #     choices=[
    #         ["only_c", "Mostly play C"],
    #         ["only_d", "Mostly play D"],
    #         ["minority", "Follow the minority's strategy"],
    #         ["majority", "Follow the majority's strategy"],
    #         ["random", "Randomly choose between C and D"],
    #         ["sophisticated", "Following a more complex strategy"],
    #     ],
    #     label="Which describes your strategy best?",
    #     widget=widgets.RadioSelect,
    # )

    # debrief_2 = models.StringField(
    #     choices=[
    #         ["only_c", "Mostly play C"],
    #         ["only_d", "Mostly play D"],
    #         ["minority", "Follow the minority's strategy"],
    #         ["majority", "Follow the majority's strategy"],
    #         ["random", "Randomly choose between C and D"],
    #         ["sophisticated", "Following a more complex strategy"],
    #     ],
    #     label="How, do you think most of your opponents chose?",
    #     widget=widgets.RadioSelect,
    # )

    # debrief = models.StringField(
    #     choices=[
    #         [1, "0-20%"],
    #         [2, "20-40%"],
    #         [3, "40-60%"],
    #         [4, "60-80%"],
    #         [5, "80-100%"],
    #     ],
    #     label='How large should the group to follow be?',
    #     widget=widgets.RadioSelect,
    # )
