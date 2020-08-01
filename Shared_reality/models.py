
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'Shared_reality_questions'
    players_per_group = None
    num_rounds = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    highest_bidder = models.IntegerField()
    highest_bid = models.IntegerField()
    def my_method(self):
        pass
class Player(BasePlayer):
    my_field = models.StringField()
    SRG_1 = models.StringField()
    SRG_2 = models.StringField()
    SRG_3 = models.StringField()
    SRG_4 = models.StringField()
    SRG_5 = models.StringField()
    SRG_6 = models.StringField()
    SRG_7 = models.StringField()
    SRG_8 = models.StringField()
    SRT_1 = models.StringField()
    SRT_2 = models.StringField()
    IOS_1 = models.StringField()
    Epist_1 = models.StringField()
    Epist_2 = models.StringField()
    Epist_3 = models.StringField()
    Click = models.StringField()
    rel_1 = models.StringField()
    rel_2 = models.StringField()
    sim_1 = models.StringField()
    sim_2 = models.StringField()
    sim_3 = models.StringField()
    sim_4 = models.StringField()
    sim_5 = models.StringField()
    rap_1 = models.StringField()
    rap_2 = models.StringField()
    rap_3 = models.StringField()
    rap_4 = models.StringField()
    rap_5 = models.StringField()
    rap_6 = models.StringField()
    rap_7 = models.StringField()
    rap_8 = models.StringField()
    rap_9 = models.StringField()
    rap_10 = models.StringField()
    cert_1 = models.StringField()
    cert_2 = models.StringField()
    cert_3 = models.StringField()
    open_1 = models.StringField()
    reflect = models.LongStringField()

