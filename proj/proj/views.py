from django.shortcuts import render
from . import models
def homefunction(request):
    print(models.Farmer.objects())
    return render(request,"index.html")