from django.shortcuts import render
from .models import Device

# Create your views here.
def ind(request):
    devLists = Device.objects.all()
    return render(request, 'map/index.html', {'devices':devLists})
