
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Consent(Page):
    form_model = 'player'
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
page_sequence = [Consent, MyWaitPage_1, Screen_setting, Icebreaker, MyWaitPage_2]
