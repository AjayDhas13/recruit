# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from controlpanel.models import Applications
from .forms import Application
from django.conf import settings
import os
from django.contrib import messages

def handle_uploaded_file(f, file_name, source_dir):
    with open(source_dir + file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def home(request):
	if request.method == "POST":
		form = Application(data=request.POST, files=request.FILES)
		if form.is_valid():
			profile = ""
			objModel = Applications()
			file = request.FILES.get("profile", "")
			objModel.name = form.cleaned_data["name"]
			objModel.email = form.cleaned_data["email"]
			objModel.mobile = form.cleaned_data["mobile"]
			objModel.date_of_birth = form.cleaned_data["date_of_birth"]
			objModel.gender = form.cleaned_data["gender"]
			objModel.education = form.cleaned_data["education"]
			if file:
				fname = str(file)
				filesize = len(file.read())
				root, ext = os.path.splitext(fname)
				objModel.profile = fname
				if ext[1:] in ['pdf']:
					sourceDir = settings.PROFILE_PATH
					if not os.path.exists(sourceDir):
						os.makedirs(sourceDir)

					handle_uploaded_file(file, fname, sourceDir)
				else:
					messages.add_message(request, messages.WARNING, u"Only PDF Files are supported!..")
					return render(request, "applicants/home.html", {"form": form})
			try:
				objModel.save()
				form = Application()
				messages.add_message(request, messages.SUCCESS, u"Thanks!.Your Application Reference No ["+objModel.ref_id+"] submitted successfully..")
			except Exception:
				pass
				messages.add_message(request, messages.WARNING, u"Sorry try again after sometimes!..")
		else:
			print "Form Error"
	else:
		form = Application()

	return render(request, "applicants/home.html", {"form": form})

def track(request):
	data = None
	if request.method == "POST":
		ref_id = request.POST.get("ref_id", "")
		applicationObj = get_object_or_404(Applications, ref_id=ref_id)
		status = None
		if applicationObj.status == 0:
			status = "Submitted"
		elif applicationObj.status == 1:
			status = "Viewed"
		elif applicationObj.status == 2:
			status = "Accepted"
		else:
			status = "Rejected"
		messages.add_message(request, messages.SUCCESS, u"Your Application request is "+ status)
	return render(request, "applicants/track.html")