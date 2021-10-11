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
    name_in_url = 'survey_bonus'
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
        choices=[['I choose one single action to be played against all other players.', 'I choose one single action to be played against all other players.'],\
         ['I choose an actions for every player (20 in total).', 'I choose an actions for every player (20 in total).'],\
         ['I do not choose anything.', 'I do not choose anything.']],
        label='In each round, how many actions do you choose?',
        widget=widgets.RadioSelect,
    )

    q2 = models.StringField(
        choices=[['1', '1'], ['3', '3'], ['5', '5'], ['8', '8']],
        label='In the payoff matrix if you choose Not Collaborate and one opponent chooses Collaborate what is your payoff?',
        widget=widgets.RadioSelect,
    )

    q3 = models.StringField(
        choices=[['Choice of other players in the current round', 'Choice of other players in the current round'],\
         ['Choice of other players in the last round', 'Choice of other players in the last round']],
        label='What does the colour and letter in the summary figure show?',
        widget=widgets.RadioSelect,
    )

    q4 = models.StringField(
        choices=[['Cooperate', 'Cooperate'], ['Not Cooperate', 'Not Cooperate'], [' Any', ' Any']],
        label='Which choice entitles you to get bonus points?',
        widget=widgets.RadioSelect,
    )

    q5 = models.StringField(
        choices=[['I get 8 points for each player playing "Not Cooperate", if I cooperate.', 'I get 8 points for each player playing "Not Cooperate", if I cooperate.'],\
         ['I get 8 points for each player, if I cooperate', 'I get 8 points for each player, if I cooperate'],\
         ['I get 8 points for each player playing "Cooperate", if I do not cooperate', 'I get 8 points for each player playing "Cooperate", if I do not cooperate']],
        label='Which of the following statements is correct?',
        widget=widgets.RadioSelect,
    )