from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BaseCharacter(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    # Stats
    strength = models.IntegerField(default=1)
    agility = models.IntegerField(default=1)
    mind = models.IntegerField(default=1)
    essence = models.IntegerField(default=1)
    # other important things
    total_experience = models.IntegerField(default=1)
    spent_experience = models.IntegerField(default=0)
    free_experience = models.IntegerField(default=1)  # db space is cheap in this case, proc cycles are expensive
    # backend implementation stuff
    visibility = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Skill(models.Model):
    # TODO: add archetype
    character = models.ForeignKey(BaseCharacter)
    name = models.CharField(max_length=255)
    stat = models.CharField(max_length=255)
    weapon = models.CharField(max_length=255, blank=True, null=True)
    ability = models.CharField(max_length=255, blank=True, null=True)


class Item(models.Model):
    # TODO: add archetype
    character = models.ForeignKey(BaseCharacter)
    name = models.CharField(max_length=255)
    stat = models.CharField(max_length=255)
    offensive = models.NullBooleanField()
    armor = models.IntegerField(default=0)
    price = models.FloatField(default=0)


class Ability(models.Model):
    # TODO: add archetype
    character = models.ForeignKey(BaseCharacter)
    name = models.CharField(max_length=255)
    dice = models.IntegerField(default=1)
    abilityRange = models.IntegerField(default=1)  # in squares
    statusEffect = models.CharField(null=True, blank=True, max_length=255)
    requiredItem = models.CharField(max_length=255)
    actionsPoints = models.IntegerField(default=1)
    extraScript = models.TextField(blank=True, null=True)
