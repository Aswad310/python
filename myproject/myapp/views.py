from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Employe
# Create your views here.

def home(request):
    text = """<h1>Home Page</h1>"""
    return HttpResponse(text)

def contact(request):
    text = """<h1>Contact Page</h1>"""
    return HttpResponse(text)

def product(request, number):
    text = """<h1>Product Page %s</h1>"""%number
    return HttpResponse(text)

def productday(request, month, year):
    text = """<h1>Product Page %s %s</h1>"""%(month, year)
    return HttpResponse(text)

def hello(request):
    today = datetime.now()
    
    dayofweek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    return render(request, 'main/hello.html', {"today" : today, "day_of_week" : dayofweek})

# database CRUD
def crudops(request):
   
   #Creating an entry
   employe = Employe(
       website = 'www.google.com',
       mail  = 'abad@gmail.com',
       name = 'Aswad',
       phonenuber = '002376970'
   )
   employe.save()
   
   #Read all entries
   objects = Employe.objects.all()
   res = 'Printing all Employe entries in DB : <br>'
   for obj in objects:
       res += obj.name+"<br>"
   
   # Read Specific Entry
   obj = Employe.objects.get(name = "Aswad Ali")
   res += 'Printing one Entry <br>'
   res += obj.name
   
   # Delete an Entry
   obj = Employe.objects.get(name = "Aswad Ali")
   res += '<br> Delete an Entry <br>'
   obj.delete()
   
   # Update an Entry
   employe = Employe.objects.get(name = "Aswad Ali")
   employe.name = "Abad Ali"
   employe.save()
   
   return HttpResponse(res)

# data mainpulation
def datamanipulation(request):
    res = ''
    
    # Filtering Data
    emp = Employe.objects.filter(name = 'Aswad Ali')
    res += "Found : %s results<br>"%len(emp)
    
    # Ordering Results
    emp = Employe.objects.order_by("name")
    
    for obj in emp:
        res += obj.name + '<br>'
        
    return HttpResponse(res)