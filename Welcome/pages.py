
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Consent(Page):
    form_model = 'player'
class Global_1(Page):
    form_model = 'player'
    form_fields = ['pre_global_1']
class Global_2(Page):
    form_model = 'player'
    form_fields = ['pre_global_2']
class Global_3(Page):
    form_model = 'player'
    form_fields = ['pre_global_3']
class Specific_2(Page):
    form_model = 'player'
    form_fields = ['goverment']    
class Zoom(Page):
    form_model = 'player'
class Screen_setting(Page):
    form_model = 'player'    
class Icebreaker(Page):
    form_model = 'player'
class MyWaitPage_1(WaitPage):
    pass
class MyWaitPage_2(WaitPage):
    pass
class MyWaitPage_3(WaitPage):
    pass
page_sequence = [Consent, MyWaitPage_1, Global_1, Global_2, Global_3, Specific_2, MyWaitPage_2, Screen_setting, Icebreaker, MyWaitPage_2]
