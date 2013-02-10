from django.forms import ModelForm
from models import *


class CharacterForm(ModelForm):
    class Meta:
        model = BaseCharacter


class AbilityForm(ModelForm):
    class Meta:
        model = Ability
