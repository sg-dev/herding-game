from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import math

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']

    def vars_for_template(self):
        me = self.player
        tax = Constants.alpha_f_list[me.id_in_group - 1][0] * 100
        p_CC = Constants.R
        p_CD = Constants.S + tax/100 * Constants.T
        p_DC = (1-tax/100) * Constants.T
        p_DD = (1-tax/100) * Constants.P
        return dict(tax=tax, p_CC=p_CC, p_CD=p_CD, p_DC=p_DC, p_DD=p_DD)

class End(Page):
    def vars_for_template(self):
        # Get player's and bot's decision
        me = self.player
        coin_flip = ['C','D']
        bot_decision = random.choice(coin_flip)

        # Assign tax rate
        tax = Constants.alpha_f_list[me.id_in_group - 1][0]
        f = Constants.alpha_f_list[me.id_in_group - 1][1]

        # Number of cooperators and defectors
        n_C = math.ceil((1-f) * Constants.neigh_size)
        n_D = math.floor(f * Constants.neigh_size)

        # Get mine and bot's payoff
        if me.decision == 'D':
            me.payoff = (1 - tax) * Constants.P * n_D + (1 - tax) * Constants.T * n_C
        else:
            me.payoff = (Constants.S + tax * Constants.T) * n_D + Constants.R * n_C
        
        # Return to template
        return dict(my_decision=me.decision, my_payoff=me.payoff, n_C=n_C, n_D=n_D, tax=tax)


page_sequence = [Decision, End]
