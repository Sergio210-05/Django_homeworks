from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_type = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort_type == "name":
        phones = phones.order_by("name")
    elif sort_type == "min_price":
        phones = phones.order_by("price")
    elif sort_type == "max_price":
        phones = phones.order_by("price").reverse()
    # item = phones[0].slug
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone,
    }
    return render(request, template, context)
