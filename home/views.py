from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    peoples = [
        {"name":"Nutan","age":17},
        {"name":"Nitya","age":26},
        {"name":"Naksha","age":27},
        {"name":"Naina","age":28},
        {"name":"Naksh","age":29}

    ]

    return render(request, "home/index.html", context = {'peoples':peoples})

def about(request):
      return render(request, "home/about.html")

def contact(request):
      return render(request, "home/contact.html")

def sucess_page(request):
     return HttpResponse("""<h1>Hey I am Django first home page<h1>
    <p>This is the django app</p>
    <hr>
    <h1>This is home page<h1>
    
    """)

