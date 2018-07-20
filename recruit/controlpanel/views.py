# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_list_or_404, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Applications
from applicants.forms import Application
from .forms import ApplicationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
import os
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
def login(request):
	if request.method == "POST":
		username = request.POST['UserName']
		password = request.POST['Password']
		user = authenticate(username=username, password=password)
		if user is not None:
			auth_login(request, user)
			return HttpResponseRedirect("/controlpanel")
		else:
			messages.add_message(request, messages.WARNING, u"Invalid Username or Password.")
	else:
		pass
	return render(request, "login.html")

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/controlpanel")

@login_required(login_url='/controlpanel/login/')
def home(request):
	applicationList = get_list_or_404(Applications)
	return render(request, "controlpanel/list.html", {"applicationList": applicationList})

@login_required(login_url='/controlpanel/login/')
def view(request, ref_id):
	applicationObj = get_object_or_404(Applications, ref_id=ref_id)
	form = ApplicationForm(instance=applicationObj)
	try:
		applicationObj.status = 1
		applicationObj.save()
	except Exception:
		messages.add_message(request, messages.WARNING, u"There was some error while updating!...")

	return render(request, "controlpanel/view.html", {"form": form})

@login_required(login_url='/controlpanel/login/')
def accept(request, ref_id):
	applicationObj = get_object_or_404(Applications, ref_id=ref_id)
	try:
		applicationObj.status = 2
		applicationObj.save()
		messages.add_message(request, messages.SUCCESS, u"Application has been accepted Successfully!..")
	except Exception:
		messages.add_message(request, messages.WARNING, u"Please try again after sometimes!..")
	
	return HttpResponseRedirect("/controlpanel")

@login_required(login_url='/controlpanel/login/')
def reject(request, ref_id):
	applicationObj = get_object_or_404(Applications, ref_id=ref_id)
	try:
		applicationObj.status = 3
		applicationObj.save()
		messages.add_message(request, messages.SUCCESS, u"Application has been rejected Successfully!..")
	except Exception:
		messages.add_message(request, messages.WARNING, u"Please try again after sometimes!..")
	
	return HttpResponseRedirect("/controlpanel")

@login_required(login_url='/controlpanel/login/')
def download(request, ref_id):
	applicationObj = get_object_or_404(Applications, ref_id=ref_id)
	file_path = os.path.join(settings.PROFILE_PATH, applicationObj.profile)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/pdf")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404
