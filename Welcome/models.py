
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
    Name = models.StringField(label='What is your name?')
    Age = models.IntegerField(label='How old are you? ')