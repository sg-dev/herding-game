from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class Instructions1(Page):
	pass

class Instructions2(Page):
	pass

class Attention1(Page):
	timeout_seconds = 180
	form_model = 'player'
	form_fields = ['q1', 'q2', 'q3']

	def error_message(player, values):
		if values['q1'] != 'Collaborating players' or values['q2'] != 'No' or values['q3'] != '5':
			return 'Wrong answer, try again.'

# class Attention2(Page):
#     form_model = 'player'
#     form_fields = ['q1', 'q2']

#     def error_message(player, values):
#     	if values['q1'] == 'I would Defect':
#     		return 'Wrong answer, try again.'
#     	if values['q2'] == 'I would Cooperate':
#     		return 'Wrong answer, try again.'


page_sequence = [Instructions1, Attention1]#, Instructions2, Attention2]