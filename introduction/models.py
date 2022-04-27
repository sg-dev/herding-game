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
    R = c(6)  # Both cooperating
    S = c(0)  # The one cooperating and the other defecting
    T = c(10)  # The one defecting and the other cooperating
    P = c(0)  # Both defecting

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
            [1, "1 action against all other players."],
            [2, f"1 for every player. {Constants.n_players} in total."],
            [3, "No choice, it is automatic."],
            [4, f"2 for every player. {2*Constants.n_players} in total."],
        ],
        label="<strong>Q1:</strong> In each round, how many actions do you choose?",
        widget=widgets.RadioSelect,
    )

    q2 = models.StringField(
        choices=[
            [
                1,
                f"{Constants.R}*{Constants.n_players}={Constants.R*Constants.n_players}",
            ],
            [
                3,
                f"{Constants.bonus}*{Constants.n_players}={Constants.bonus*Constants.n_players}",
            ],
            [
                5,
                f"{Constants.S}*{Constants.n_players}={Constants.S*Constants.n_players}",
            ],
            [
                8,
                f"{Constants.T}*{Constants.n_players}={Constants.T*Constants.n_players}",
            ],  # correct
        ],
        label=f"<strong>Q2:</strong> In the payoff matrix above. If you choose <b>D</b> and {Constants.n_players} players choose <b>C</b> what is your payoff?",
        widget=widgets.RadioSelect,
    )

    q3 = models.StringField(
        choices=[
            [1, "Choice of other players in the current round"],
            [2, "Choice of other players in the previous round"],
            [4, "Choice of other players in the next round"],
            [4, "My choices up to now"],
        ],
        label="<strong>Q3:</strong> What does the colour and letter in the summary figure show?",
        widget=widgets.RadioSelect,
    )

    q4 = models.StringField(
        choices=[[1, "C"], [2, "D"], [3, "C and D"], [4, "Neither C nor D"]],
        label="<strong>Q4:</strong> Which choice entitles you to get bonus points?",
        widget=widgets.RadioSelect,
    )

    q5 = models.StringField(
        choices=[
            [
                1,
                f'I get an extra {Constants.bonus} for each player choosing "D" if I choose "C".',
            ],
            [2, f'I get an extra {Constants.R} per player choosing "C".'],
            [
                3,
                f'I get an extra {Constants.S} per player choosing "C" if I choose "D".',
            ],
        ],
        label="<strong>Q5:</strong> Which of the following statements is correct?",
        widget=widgets.RadioSelect,
    )
