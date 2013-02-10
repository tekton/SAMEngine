from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def RegistrationPage(request):
    form = UserCreationForm
    return render_to_response("auth/login.html", {'form': form}, context_instance=RequestContext(request))
