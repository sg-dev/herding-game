from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class Instructions(Page):
	pass


class Comprehension(Page):
	timeout_seconds = 180
	form_model = 'player'
	form_fields = ['q1', 'q2', 'q3']

	def error_message(player, values):
		if values['q1'] != 'Collaborating players' or values['q2'] != 'No' or values['q3'] != '5':
			return 'Wrong answer, try again.'


page_sequence = [Instructions, Comprehension]
