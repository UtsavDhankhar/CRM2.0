from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Lead , Agent
from .forms import LeadForm , LeadModelForm , NewUserCreationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



def landing_page(request):
    return render(request,  "landing.html")

def login_page(request):

    page = "login"

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request , username=username , password = password)
    
        if(user):

            login(request , user)
            return redirect("/leads")
        
        else:

            return render(request, 'Lead/login_register.html' , {'error':"Invalid input" , 'context': page})

    else:

        return render(request , 'Lead/login_register.html' , {'context' : page})


def register_page(request):

    page = 'register'
    form = NewUserCreationForm()

    if request.method == "POST":
        form = NewUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request , "account has been successfully created")
            login(request , user)
            return redirect("/leads")
        
        else:
            messages.error(request, "form was invalid ")
            

    
    return render(request, 'Lead/login_register.html' , {'form': form,'context':page})

def logout_page(request):
    logout(request)
    return redirect("landing_page")




@login_required(login_url='login')
def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads" : leads
    }
    return render(request,"Lead/lead_list.html" , context)

@login_required(login_url='login')
def lead_detail(request , pk):
    lead = Lead.objects.get(id = pk)
    context = {
        "lead" : lead
    }
    return render(request, "Lead/lead_detail.html" , context)
    
@login_required(login_url='login')
def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/leads")
    
    context = {
        "form" : form
    }

    return render(request,"Lead/lead_create.html" , context)

@login_required(login_url='login')
def lead_update(request, pk):
    lead = Lead.objects.get(id = pk)
    form = LeadModelForm(instance=lead)

    if request.method == "POST":
        form = LeadModelForm(request.POST , instance=lead)

        if form.is_valid():
            form.save()
            return redirect("/leads")

    context = {
        "form" : form,
        "lead" : lead,
    }

    return render(request , "Lead/lead_update.html" , context)

@login_required(login_url='login')
def lead_delete(request, pk):
    lead = Lead.objects.get(id = pk)
    lead.delete()
    return redirect("/leads") 





