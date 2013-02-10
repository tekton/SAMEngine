from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from forms import CharacterForm
from models import BaseCharacter


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
    return render_to_response("characters/list.html", context_instance=RequestContext(request))
