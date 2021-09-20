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
        p_CD = int(Constants.S)
        p_DC = int(Constants.T)
        p_DD = int(Constants.P)

        # Last round's info
        if self.player.round_number != 1:
            ## Get player's and bot's decision
            me = self.player.in_round(self.player.round_number - 1)

            # Get fraction of coops/defs
            f = Constants.alpha_f_list[me.id_in_group - 1][1][me.round_number - 1]

            ## Number of cooperators and defectors
            n_C = math.ceil((1-f) * Constants.neigh_size)
            n_D = math.floor(f * Constants.neigh_size)

            ## Get mine and bot's payoff
            if me.decision == 'D':
                n_C_1 = n_C
            else:
                n_C_1 = n_C + 1
        else: 
            #n_C = -1
            n_C_1 = -1
            #n_D = -1
            ## Get player's and bot's decision
            me = self.player.in_round(self.player.round_number)

            # Get fraction of coops/defs
            f = Constants.alpha_f_list[me.id_in_group - 1][1][me.round_number - 1]

            ## Number of cooperators and defectors
            n_C = math.ceil((1-f) * Constants.neigh_size)
            n_D = math.floor(f * Constants.neigh_size)

        # Opponents
        rand1 = Constants.opponents_list[me.id_in_group - 1][0]
        rand2 = Constants.opponents_list[me.id_in_group - 1][1]
        rand3 = Constants.opponents_list[me.id_in_group - 1][2]
        rand4 = Constants.opponents_list[me.id_in_group - 1][3]
        rand5 = Constants.opponents_list[me.id_in_group - 1][4]
        rand6 = Constants.opponents_list[me.id_in_group - 1][5]
        rand7 = Constants.opponents_list[me.id_in_group - 1][6]
        rand8 = Constants.opponents_list[me.id_in_group - 1][7]
        rand9 = Constants.opponents_list[me.id_in_group - 1][8]
        rand10 = Constants.opponents_list[me.id_in_group - 1][9]
        rand11 = Constants.opponents_list[me.id_in_group - 1][10]
        rand12 = Constants.opponents_list[me.id_in_group - 1][11]
        rand13 = Constants.opponents_list[me.id_in_group - 1][12]
        rand14 = Constants.opponents_list[me.id_in_group - 1][13]
        rand15 = Constants.opponents_list[me.id_in_group - 1][14]
        rand16 = Constants.opponents_list[me.id_in_group - 1][15]
        rand17 = Constants.opponents_list[me.id_in_group - 1][16]
        rand18 = Constants.opponents_list[me.id_in_group - 1][17]
        rand19 = Constants.opponents_list[me.id_in_group - 1][18]
        rand20 = Constants.opponents_list[me.id_in_group - 1][19]
        rand_you = max(Constants.opponents_list[me.id_in_group - 1][:20]) + 1#Constants.opponents_list[me.id_in_group - 1][20]

        # Return to template
        return dict(tax=int(tax), p_CC=p_CC, p_CD=p_CD, p_DC=p_DC, p_DD=p_DD, n_C=n_C, n_D=n_D, n_C_1=n_C_1, \
            rand1=rand1, rand2=rand2, rand3=rand3, rand4=rand4, rand5=rand5, rand6=rand6, rand7=rand7, rand8=rand8,\
            rand9=rand9, rand10=rand10, rand11=rand11, rand12=rand12, rand13=rand13, rand14=rand14, rand15=rand15, rand16=rand16, \
            rand17=rand17, rand18=rand18, rand19=rand19, rand20=rand20, rand_you=rand_you)

class ResultsWaitPage(Page):
    timeout_seconds = 5

class End(Page):
    def vars_for_template(self):
        # Get player's and bot's decision
        me = self.player
        coin_flip = ['C','D']
        bot_decision = random.choice(coin_flip)

        print("ROUND", me.round_number - 1)

        # Assign tax rate
        tax = Constants.alpha_f_list[me.id_in_group - 1][0]
        f = Constants.alpha_f_list[me.id_in_group - 1][1][me.round_number - 1]

        # Number of cooperators and defectors
        n_C = math.ceil((1-f) * Constants.neigh_size)
        n_D = math.floor(f * Constants.neigh_size)

        # Get mine and bot's payoff
        if me.decision == 'D':
            init = float(Constants.P * n_D + Constants.T * n_C)
            init_C = float(Constants.R * n_C + Constants.S * n_D)
            bonus = 0
            if n_C != 0:
                bonus_coop = float((tax*init_C*n_C + tax*init*(n_D+1))/(n_C))
            else:
                bonus_coop = 0
            print("bonus coop", bonus_coop)
            me.payoff = (1 - tax) * init#(1 - tax) * Constants.P * n_D + (1 - tax) * Constants.T * n_C
            my_decision = 'Not collaborate'
            #coop_payoff = float(Constants.R * (n_C - 1) + Constants.S * (n_D + 1))
            coop_payoff = init_C
            def_payoff = float(init)
            n_C_1 = n_C
            n_D_1 = n_D + 1
        else:
            init = float(Constants.R * n_C + Constants.S * n_D)
            init_D = float(Constants.P * n_D + Constants.T * n_C)
            bonus = float((tax*init*(n_C + 1) + tax*init_D*n_D)/(n_C + 1))
            bonus_coop = bonus
            me.payoff = (1 - tax)*init + bonus#(Constants.S + tax * Constants.T) * n_D + Constants.R * n_C
            my_decision = 'Collaborate'
            print("bonus coop", bonus_coop)
            coop_payoff = float(init)
            def_payoff = float(Constants.P * n_D + Constants.T * (n_C + 1))
            n_C_1 = n_C + 1
            n_D_1 = n_D

        #delta = abs(me.payoff - (1 - tax) * init)

        cumulative_payoff = me.payoff
        for p in me.in_previous_rounds():
            cumulative_payoff += p.payoff
        cumulative_payoff = float(cumulative_payoff)

        # Opponents
        rand1 = Constants.opponents_list[me.id_in_group - 1][0]
        rand2 = Constants.opponents_list[me.id_in_group - 1][1]
        rand3 = Constants.opponents_list[me.id_in_group - 1][2]
        rand4 = Constants.opponents_list[me.id_in_group - 1][3]
        rand5 = Constants.opponents_list[me.id_in_group - 1][4]
        rand6 = Constants.opponents_list[me.id_in_group - 1][5]
        rand7 = Constants.opponents_list[me.id_in_group - 1][6]
        rand8 = Constants.opponents_list[me.id_in_group - 1][7]
        rand9 = Constants.opponents_list[me.id_in_group - 1][8]
        rand10 = Constants.opponents_list[me.id_in_group - 1][9]
        rand11 = Constants.opponents_list[me.id_in_group - 1][10]
        rand12 = Constants.opponents_list[me.id_in_group - 1][11]
        rand13 = Constants.opponents_list[me.id_in_group - 1][12]
        rand14 = Constants.opponents_list[me.id_in_group - 1][13]
        rand15 = Constants.opponents_list[me.id_in_group - 1][14]
        rand16 = Constants.opponents_list[me.id_in_group - 1][15]
        rand17 = Constants.opponents_list[me.id_in_group - 1][16]
        rand18 = Constants.opponents_list[me.id_in_group - 1][17]
        rand19 = Constants.opponents_list[me.id_in_group - 1][18]
        rand20 = Constants.opponents_list[me.id_in_group - 1][19]
        rand_you = max(Constants.opponents_list[me.id_in_group - 1][:20]) + 1#Constants.opponents_list[me.id_in_group - 1][20]

        print(n_C)

        pot = tax * (n_C_1 * coop_payoff + n_D_1 * def_payoff)
        
        # Return to template
        return dict(init=init, my_decision=my_decision, my_payoff=float(me.payoff), n_C=n_C, n_D=n_D, \
            n_C_1=n_C_1, n_D_1=n_D_1, tax=float(tax*100), bonus=bonus, bonus_coop=round(bonus_coop, 1), \
            coop_payoff=coop_payoff, def_payoff=def_payoff, round_num=me.round_number, \
            my_cumulative_payoff=cumulative_payoff, \
            rand1=rand1, rand2=rand2, rand3=rand3, rand4=rand4, rand5=rand5, rand6=rand6, rand7=rand7, rand8=rand8,\
            rand9=rand9, rand10=rand10, rand11=rand11, rand12=rand12, rand13=rand13, rand14=rand14, rand15=rand15, rand16=rand16, \
            rand17=rand17, rand18=rand18, rand19=rand19, rand20=rand20, rand_you=rand_you, pot=round(pot, 1))

class Debrief(Page):
    form_model = 'player'
    form_fields = ['debrief']

    def error_message(player, values):
        if values['debrief'] == '50-75%' or values['debrief'] == '76-100%':
            return 'The correct answer is 13.5%, so you were a bit far off :( Good one anyway!'
        elif values['debrief'] == '0-10%' or values['debrief'] == '26-50%':
            return 'The correct answer is 13.5%, so close but not yet there :| Nice try!'


    def is_displayed(self):
        return self.player.round_number == 5

class Thanks(Page):
    def is_displayed(self):
        return self.player.round_number == 5

page_sequence = [Decision, ResultsWaitPage, End, Debrief, Thanks]
