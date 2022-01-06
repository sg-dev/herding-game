from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
)


class Constants(BaseConstants):
    name_in_url = "introduction"
    players_per_group = None
    num_rounds = 1
    # Payoffs
    R = c(7)  # Both cooperating
    S = c(0)  # The one cooperating and the other defecting
    T = c(10)  # The one defecting and the other cooperating
    P = c(1)  # Both defecting

    # Bonus for cooperators
    bonus = c(4)

    # Bonus for cooperators
    bonus = c(4)
    n_players = 20


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.StringField(
        choices=[
            [1, "I chose one single action to be played against all other players."],
            [2, "I chose an action for every player (20 in total)."],
            [3, "I do not choose anything."],
        ],
        label="<strong>Q1:</strong> In each round, how many actions do you choose?",
        widget=widgets.RadioSelect,
    )

    q2 = models.StringField(
        choices=[
            [1, Constants.bonus],
            [3, Constants.R],
            [5, Constants.S],
            [8, Constants.T],
        ],
        label="<strong>Q2:</strong> In the payoff matrix if you choose Not Collaborate and one opponent chooses Collaborate what is your payoff?",
        widget=widgets.RadioSelect,
    )

    q3 = models.StringField(
        choices=[
            [1, "Choice of other players in the current round"],
            [2, "Choice of other players in the last round"],
        ],
        label="<strong>Q3:</strong> What does the colour and letter in the summary figure show?",
        widget=widgets.RadioSelect,
    )

    q4 = models.StringField(
        choices=[[1, "Cooperate"], [2, "Not Cooperate"], [3, "Any"]],
        label="<strong>Q4:</strong> Which choice entitles you to get bonus points?",
        widget=widgets.RadioSelect,
    )

    q5 = models.StringField(
        choices=[
            [
                1,
                f'I get an extra {Constants.bonus} for each player playing "Not Cooperate" if I chose "Cooperate".',
            ],
            [2, f'I get an extra {Constants.T} per player choosing "Cooperate".'],
            [
                3,
                f'I get an extra {Constants.bonus} per player choosing "Cooperate" if I choose "Not cooperate".',
            ],
        ],
        label="<strong>Q5:</strong> Which of the following statements is correct?",
        widget=widgets.RadioSelect,
    )
