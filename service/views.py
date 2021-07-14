from django.shortcuts import render
from .models import Service
from django.core.paginator import Paginator


# Create your views here.

def service_list(request):
    service_list = Service.objects.all()
    paginator = Paginator(service_list, 5)  # show 5 services per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'services': page_obj}  # template name
    return render(request, 'service/service_list.html', context)


def service_detail(request, slug):
    service_detail = Service.objects.get(slug=slug)
    context = {'service': service_detail}
    return render(request, 'service/service_detail.html', context)
