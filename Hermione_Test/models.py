from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv, os, random

doc = ''


class Constants(BaseConstants):
    name_in_url = 'Hermione_Test'
    players_per_group = 2
    num_rounds = 1




class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    discussion1 = models.FloatField()

    def live_slider(self, id_in_group, package):
        broadcast = {"slider_value": package["slider_value"], "disable": package["disable"]}
        return {0: broadcast}


class Player(BasePlayer):
    Name = models.StringField(label='What is your name?')
    Age = models.IntegerField(label='What is your age?')
    PartnerAgreement = models.StringField(choices=[['Strongly disagree', 'Strongly disagree'], ['Disagree', 'Disagree'],
                                                   ['Somewhat disagree', 'Somewhat disagree'],
                                                   ['Neither agree nor disagree', 'Neither agree nor disagree'],
                                                   ['Somewhat agree', 'Somewhat agree'], ['Agree', 'Agree'], ['Strongly agree', 'Strongly agree']],
                                          label=' ',
                                          widget=widgets.RadioSelect)
    judgement1 = models.FloatField()
    certainty1 = models.FloatField()
    judgement2 = models.FloatField()
    certainty2 = models.FloatField()
    judgement3 = models.FloatField()
    certainty3 = models.FloatField()
    mutual_judgment = models.IntegerField()
    my_field = models.StringField()

    def my_method(self):
        "live_slider"
