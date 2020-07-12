
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'Demographic'
    players_per_group = 2
    num_rounds = 1
    instructions_template = 'Demographic/instructions.html'
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    Gender = models.StringField(choices=[['Male', 'Male'], ['Female', 'Female'], ['Other ', 'Other ']], label='What is your gender?')
    Race = models.LongStringField(choices=[['American Indian/Alaska Native', 'American Indian/Alaska Native'], ['Asian, Native Hawaiian or other Pacific Islander', 'Asian, Native Hawaiian or other Pacific Islander'], ['Black of African American', 'Black of African American'], ['White, non-hispanic origin ', 'White, non-hispanic origin '], ['Hispanic ', 'Hispanic '], ['Multiple ', 'Multiple '], ['Other', 'Other']], label='With which group do you most identify?')
    Relationship = models.StringField(choices=[['Single', 'Single'], ['Dating, not living together', 'Dating, not living together'], ['Dating, living together ', 'Dating, living together '], ['Engaged, not living together ', 'Engaged, not living together '], ['Engaged, living together', 'Engaged, living together'], ['Married', 'Married'], ['Domestic Partnership', 'Domestic Partnership'], ['Other', 'Other']], label='What is your current relationship status?')
    SexualOrientation = models.StringField(blank=True, choices=[['Straight', 'Straight'], ['Gay/Lesbian', 'Gay/Lesbian'], ['Bisexual', 'Bisexual'], ['Other', 'Other']], label='Which best describes your sexual orientation?')
    Job = models.StringField(blank=True, label='What is your current job?')
    Education = models.StringField(choices=[['None', 'None'], ['Elementary School', 'Elementary School'], ['Middle School', 'Middle School'], ['Some High School', 'Some High School'], ['High School', 'High School'], ['Some College', 'Some College'], ['Associates', 'Associates'], ["Bachelor's", "Bachelor's"], ['Graduate Degree', 'Graduate Degree'], ['Doctorate ', 'Doctorate ']], label='How many years of formal education have you completed?')
    Ladder = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10']], label='   ')
    PoliticalParty = models.FloatField()
    PoliticalOrientation = models.FloatField()
    Age = models.IntegerField(label='Please enter your age')
    Compromise = models.StringField(blank=True, label='What do you consider a compromise?')
    Describe = models.StringField(blank=True, label='As briefly as possible, please describe what you think this study was about:')
    Comments = models.StringField(blank=True, label='Please feel free to make any additional comments about the study: ')
    Issues = models.StringField(blank=True, label='Did you experience any technical issues during the experiment? If so, please explain what these issues were')