from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class Instructions1(Page):
    pass

class Instructions2(Page):
    pass


class Attention1(Page):
    timeout_seconds = 1080
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5']

    def error_message(player, values):
        q = {
            'q1': 1,
            'q2': 8,
            'q3': 2,
            'q4': 1,
            'q5': 1
            }
        incorrect = []
        for q_name, q_text in q.items():
            if values[q_name] != str(q_text):
                incorrect.append(q_name[1:])
        if incorrect:
            return f'Please correct your answers to questions {", ".join(incorrect)}.'

        else:
            return None


class InterimWaitPage(Page):
    timeout_seconds = 1 # Change as you wish (for realistic view purposes)


page_sequence = [Instructions1, Attention1, InterimWaitPage]#, Instructions2, Attention2]
