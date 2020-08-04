
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Specific(Page):
    form_model = 'player'
    form_fields = ['state','covid','pay_cut','news_source']
class Specific_2(Page):
    form_model = 'player'
    form_fields = ['goverment']    
class Global_1(Page):
    form_model = 'player'
    form_fields = ['post_global_1']
class Global_2(Page):
    form_model = 'player'
    form_fields = ['post_global_2']
class Global_3(Page):
    form_model = 'player'
    form_fields = ['post_global_3']

page_sequence = [Specific, Global_1, Global_2, Global_3]
