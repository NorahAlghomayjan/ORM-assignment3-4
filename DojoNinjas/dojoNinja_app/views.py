from django.shortcuts import render , redirect
from .models import Dojos , Ninjas



#main page 
def index(request):
    context = {
        "dojos" : Dojos.objects.all(),
        "ninjas": Ninjas.objects.all(),
    } 
    return render(request,'forms.html',context)


#clicking add dojo button will invoke this method 
def addDojo (request):
    if not(request.method == 'POST'):
        return redirect('/')
    
    name = request.POST.get('name')
    city = request.POST.get('city')
    state = request.POST.get('state')
    count = 0 #cause there is no ninja assigned to this just created dojo.

    Dojos.objects.create(name=name,city=city,state=state,count=count)

    return redirect('/')


def addNinja (request):
    if not(request.method == 'POST'):
        return redirect('/')
    
    first = request.POST.get('first')
    last = request.POST.get('last')
    dojoID = request.POST.get('dojo')
    dojo = Dojos.objects.get(id=dojoID)
    dojo.count +=1 #add count by 1 every time a new ninja assigned to dojo
    dojo.save()

    Ninjas.objects.create(first_name=first,last_name=last,dojo=dojo)

    return redirect('/')
    
def deleteDojo (request,id):
    dojo = Dojos.objects.get(id=id)
    dojo.delete()

    return redirect('/')


