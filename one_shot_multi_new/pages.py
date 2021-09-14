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
        p_CC = int(Constants.R)
        p_CD = int(Constants.S)#Constants.S + tax/100 * Constants.T
        p_DC = int(Constants.T)#(1-tax/100) * Constants.T
        p_DD = int(Constants.P)#(1-tax/100) * Constants.P
        return dict(tax=int(tax), p_CC=p_CC, p_CD=p_CD, p_DC=p_DC, p_DD=p_DD)

class ResultsWaitPage(Page):
    timeout_seconds = 5

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
            init = int(Constants.P * n_D + Constants.T * n_C)
            init_C = int(Constants.R * n_C + Constants.S * n_D)
            bonus = 0
            if n_C != 0:
                bonus_coop = int((tax*init_C*n_C + tax*init*n_D)//(n_C))
            else:
                bonus_coop = 0
            me.payoff = (1 - tax) * init#(1 - tax) * Constants.P * n_D + (1 - tax) * Constants.T * n_C
            my_decision = 'Not collaborate'
            coop_payoff = int(Constants.R * (n_C - 1) + Constants.S * (n_D + 1))
            def_payoff = int(init)
            n_C_1 = n_C
            n_D_1 = n_D + 1
        else:
            init = int(Constants.R * n_C + Constants.S * n_D)
            init_D = int(Constants.P * n_D + Constants.T * n_C)
            bonus = int((tax*init*(n_C + 1) + tax*init_D*n_D)//(n_C + 1))
            bonus_coop = bonus
            me.payoff = (1 - tax)*init + bonus#(Constants.S + tax * Constants.T) * n_D + Constants.R * n_C
            my_decision = 'Collaborate'
            coop_payoff = int(init)
            def_payoff = int(Constants.P * (n_D - 1) + Constants.T * (n_C + 1))
            n_C_1 = n_C + 1
            n_D_1 = n_D
        
        # Return to template
        return dict(init=init, my_decision=my_decision, my_payoff=int(me.payoff), n_C=n_C, n_D=n_D, n_C_1=n_C_1, n_D_1=n_D_1, tax=int(tax*100), bonus=bonus, bonus_coop=bonus_coop, coop_payoff=coop_payoff, def_payoff=def_payoff)

class Debrief(Page):
    form_model = 'player'
    form_fields = ['debrief']

class Thanks(Page):
    pass

page_sequence = [Decision, ResultsWaitPage, End, Debrief, Thanks]
