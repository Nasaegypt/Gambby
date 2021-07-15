from django.shortcuts import render
from .models import Service
from django.core.paginator import Paginator
from .forms import ServiceForm


# Create your views here.

def service_list(request):
    service_list = Service.objects.all()
    paginator = Paginator(service_list, 2)  # show 5 services per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'services': page_obj}  # template name
    return render(request, 'service/service_list.html', context)


def service_detail(request, slug):
    service_detail = Service.objects.get(slug=slug)
    context = {'service': service_detail}
    return render(request, 'service/service_detail.html', context)


def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            myform.save()  # repeated to enter the id with slug
        else:
            pass

    else:
        form = ServiceForm()

    return render(request, 'service/add_service.html', {'form': form})
