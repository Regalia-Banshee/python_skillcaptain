from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "registration/home.html",{})

def AuthView(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST or none)
        if form.is_valid():
            form.save()
    else:
        form=UserCreationForm
    return render(request, "registration/signup.html",{"form": form})
