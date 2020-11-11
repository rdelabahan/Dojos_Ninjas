from django.shortcuts import render, redirect
from dojo_ninjas_app.models import Dojo, Ninja

def index(request):
    context = {
        "dojos": Dojo.objects.all()
    }
    return render(request,'index.html',context)

def create_dojo(request):
    if request.method == "POST":
        Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state'],
    )
    return redirect('/')

def create_ninja(request):
    if request.method == "POST":
        Ninja.objects.create(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        dojo_id=request.POST['dojoname'],
    )
    return redirect('/')

def delete_dojo(request):
    if request.method == "POST":
        dojo = Dojo.objects.get(id=request.POST['del'])
        dojo.delete()
    return redirect('/')



