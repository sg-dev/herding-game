from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class Instructions1(Page):
	pass

class Instructions2(Page):
	pass

class Attention1(Page):
    form_model = 'player'
    form_fields = ['tax', 'bonus']

class Attention2(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2']


page_sequence = [Instructions1, Attention1, Instructions2, Attention2]