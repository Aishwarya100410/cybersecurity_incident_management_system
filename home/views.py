from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from datetime import datetime
from .models import Report
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from .models import Report
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request,'main.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Custom login logic
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if (username == 'Harini' and password == 'Harini18') or (username == 'Aishwarya' and password == 'Aishwarya10'):
            request.session['admin_authenticated'] = True
            return redirect('admindashboard')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'adminlogin.html')

# Custom decorator for authentication
def admin_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.session.get('admin_authenticated'):
            return redirect('adminlogin')
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func

@admin_required
def admindashboard(request):
    return render(request, 'admindashboard.html')

def logout(request):
    request.session.flush()
    return redirect('main')

def admindashboard(request):
    return render(request,'admindashboard.html')
def tips(request):
    return render(request,'tips.html')
def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'userlogin.html')
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered Successfully. You can now log in.')
            return redirect('userlogin')
    else:
        form = CreateUserForm()
    context = {'form': form}
    return render(request, 'register.html', context)
def home(request):
    return render(request,'home.html')
# Create your views here.
def about(request):
      return render(request,'about.html')
from django.contrib.auth import logout as auth_logout

def logout(request):
    return render(request,'logout.html')
def  incidentmanagement(request):
      return render(request,'incidentmanagement.html')
def settings(request):
      return render(request,'settings.html')
from django.shortcuts import render
from .models import Report

def track(request):
    incidents = Report.objects.all()  # You can filter based on the logged-in user if needed
    return render(request, 'track.html', {'incidents': incidents})
def track(request):
      return render(request,'track.html')
def analysis(request):
      return render(request,'analysis.html')
def severityl(request):
    return render(request,'severityl.html')
def report(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        location = request.POST.get('location')
        description = request.POST.get('description')
        severity = request.POST.get('severity')

        if name and date and location and description and severity:
            incident = Report(
                name=name,
                date=date,
                location=location,
                description=description,
                severity=severity
            )
            incident.save()
            messages.success(request, 'Incident reported successfully!')
            return redirect('report')
        else:
            messages.error(request, 'All fields are required.')

    return render(request, 'report.html')

from django.shortcuts import render, redirect
from .models import Incident
from .forms import IncidentReportForm

'''def report(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('track')  # Redirect to the track incidents page after saving
    else:
        form = IncidentReportForm()
    return render(request, 'report.html', {'form': form})

def track(request):
    incidents = Incident.objects.all()
    return render(request, 'track.html', {'incidents': incidents})
'''
