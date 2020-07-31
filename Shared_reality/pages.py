
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class intro(Page):
    form_model = 'player'
    
class SRG(Page):
    form_model = 'player'
    form_fields = ['SRG_1', 'SRG_2', 'SRG_3', 'SRG_4', 'SRG_5', 'SRG_6', 'SRG_7', 'SRG_8']
    
class CO_CON(Page):
    form_model = 'player'
    form_fields = ['CO_CON_1', 'CO_CON_2', 'CO_CON_3', 'CO_CON_4', 'CO_CON_5']
    
class SRT(Page):
    form_model = 'player'
    form_fields = ['SRT_1', 'SRT_2']
    
class IOS(Page):
    form_model = 'player'
    form_fields = ['IOS_1']

class epist(Page):
    form_model = 'player'
    form_fields = ['Epist_1', 'Epist_2', 'Epist_3']

class click(Page):
    form_model = 'player'
    form_fields = ['Click']

class relate(Page):
    form_model = 'player'
    form_fields = ['rel_1', 'rel_2']

class resp(Page):
    form_model = 'player'
    form_fields = ['resp_1', 'resp_2', 'resp_3']

class sim(Page):
    form_model = 'player'
    form_fields = ['sim_1', 'sim_2', 'sim_3', 'sim_4', 'sim_5']

class rap(Page):
    form_model = 'player'
    form_fields = ['rap_1', 'rap_2', 'rap_3', 'rap_4', 'rap_5', 'rap_6', 'rap_7', 'rap_8', 'rap_9', 'rap_10']

class cert(Page):
    form_model = 'player'
    form_fields = ['cert_1', 'cert_2', 'cert_3']

class open(Page):
    form_model = 'player'
    form_fields = ['open_1', 'reflect']

page_sequence = [intro, cert, sim, click, SRG, IOS, SRT, epist, relate, open]
