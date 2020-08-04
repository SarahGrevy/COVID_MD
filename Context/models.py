
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'Context'
    players_per_group = 2
    num_rounds = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    state = models.StringField(blank=True, label='In what state have you primarily lived during the coronavirus outbreak? If you have primarily lived outside the U.S, please specify which country.')
    covid = models.LongStringField(choices=[['Yes', 'Yes'], ['No', 'No'],
                                                   ['Prefer not to answer', 'Prefer not to answer']],
                                          label='Have you or someone close to you contracted COVID-19?')
    pay_cut = models.LongStringField(choices=[['Yes', 'Yes'], ['No', 'No'],
                                                   ['Prefer not to answer', 'Prefer not to answer']],
                                     label='Have you or someone in your housefold either lost a job or taken a paycut because of the coronavirus outbreak?')
    news_source = models.StringField(blank=True, label='What is your most trusted news source?')
    post_goverment = models.FloatField()
    post_global_1 = models.FloatField()
    post_global_2 = models.FloatField()
    post_global_3 = models.FloatField()

