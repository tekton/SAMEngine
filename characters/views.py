from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext


def BasicInfo(request, char_id):
    # check redis for the character...
    # if it's not there, ask postgres
    # then put it in redis...
    # ...and return the character info as a json object!
    return


def CheckXPCost():
    return


def SpendXPOnStat(request, char_id, stat):
    return


def SpendXPOnAbility(request, char_id, ability_id, column, increase):
    return


@login_required
def CharacterList(request):
    return render_to_response("characters/list.html", context_instance=RequestContext(request))
