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

    simulated_playing_time = 1

    # Payoffs
    R = c(6)  # Both cooperating
    S = c(0)  # The one cooperating and the other defecting
    T = c(10) # The one defecting and the other cooperating
    P = c(0)  # Both defecting

    # Bonus for cooperators
    bonus = c(4)

    # Neighborhood size
    neigh_size = 20

    # Fraction of defectors
    strategy_schedule = [18, 14, 12, 10, 8, 6, 6, 6]
    num_rounds = len(strategy_schedule)-1

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
    potential_payoff = models.CurrencyField()
    decision = models.CharField(
        choices=["A", "B"],
        doc="""This player's decision""",
        widget=widgets.RadioSelect(),
    )

    # set random payoff round
    def set_payoff(self, payoff):
        self.potential_payoff = payoff

        if self.round_number == 1:
            self.participant.vars["round_to_pay_bonus"] = random.randint(
                1, Constants.num_rounds
            )

        if self.participant.vars["round_to_pay_bonus"] == self.round_number:
            # actually pay this round
            self.payoff += payoff
            self.participant.vars["payoff_bonus_game"] = payoff
        else:
            # do not pay this round
            self.payoff += 0
