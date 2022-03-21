from otree.api import Currency as c

from ._builtin import Page, WaitPage
from .models import Constants


class Instructions1(Page):
    def vars_for_template(self):
        return {
            "R": Constants.R,
            "S": Constants.S,
            "T": Constants.T,
            "P": Constants.P,
            "bonus": Constants.bonus,
            "Rx3": Constants.R * 3,
            "Sx17": Constants.S * 17,
        }


class Instructions_setting(Page):
    def vars_for_template(self):
        return {
            "R": Constants.R,
            "S": Constants.S,
            "T": Constants.T,
            "P": Constants.P,
            "bonus": Constants.bonus,
            "n_C": 10,
            "n_D": 10,
            "n_C_1": 9,
        }

    def js_vars(self):
        return {
            "neigh_size": Constants.n_players,
            "nC": 10,
            "secAnimation": 0.2,
            "shuffle": False,
            "skip": 0,
        }


class Instructions_points(Page):
    def vars_for_template(self):
        return {
            "R": Constants.R,
            "S": Constants.S,
            "T": Constants.T,
            "P": Constants.P,
            "bonus": Constants.bonus,
            "Rx3": Constants.R * 3,
            "Sx17": Constants.S * 17
        }


class Instructions_example_round(Page):
    def vars_for_template(self):
        return {
            "R": Constants.R,
            "S": Constants.S,
            "T": Constants.T,
            "P": Constants.P,
            "bonus": Constants.bonus,
            "Rx3": Constants.R * 3,
            "Sx17": Constants.S * 17,
            "bonusx17": Constants.bonus * 17,
            "Rx3pSx17": Constants.R * 3 + Constants.S * 17,
            "Rx3pSx17pbonusx17": Constants.R * 3
            + Constants.S * 17
            + Constants.bonus * 17,
            "Tx3": Constants.T * 3,
            "Px17": Constants.P * 17,
            "Tx3pPx17": Constants.T * 3 + Constants.P * 17,
            "value_of_200_points": c(200).to_real_world_currency(self.session)
        }

    def js_vars(self):
        return {
            "neigh_size": Constants.n_players,
            "nC": 3,
            "secAnimation": 0,
            "shuffle": False,
            "skip": 0,
        }


class Instructions_next_steps(Page):
    pass


class Start_game(Page):
    pass


class Attention1(Page):
    timeout_seconds = 1080
    form_model = "player"
    form_fields = ["q1", "q2", "q3", "q4", "q5"]

    def vars_for_template(self):
        return {
            "R": Constants.R,
            "S": Constants.S,
            "T": Constants.T,
            "P": Constants.P,
            "bonus": Constants.bonus,
        }

    def error_message(self, values):
        q = {"q1": 1, "q2": 8, "q3": 2, "q4": 1, "q5": 1}
        incorrect = []
        for q_name, q_text in q.items():
            if values[q_name] != str(q_text):
                incorrect.append(q_name[1:])
        if incorrect:
            return f'Please correct your answers to questions: {", ".join(incorrect)}.'
        else:
            return None


class InterimWaitPage(Page):
    timeout_seconds = 1  # Change as you wish (for realistic view purposes)


page_sequence = [
    # Instructions1,
    Instructions_setting,
    Instructions_points,
    Instructions_example_round,
    Instructions_next_steps,
    Attention1,
    Start_game,
]
