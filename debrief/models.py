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
        label="Which describes your strategy best?",
        widget=widgets.RadioSelect,
    )

    debrief2 = models.StringField(
        label="How do you think most of your opponents chose?",
        widget=widgets.RadioSelect,
    )

    def debrief_choices(player):
        choices = [
            ("only_c", "I mostly played A (i.e., bonus choice)"),
            ("only_d", "I mostly played B (i.e., no bonus choice)"),
            ("minority", "I followed the minority"),
            ("majority", "I followed the majority"),
            ("random", "I randomly choose between A and B"),
            ("sophisticated", "I followed a different strategy"),
        ]

        random.shuffle(choices)
        return choices

    def debrief2_choices(player):
        choices = [
            ["only_c", "They mostly played A"],
            ["only_d", "They mostly played B"],
            ["minority", "They followed the minority"],
            ["majority", "They followed the majority"],
            ["random", "They randomly choose between A and B"],
            ["sophisticated", "They followed a different strategy"],
        ]

        random.shuffle(choices)
        return choices
