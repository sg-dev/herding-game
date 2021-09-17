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
    name_in_url = 'herding_instructions'
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

    q1 = models.StringField(
        choices=[['Collaborating players', 'Collaborating players'], ['All players', 'All players'], ['Non collaborating players', 'Non collaborating players']],
        label='The collected taxes (public pot) is redistributed among:',
        widget=widgets.RadioSelect,
    )

    q2 = models.StringField(
        choices=[['Yes', 'Yes'], ['No', 'No']],
        label='Can you have different choices for different players in the same round?',
        widget=widgets.RadioSelect,
    )

    q3 = models.StringField(
        choices=[['0', '0'], ['1', '1'], ['5', '5'], ['10', '10']],
        label='If the tax is 50% and your earnings are 10, how much do you contribute to the public pot?',
        widget=widgets.RadioSelect,
    )
