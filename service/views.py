from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Service, SubCategory
from django.core.paginator import Paginator
from .forms import ServiceForm
from .filters import ServiceFilter


# Create your views here.

def service_list(request):
    myfilter = ServiceFilter(request.GET, queryset=Service.objects.all())
    services_list = myfilter.qs
    service_count = services_list.count()
    elements = 6  # services per page
    paginator = Paginator(services_list.order_by('-id'), elements)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    elements = str(":-" + str(elements))
    context = {'services': page_obj, 'service_count': service_count, 'myfilter': myfilter,
               'elements': elements}  # template name
    return render(request, 'service/service_list.html', context)


def service_detail(request, slug):
    service_details = Service.objects.get(slug=slug)
    context = {'service': service_details}
    return render(request, 'service/service_detail.html', context)


def load_sub_category(request):
    main_category_id = request.GET.get('main_category_id')
    sub_categories = SubCategory.objects.filter(main_category_id=main_category_id).all()
    return render(request, 'service/sub_category_list_options.html', {'sub_categories': sub_categories})


@login_required
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect('services:service_list')

        else:
            pass

    else:
        form = ServiceForm()

    return render(request, 'service/add_service.html', {'form': form})
