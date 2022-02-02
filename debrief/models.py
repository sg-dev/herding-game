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


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)


class Group(BaseGroup):
    pass


class Constants(BaseConstants):
    name_in_url = "debrief"
    players_per_group = None
    num_rounds = 1


class Player(BasePlayer):
    decision = models.CharField(
        choices=["C", "D"],
        doc="""This player's decision""",
        widget=widgets.RadioSelect(),
    )

    debrief = models.StringField(
        choices=[
            ["only_c", "Mostly play C"],
            ["only_d", "Mostly play D"],
            ["minority", "Follow the minority's strategy"],
            ["majority", "Follow the majority's strategy"],
            ["random", "Randomly choose between C and D"],
            ["sophisticated", "Following a more complex strategy"],
        ],
        label="Which describes your strategy best?",
        widget=widgets.RadioSelect,
    )

    debrief_2 = models.StringField(
        choices=[
            ["only_c", "Mostly play C"],
            ["only_d", "Mostly play D"],
            ["minority", "Follow the minority's strategy"],
            ["majority", "Follow the majority's strategy"],
            ["random", "Randomly choose between C and D"],
            ["sophisticated", "Following a more complex strategy"],
        ],
        label="How, do you think most of your opponents chose?",
        widget=widgets.RadioSelect,
    )
