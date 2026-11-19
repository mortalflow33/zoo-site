from django.shortcuts import render

def index(request):
    return render(request, 'zoo_app/index.html')
