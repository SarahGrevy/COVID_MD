
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Survey(Page):
    form_model = 'player'
    form_fields = ['Age', 'Gender', 'Race', 'Relationship', 'SexualOrientation', 'Education', 'Job']
class Household_Income(Page):
    form_model = 'player'
    form_fields = ['Ladder']
class Political_Orientation(Page):
    form_model = 'player'
    form_fields = ['PoliticalOrientation']
class Political_Party(Page):
    form_model = 'player'
    form_fields = ['PoliticalParty']
class Blank_Questions(Page):
    form_model = 'player'
    form_fields = ['Compromise', 'Describe', 'Comments', 'Issues']
page_sequence = [Survey, Household_Income, Political_Orientation, Political_Party, Blank_Questions]