from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required 

@login_required
def logout_page(request):
	logout(request)
	return render_to_response('registration/logout.html')	

@login_required
def page(request):
	user = request.user
	return render_to_response('page.html', {'user': user})
