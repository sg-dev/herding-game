from otree.api import Currency as c

from ._builtin import Page, WaitPage
from .models import Constants


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
            "is_in_deception_regime": self.participant.in_deception,
        }

    def js_vars(self):
        return {
            "neigh_size": Constants.n_players,
            "nC": 10,
            "secAnimation": 0.2,
            "shuffle": False,
            "skip": 0,
            "is_in_deception_regime": self.participant.in_deception,
        }


class Instructions_points(Page):
    def vars_for_template(self):
        return {
            "R": Constants.R,
            "S": Constants.S,
            "T": Constants.T,
            "P": Constants.P,
            "bonus": Constants.bonus,
            "Rx8": Constants.R * 8,
            "Sx12": Constants.S * 12,
            "value_of_200_points": c(200).to_real_world_currency(self.session),
            "is_in_deception_regime": self.participant.in_deception,
        }


class Instructions_example_round(Page):
    def vars_for_template(self):
        return {
            "R": Constants.R,
            "S": Constants.S,
            "T": Constants.T,
            "P": Constants.P,
            "bonus": Constants.bonus,
            "Rx8": Constants.R * 8,
            "Sx12": Constants.S * 12,
            "bonusx12": Constants.bonus * 12,
            "Rx8pSx12": Constants.R * 8 + Constants.S * 12,
            "Rx8pSx12pbonusx12": Constants.R * 8
            + Constants.S * 12
            + Constants.bonus * 12,
            "Tx8": Constants.T * 8,
            "Px12": Constants.P * 12,
            "Tx8pPx12": Constants.T * 8 + Constants.P * 12,
            "is_in_deception_regime": self.participant.in_deception,
        }

    def js_vars(self):
        return {
            "neigh_size": Constants.n_players,
            "nC": 8,
            "secAnimation": 0,
            "shuffle": False,
            "skip": 0,
        }


class Instructions_next_steps(Page):
    def vars_for_template(self):
        return {
            "is_in_deception_regime": self.participant.in_deception,
        }


class Start_game(Page):
    pass


class Attention1(Page):
    timeout_seconds = 60 * 7
    form_model = "player"
    form_fields = ["q1", "q2", "q3", "q4", "q5"]

    def vars_for_template(self):
        return {
            "R": Constants.R,
            "S": Constants.S,
            "T": Constants.T,
            "P": Constants.P,
            "bonus": Constants.bonus,
            "is_in_deception_regime": self.participant.in_deception,
        }

    def js_vars(self):
        return {
            "neigh_size": Constants.n_players,
            "nC": 10,
            "secAnimation": 0,
            "shuffle": False,
            "skip": 0,
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


page_sequence = [
    Instructions_setting,
    Instructions_points,
    Instructions_example_round,
    Instructions_next_steps,
    Attention1,
    Start_game,
]
