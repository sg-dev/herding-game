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
    debrief = models.StringField(
        choices=[
            ["only_c", "I mostly played A (choice yielding a bonus)"],
            ["only_d", "I mostly played B (choice without a bonus)"],
            ["minority", "I followed the minority's strategy"],
            ["majority", "I followed the majority's strategy"],
            ["random", "I randomly choose between A and B"],
            ["sophisticated", "I followed a different strategy"],
        ],
        label="Which describes your strategy best?",
        widget=widgets.RadioSelect,
    )

    debrief_2 = models.StringField(
        choices=[
            ["only_c", "The others mostly played A"],
            ["only_d", "The others mostly played B"],
            ["minority", "They followed the minority's strategy"],
            ["majority", "They followed the majority's strategy"],
            ["random", "They randomly choose between A and B"],
            ["sophisticated", "They followed a different strategy"],
        ],
        label="How, do you think most of your opponents chose?",
        widget=widgets.RadioSelect,
    )
