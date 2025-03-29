from django.shortcuts import render


def filter(request):
    return render(request,"filter/filter.html",{})