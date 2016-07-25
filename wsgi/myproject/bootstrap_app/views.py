from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'bootstrap_app/index.html', {"items":["primeira", "segunda", "terceira"]})
