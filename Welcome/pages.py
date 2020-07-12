
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Consent(Page):
    form_model = 'player'
class Welcome(Page):
    form_model = 'player'
class Zoom(Page):
    form_model = 'player'
class Icebreaker(Page):
    form_model = 'player'
class MyWaitPage_1(WaitPage):
    pass
class MyWaitPage_2(WaitPage):
    pass
page_sequence = [Consent, Welcome, Zoom, MyWaitPage_1, Icebreaker, MyWaitPage_2]