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


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1

    # Payoffs
    R = c(5) # Both cooperating
    S = c(3) # The one cooperating and the other defecting
    T = c(10) # The one defecting and the other cooperating
    P = c(4) # Both defecting


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    tax = models.StringField(
        choices=[['A fraction of the total payoff that the platform retains', 'A fraction of the total payoff that the platform retains'], ['A fraction of the total payoff that the platform redistributes', 'A fraction of the total payoff that the platform redistributes']],
        label='What is the tax rate?',
        widget=widgets.RadioSelect,
    )

    bonus = models.StringField(
        choices=[['When both players choose the same action', 'When both players choose the same action'], ['When players choose different actions', 'When players choose different actions']],
        label='When is the bonus awarded?',
        widget=widgets.RadioSelect,
    )

    q1 = models.StringField(
        choices=[['I would Cooperate', 'I would Cooperate'], ['I would Defect', 'I would Defect']],
        label='If α = 1 and the other player was about to Defect, which would the best choice be?',
        widget=widgets.RadioSelect,
    )

    q2 = models.StringField(
        choices=[['I would Cooperate', 'I would Cooperate'], ['I would Defect', 'I would Defect']],
        label='If α = 0 and the other player was about to Cooperate, which would the best choice be?',
        widget=widgets.RadioSelect,
    )