from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from forms import CharacterForm, AbilityForm
from models import BaseCharacter, Ability


def BasicInfo(request, char_id):
    # check redis for the character...
    # if it's not there, ask postgres
    # then put it in redis...
    # ...and return the character info as a json object!
    try:
        character = BaseCharacter.objects.get(pk=char_id)
    except BaseCharacter.DoesNotExist:
        return render_to_response("characters/list.html", context_instance=RequestContext(request))
    return render_to_response("characters/show.html", {"character": character}, context_instance=RequestContext(request))


def CheckXPCost():
    return


def SpendXPOnStat(request, char_id, stat):
    return


def SpendXPOnAbility(request, char_id, ability_id, column, increase):
    return


@login_required
def NewCharacter(request):
    print "new character"
    form = CharacterForm()
    if request.POST:
        character = BaseCharacter()
        form = CharacterForm(request.POST, instance=character)
        new_character = form.save()
        print "now redirect to " + str(new_character)
        return redirect('characters.views.BasicInfo', new_character.id)
    return render_to_response("characters/new.html", {"form": form}, context_instance=RequestContext(request))


@login_required
def CharacterList(request):
    print "character list"
    characters = BaseCharacter.objects.filter(user=request.user.id)
    print characters
    return render_to_response("characters/list.html", {"characters": characters}, context_instance=RequestContext(request))


@login_required
def AbilityNew(request):
    print "new ability"
    form = AbilityForm()
    ability = Ability()
    if request.POST:
        form = AbilityForm(request.POST, instance=ability)
        new_ability = form.save()
        print "now redirect to " + str(new_ability)
        return redirect('characters.views.AbilityShow', new_ability.id)
    else:
        character = request.GET.get("character", 0)
        if character != 0:
            try:
                print character
                c = BaseCharacter.objects.get(pk=character)
                ability.character = c
                form = AbilityForm(instance=ability)
            except:
                pass
        else:
            pass
    return render_to_response("ability/new.html", {"form": form}, context_instance=RequestContext(request))


@login_required
def AbilityShow(request, ability_id):
    try:
        character = Ability.objects.get(pk=ability_id)
    except Ability.DoesNotExist:
        return render_to_response("characters/list.html", context_instance=RequestContext(request))
    return render_to_response("characters/show.html", {"character": character}, context_instance=RequestContext(request))
