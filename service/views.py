from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Service
from django.core.paginator import Paginator
from .forms import ServiceForm
from .filters import ServiceFilter


# Create your views here.

def service_list(request):
    service_list = Service.objects.all()
    #filters
    myfilter = ServiceFilter(request.GET, queryset=service_list)
    service_list = myfilter.qs
    service_count = Service.objects.count()
    paginator = Paginator(service_list.order_by('-id'), 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'services': page_obj, 'service_count': service_count, 'myfilter': myfilter}  # template name
    return render(request, 'service/service_list.html', context)


def service_detail(request, slug):
    service_detail = Service.objects.get(slug=slug)
    context = {'service': service_detail}
    return render(request, 'service/service_detail.html', context)


@login_required
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            form = ServiceForm()

        else:
            pass

    else:
        form = ServiceForm()

    return render(request, 'service/add_service.html', {'form': form})
