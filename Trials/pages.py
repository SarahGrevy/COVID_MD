
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random, os

class Stimuli(Page):
    form_model = 'player'
    def vars_for_template(self):
            return self.player.vars_for_template()

class Judgement_1(Page):
    form_model = 'player'
    form_fields = ['judgement1']
    def vars_for_template(self):
            return self.player.vars_for_template()


class Certainty_1(Page):
    form_model = 'player'
    form_fields = ['certainty1']

class MyWaitPage_2(WaitPage):

    pass
class Discussion_1(Page):
    form_model = 'player'
    live_method = "live_slider"
    def vars_for_template(self):
            return self.player.vars_for_template()



class Wavelength(Page):
    form_model = 'player'
    form_fields = ['PartnerAgreement']
    def vars_for_template(self):
            return self.player.vars_for_template()


class Judgement_2(Page):
    form_model = 'player'
    form_fields = ['judgement2']
    def vars_for_template(self):
            return self.player.vars_for_template()


class Certainty_2(Page):
    form_model = 'player'
    form_fields = ['certainty2']

class MyWaitPage_3(WaitPage):
    pass

class Stimuli_Rewatch(Page):
    form_model = 'player'
    def vars_for_template(self):
            return self.player.vars_for_template()

class Judgement_3(Page):
    form_model = 'player'
    form_fields = ['judgement3']
    def vars_for_template(self):
            return self.player.vars_for_template()

class Certainty_3(Page):
    form_model = 'player'
    form_fields = ['certainty3']

class MyWaitPage_4(WaitPage):
    pass



## SHARED REALITY QUESTIONS
class IOS(Page):
    def is_displayed(self):
        return self.round_number == 3 or self.round_number == 6
    form_model = 'player'
    form_fields = ['IOS_1']
    def vars_for_template(self):
            return self.player.vars_for_template()

class P_QUESTIONS_0(Page):
    def is_displayed(self):
       return self.round_number == 3 or self.round_number == 6 # Page will show on round 3 and 6 only
    form_model = 'player'

class P_QUESTIONS_1(Page):
    def is_displayed(self):
        return self.round_number == 3 or self.round_number == 6
    form_model = 'player'
    form_fields = ['PQ_1', 'PQ_2', 'PQ_3', 'PQ_4']


class P_QUESTIONS_2(Page):
    def is_displayed(self):
        return self.round_number == 3 or self.round_number == 6
    form_model = 'player'
    form_fields = ['PQ_5', 'PQ_6', 'PQ_7', 'PQ_8', 'PQ_9', 'PQ_10']

class MyWaitPage_5(WaitPage):
    def is_displayed(self):
        return self.round_number == 3 or self.round_number == 6
#page_sequence = [Stimuli]
page_sequence = [Stimuli, Judgement_1, Certainty_1, MyWaitPage_2, Discussion_1, Wavelength, Judgement_2, Certainty_2, MyWaitPage_3, Stimuli_Rewatch, Judgement_3, Certainty_3, MyWaitPage_4, P_QUESTIONS_0, P_QUESTIONS_1, IOS, P_QUESTIONS_2, MyWaitPage_5]












