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
	form_fields = ['q1', 'q2', 'q3', 'q4', 'q5']

	def error_message(player, values):
		if values['q1'] != 'I choose one single action to be played against all other players.' or values['q2'] != '8' or \
		values['q3'] != 'Choice of other players in the last round' or values['q4'] != 'Cooperate' or \
		values['q5'] != 'I get 8 points for each player playing "Not Cooperate", if I cooperate.':
			return 'Wrong answer, try again.'

# class Attention2(Page):
#     form_model = 'player'
#     form_fields = ['q1', 'q2']

#     def error_message(player, values):
#     	if values['q1'] == 'I would Defect':
#     		return 'Wrong answer, try again.'
#     	if values['q2'] == 'I would Cooperate':
#     		return 'Wrong answer, try again.'

class InterimWaitPage(Page):
    timeout_seconds = 1 # Change as you wish (for realistic view purposes)


page_sequence = [Instructions1, Attention1, InterimWaitPage]#, Instructions2, Attention2]