from django.shortcuts import render
from Sicop.settings import DATABASE_NOT_LITE

def filter(request):
    DATABASE_NOT_LITE.set_table("filtros")
    data = DATABASE_NOT_LITE.find({})
    return render(request,"filter/filter.html",{"data":data})