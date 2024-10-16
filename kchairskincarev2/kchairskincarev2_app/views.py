from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import AppointmentRequest, MessageRequest
from kchairskincarev2_app.forms import AppointmentForm, ContactForm, CustomAuthenticationForm, CreateUserForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context = {}

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        # Render the form for GET requests
        form = AppointmentForm()

    context['form'] = form
    
    return render(request, "index.html", context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def services(request):
    context = {}

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        # Render the form for GET requests
        form = AppointmentForm()

    context['form'] = form

    return render(request, 'services.html', context)

def pricing(request):
    context = {}

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        # Render the form for GET requests
        form = AppointmentForm()

    context['form'] = form

    return render(request, 'pricing.html', context)

def portfolio(request):
    context = {}
    return render(request, 'portfolio.html', context)

def team(request):
    context = {}
    return render(request, 'team.html', context)

def faq(request):
    context = {}
    return render(request, 'faq.html', context)

def services_page(request):
    context = {}
    return render(request, 'services-page.html', context)

def team_details(request):
    context = {}
    return render(request, 'team-details.html', context)

def post(request):
    context = {}
    return render(request, 'post.html', context)

def error_404(request):
    context = {}
    return render(request, '404.html', context)

def coming_soon(request):
    context = {}
    return render(request, 'coming-soon.html', context)

def blog(request):
    context = {}
    return render(request, 'blog.html', context)

def blog2(request):
    context = {}
    return render(request, 'blog2.html', context)

def blog3(request):
    context = {}
    return render(request, 'blog3.html', context)

def contact(request):
    context = {}

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        # Render the form for GET requests
        form = ContactForm()

    context['form'] = form

    return render(request, 'contact.html', context)

def logout(request):
    return redirect('login')

class CustomLoginView(auth_views.LoginView):
    template_name = 'login.html'
    authentication_form = CustomAuthenticationForm

@login_required
def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)

@login_required
def requested_appointments(request):
    context = {}
    return render(request, 'requested-appointments.html', context)

@login_required
def approved_appointments(request):
    context = {}
    return render(request, 'approved-appointments.html', context)

@login_required
def message_requests(request):
    context = {}
    return render(request, 'message-requests.html', context)

@login_required
def register_user(request):
    context = {}
    return render(request, 'register-user.html', context)

@login_required
def email_subscribers(request):
    context = {}
    return render(request, 'email-subscribers.html', context)

@login_required
def contact_info(request):
    context = {}
    return render(request, 'contact-info.html', context)