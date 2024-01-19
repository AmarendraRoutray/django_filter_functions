from django.shortcuts import render

# Create your views here.
import datetime

def filters(request):
    
    dt = datetime.datetime.now()
    data = {'data':'heLLO I aM LuFfY', 'dt':dt, 'c':1, 'd':10 }
    
    return render(request,'filters.html',data)