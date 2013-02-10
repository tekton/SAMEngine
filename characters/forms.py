from django.forms import ModelForm
from models import *


class CharacterForm(ModelForm):
    class Meta:
        model = BaseCharacter
