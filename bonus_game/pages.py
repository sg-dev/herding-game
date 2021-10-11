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
        p_CC = int(Constants.R)
        p_CD = int(Constants.S)
        p_DC = int(Constants.T)
        p_DD = int(Constants.P)

        # Last round's info
        if self.player.round_number != 1:
            # Get player's and bot's decision
            me_prev = self.player.in_round(self.player.round_number - 1)

            # Get fraction of defectors
            f_prev = Constants.fractions_ext[me_prev.id_in_group - 1][me_prev.round_number - 1]

            # Number of cooperators and defectors
            n_C = math.ceil((1-f_prev) * Constants.neigh_size)
            n_D = math.floor(f_prev * Constants.neigh_size)

            #print(me_prev.decision)

            # Get number cooperators & defectors and unit payoff per cooperator and defector
            if me_prev.decision == 'D':
                n_C_1 = n_C
                unit_def_payoff = p_DD
                unit_coop_payoff = p_DC
                bonus = 0
                my_decision = "Don't collaborate"
            else:
                n_C_1 = n_C + 1
                unit_def_payoff = p_CD
                unit_coop_payoff = p_CC
                bonus = Constants.bonus * n_D
                my_decision = "Collaborate"

            # Get last round's payoffs
            def_payoff = n_D * unit_def_payoff
            coop_payoff = n_C * unit_coop_payoff
            # my_payoff = me.payoff

            # print('Here: ', my_payoff)

            # Unit bonus
            unit_bonus = Constants.bonus

        else: 
            n_C_1 = -1

            ## Get player's and bot's decision
            me = self.player.in_round(self.player.round_number)
            my_decision = None

            print(my_decision)

            # Get fraction of coops/defs
            print('Here', me.id_in_group, me.round_number)
            f_prev = Constants.fractions_ext[me.id_in_group - 1][me.round_number - 1]

            ## Number of cooperators and defectors
            n_C = math.ceil((1-f_prev) * Constants.neigh_size)
            n_D = math.floor(f_prev * Constants.neigh_size)

            # Payoffs and bonus
            unit_def_payoff = 0
            unit_coop_payoff = 0
            def_payoff = 0
            coop_payoff = 0
            bonus = 0
            unit_bonus = 0

        last_payoff = def_payoff + coop_payoff + bonus
        me.payoff = last_payoff

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
        rand_you = max(Constants.opponents_list[me.id_in_group - 1][:20]) + 1

        # Return to template
        return dict(p_CC=p_CC, p_CD=p_CD, p_DC=p_DC, p_DD=p_DD, n_C=n_C, n_D=n_D, n_C_1=n_C_1, unit_def_payoff = unit_def_payoff,\
            unit_coop_payoff = unit_coop_payoff, def_payoff = def_payoff, coop_payoff = coop_payoff, bonus = bonus, last_payoff = last_payoff, \
            unit_bonus = unit_bonus, my_decision = my_decision,\
            rand1=rand1, rand2=rand2, rand3=rand3, rand4=rand4, rand5=rand5, rand6=rand6, rand7=rand7, rand8=rand8, rand9=rand9, rand10=rand10,\
            rand11=rand11, rand12=rand12, rand13=rand13, rand14=rand14, rand15=rand15, rand16=rand16, rand17=rand17, rand18=rand18, \
            rand19=rand19, rand20=rand20, rand_you=rand_you)

class ResultsWaitPage(Page):
    timeout_seconds = 1#5

# class End(Page):
#     def vars_for_template(self):
#         # Get player's and bot's decision
#         me = self.player
#         coin_flip = ['C','D']
#         bot_decision = random.choice(coin_flip)

#         # Assign fraction of defectors
#         f = Constants.fractions_ext[me.id_in_group - 1][me.round_number - 1]

#         # Number of cooperators and defectors
#         n_C = math.ceil((1-f) * Constants.neigh_size)
#         n_D = math.floor(f * Constants.neigh_size)

#         # Get mine and bot's payoff
#         if me.decision == 'D':
#             me.payoff = float(Constants.P * n_D + Constants.T * n_C)
#             my_decision = 'Not collaborate'
#             def_payoff = me.payoff
#             coop_payoff = float(Constants.R * n_C + Constants.S * n_D)
#             n_C_1 = n_C
#             n_D_1 = n_D + 1
#         else:
#             me.payoff = float(Constants.R * n_C + (Constants.S + Constants.bonus) * n_D)
#             my_decision = 'Collaborate'
#             coop_payoff = me.payoff
#             def_payoff = float(Constants.P * n_D + Constants.T * (n_C + 1))
#             n_C_1 = n_C + 1
#             n_D_1 = n_D

#         # Compute cumulative payoff until the current round
#         cumulative_payoff = me.payoff
#         for p in me.in_previous_rounds():
#             cumulative_payoff += p.payoff
#         cumulative_payoff = float(cumulative_payoff)

#         # Opponents
#         rand1 = Constants.opponents_list[me.id_in_group - 1][0]
#         rand2 = Constants.opponents_list[me.id_in_group - 1][1]
#         rand3 = Constants.opponents_list[me.id_in_group - 1][2]
#         rand4 = Constants.opponents_list[me.id_in_group - 1][3]
#         rand5 = Constants.opponents_list[me.id_in_group - 1][4]
#         rand6 = Constants.opponents_list[me.id_in_group - 1][5]
#         rand7 = Constants.opponents_list[me.id_in_group - 1][6]
#         rand8 = Constants.opponents_list[me.id_in_group - 1][7]
#         rand9 = Constants.opponents_list[me.id_in_group - 1][8]
#         rand10 = Constants.opponents_list[me.id_in_group - 1][9]
#         rand11 = Constants.opponents_list[me.id_in_group - 1][10]
#         rand12 = Constants.opponents_list[me.id_in_group - 1][11]
#         rand13 = Constants.opponents_list[me.id_in_group - 1][12]
#         rand14 = Constants.opponents_list[me.id_in_group - 1][13]
#         rand15 = Constants.opponents_list[me.id_in_group - 1][14]
#         rand16 = Constants.opponents_list[me.id_in_group - 1][15]
#         rand17 = Constants.opponents_list[me.id_in_group - 1][16]
#         rand18 = Constants.opponents_list[me.id_in_group - 1][17]
#         rand19 = Constants.opponents_list[me.id_in_group - 1][18]
#         rand20 = Constants.opponents_list[me.id_in_group - 1][19]
#         rand_you = max(Constants.opponents_list[me.id_in_group - 1][:20]) + 1
        
#         # Return to template
#         return dict(my_decision=my_decision, my_payoff=float(me.payoff), n_C=n_C, n_D=n_D, \
#             n_C_1=n_C_1, n_D_1=n_D_1, bonus=bonus, \
#             coop_payoff=coop_payoff, def_payoff=def_payoff, round_num=me.round_number, \
#             my_cumulative_payoff=cumulative_payoff, \
#             rand1=rand1, rand2=rand2, rand3=rand3, rand4=rand4, rand5=rand5, rand6=rand6, rand7=rand7, rand8=rand8,\
#             rand9=rand9, rand10=rand10, rand11=rand11, rand12=rand12, rand13=rand13, rand14=rand14, rand15=rand15, rand16=rand16, \
#             rand17=rand17, rand18=rand18, rand19=rand19, rand20=rand20, rand_you=rand_you)

class Debrief(Page):
    form_model = 'player'
    form_fields = ['debrief']
    #     if values['debrief'] == '50-75%' or values['debrief'] == '76-100%':
    #         return 'The correct answer is 13.5%, so you were a bit far off :( Good one anyway!'
    #     elif values['debrief'] == '0-10%' or values['debrief'] == '26-50%':
    #         return 'The correct answer is 13.5%, so close but not yet there :| Nice try!'


    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds

class Thanks(Page):
    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds
    def vars_for_template(self):
        # Pass variables to Thanks page
        if self.player.debrief == '0-10%' or self.player.debrief == '76-100%':
            final_message = 'The correct answer is 30%, so you were a bit far off :( Good one anyway!'
        elif self.player.debrief == '11-25%' or self.player.debrief == '51-75%':
            final_message = 'The correct answer is 30%, so close but not yet there :| Nice try!'
        else:
            final_message = 'Yes, you are right: the correct tax rate is 30% :) Great one!'
        
        cumulative_payoff = 0
        for t in range(Constants.num_rounds):
            me = self.player.in_round(self.player.round_number - t)
            cumulative_payoff += me.payoff
            print(me.payoff)
        
        return dict(message = final_message, cumulative_payoff = cumulative_payoff)


page_sequence = [Decision, ResultsWaitPage, Debrief, Thanks]
