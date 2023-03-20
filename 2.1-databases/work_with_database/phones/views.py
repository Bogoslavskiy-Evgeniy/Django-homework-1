from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_objects = Phone.objects.all()
    page_sort = request.GET.get('sort', '')

    if page_sort == 'max_price':
        phones = phone_objects.order_by('-price')
        context = {'phones': phones}
        return render(request, template, context)

    elif page_sort == 'min_price':
        phones = phone_objects.order_by('price')
        context = {'phones': phones}
        return render(request, template, context)

    elif page_sort == 'name':
        phones = phone_objects.order_by('name')
        context = {'phones': phones}
        return render(request, template, context)

    context = {'phones': phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.get(slug=slug)
    context = {'phone': phone_object}
    return render(request, template, context)
