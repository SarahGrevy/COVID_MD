
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'Welcome'
    players_per_group = 2
    num_rounds = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    pre_global_1 = models.FloatField()
    pre_global_2 = models.FloatField()
    pre_global_3 = models.FloatField()
