import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request, path_to_file=settings.BUS_STATION_CSV):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(path_to_file, encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        reader_list = list(reader)
    paginator = Paginator(reader_list, 10)
    page_number = int(request.GET.get("page", 1))
    stations_in_page = paginator.get_page(page_number)

    context = {
        'bus_stations': stations_in_page,
        'page': stations_in_page,
    }
    return render(request, 'stations/index.html', context)
