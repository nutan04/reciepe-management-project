from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def reciepe(request):
    
    if request.method == "POST":
        data = request.POST
        reciepe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get('receipe_image')
        # print(reciepe_name)
        # print(receipe_description)
        # print(receipe_image)

        Receipe.objects.create( 
            
            receipe_name = reciepe_name,
            receipe_description = receipe_description,
            receipe_image =  receipe_image
        )

        return redirect('/reciepe/')
    
    

    queryset = Receipe.objects.all()
    

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))

    context = {'reciepes' : queryset}
    return render(request, "reciepe.html", context)

def update_receipe(request,id):
    queryset = Receipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get('receipe_image')

        queryset.receipe_name = receipe_name 
        queryset.receipe_description = receipe_description

        if receipe_image :
            queryset.receipe_image = receipe_image
        
        queryset.save()
        return redirect('/reciepe/')
    
    context = {'reciepe' : queryset}
    return render(request, "update_reciepe.html", context)

def delete_receipe(request,id):
    # print(id)
    # return HttpResponse("a")
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/reciepe/')

