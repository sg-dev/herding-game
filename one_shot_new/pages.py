from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']

    def vars_for_template(self):
        me = self.player
        tax = Constants.tax_list[me.id_in_group - 1] * 100
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
        tax = Constants.tax_list[me.id_in_group - 1]

        # Get mine and bot's payoff
        if me.decision == 'D':
            if bot_decision == 'D':
                me.payoff = (1 - tax) * Constants.P
                bot_payoff = (1 - tax) * Constants.P
            else:
                me.payoff = (1 - tax) * Constants.T
                bot_payoff = Constants.S + tax * Constants.T
        else:
            if bot_decision == 'D':
                me.payoff = Constants.S + tax * Constants.T
                bot_payoff = (1 - tax) * Constants.T
            else:
                me.payoff = Constants.R
                bot_payoff = Constants.R
        
        # Return to template
        return dict(my_decision=me.decision, other_decision=bot_decision, my_payoff=me.payoff, other_payoff=bot_payoff, tax=tax)


page_sequence = [Decision, End]
