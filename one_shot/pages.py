from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Init_WaitPage(WaitPage):
     group_by_arrival_time = False

class Instructions(Page):
    def vars_for_template(self):
        me = self.player
        tax = Constants.tax_list[me.id_in_group - 1] * 100
        return dict(tax=tax)

    def is_displayed(self):
        return self.subsession.round_number == 1

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']


class ResultsWaitPage(WaitPage):
    pass
    #def after_all_players_arrive(self):
        # # Get player's and bot's decision
        # player = self.group.get_players()
        # print(player.decision)
        # coin_flip = ['C','D']
        # bot_decision = random.choice(coin_flip)

        # # Assign tax rate
        # all_players = self.player.get_others_in_subsession()
        # all_players.append(self.player)
        # print(all_players)
        # ext_factor = len(all_players) // len(Constants.alpha)
        # print(ext_factor, ": ext_factor")
        # tax_list = Constants.alpha * ext_factor
        # print(tax_list, ": before shuffling")
        # random.shuffle(tax_list)
        # print(tax_list, ": after shuffling")
        # print(self.group.id, ": group id")
        # tax = tax_list[self.group.id]

        # # Get player's and bot's payoff
        # if player.decision == 'D':
        #     if bot_decision == 'D':
        #         player.payoff = (1 - tax) * Constants.P
        #         bot_payoff = (1 - tax) * Constants.P
        #     else:
        #         player.payoff = (1 - tax) * Constants.T
        #         bot_payoff = Constants.S + tax * Constants.T
        # else:
        #     if bot_decision == 'D':
        #         player.payoff = Constants.S + tax * Constants.T
        #         bot_payoff = (1 - tax) * Constants.T
        #     else:
        #         player.payoff = Constants.R
        #         bot_payoff = Constants.R

class Results(Page):
    pass

class End(Page):
    def vars_for_template(self):
        # Get all players
        # all_players = self.group.get_players()
        # #all_players.append(self.player)
        # print(all_players)

        # Get player's and bot's decision
        me = self.player
        #print(me.decision, ": my decision")
        coin_flip = ['C','D']
        bot_decision = random.choice(coin_flip)
        #print(bot_decision, ": bot decision")

        # Assign tax rate
        # ext_factor = len(all_players) // len(Constants.alpha)
        # print(ext_factor, ": ext_factor")
        # tax_list = Constants.alpha * ext_factor
        # print(tax_list, ": before shuffling")
        # random.shuffle(tax_list)
        # print(tax_list, ": after shuffling")
        # print(me.id_in_group, ": group id")
        # tax = tax_list[me.id_in_group - 1]

        #print(me.id_in_group, ": group id")
        tax = Constants.tax_list[me.id_in_group - 1]
        #print(tax)

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


page_sequence = [Instructions, Decision, End]#[Init_WaitPage, Decision, ResultsWaitPage, Results, End]
