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
        p_CD = Constants.S #Constants.S + tax/100 * Constants.T
        p_DC = Constants.T #(1-tax/100) * Constants.T
        p_DD = Constants.P #(1-tax/100) * Constants.P
        return dict(tax=int(tax), p_CC=p_CC, p_CD=p_CD, p_DC=p_DC, p_DD=p_DD)

class End(Page):
    def vars_for_template(self):

        # Get player's and bot's decision
        me = self.player
        coin_flip = ['Cooperate','Defect']
        bot_decision = random.choice(coin_flip)

        # Assign tax rate
        tax = Constants.tax_list[me.id_in_group - 1]

        # Get mine and bot's payoff
        if me.decision == 'D':
            my_decision = 'Defect'
            if bot_decision == 'Defect':
                me.payoff = (1 - tax) * Constants.P
                bot_payoff = (1 - tax) * Constants.P
            else:
                me.payoff = (1 - tax) * Constants.T
                bot_payoff = Constants.S + tax * Constants.T
        else:
            my_decision = 'Cooperate'
            if bot_decision == 'Defect':
                me.payoff = Constants.S + tax * Constants.T
                bot_payoff = (1 - tax) * Constants.T
            else:
                me.payoff = Constants.R
                bot_payoff = Constants.R
        
        # Return to template
        return dict(my_decision=my_decision, other_decision=bot_decision, my_payoff=me.payoff, other_payoff=bot_payoff, tax=int(tax*100))


page_sequence = [Decision, End]
