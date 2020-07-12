from otree.api import Currency as c
from . import pages
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):
    def play_round(self):
        yield pages.Survey, dict(Name="xyz", Age=0)
        yield pages.Welcome
        yield pages.Zoom_Link
        yield pages.Stimuli, dict()
        yield pages.Judgement1_question, dict(judgement1=0.0)
        yield pages.Certainty1_Question, dict(certainty1=0.0)
        yield pages.Discussion1, dict(discussion1=0.0)
        yield pages.Wavelength, dict(PartnerAgreement="Strongly disagree")
        yield pages.Judgement_Question2, dict(judgement2=0.0)
        yield pages.Certainty_Question2, dict(certainty2=0.0)
        yield pages.Stimuli_Rewatch
        yield pages.Judgement_Question3, dict(judgement3=0.0)
        yield pages.Certainty_Question3, dict(certainty3=0.0)