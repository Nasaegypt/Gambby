from django.shortcuts import render
from .models import Service


# Create your views here.

def service_list(request):
    service_list = Service.objects.all()
    context = {'services': service_list}  # template name
    return render(request, 'service/service_list.html', context)


def service_detail(request, id):
    service_detail = Service.objects.get(id=id)
    context = {'service': service_detail}
    return render(request, 'service/service_detail.html', context)
