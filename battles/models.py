from django.db import models
from django.contrib.auth.models import User

from characters.models import BaseCharacter  # , Ability, Item, Skill


class BattleBase(models.Model):
    '''
        ID's are created automagically; so what do we actually need in here?
    '''
    name = models.CharField(max_length=255)
    user_one = models.ForeignKey(User, related_name='Player_One')
    user_two = models.ForeignKey(User, related_name='Player_Two')
    battle_active = models.NullBooleanField()  # null = hasn't started yet, true = go through turns, false = complete
    current_player_turn = models.NullBooleanField()  # true = character 1, false = character 2, null = not started/complete
    winner = models.NullBooleanField()  # null = undecided, true = player 1, false = player 2
    user_winner = models.ForeignKey(User, blank=True, null=True, related_name='Winner')

    def __unicode__(self):
        return self.name


class ArmyComposition(models.Model):
    '''
        This is really more like a "tag" list of characters for each side

        Additionally, after this is thrown in to redis this acts as a sanity check that things are correct;
        it also allows for a fall back position should the game get interupted
    '''
    battle = models.ForeignKey(BattleBase)
    user = models.ForeignKey(User)
    character_base = models.ForeignKey(BaseCharacter)
    # need a character_copy class that combines everything; though really that should just be a redis thing, so...
    redis_character_id = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.character_base.name + " (#" + str(self.redis_character_id) + ")"
