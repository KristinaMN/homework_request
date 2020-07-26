from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv


path_file = settings.BUS_STATION_CSV


def read_file(path):
    result = []
    with open(path, 'r') as file:
        read = csv.DictReader(file)
        for i in read:
            result.append(i)
    return result

def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    current_page = int(request.GET.get('page', 1))
    elemets_show = 15
    next_page_url = ''
    prev_page_url = ''

    paginator = Paginator(read_file(path_file), elemets_show)
    page_obj = paginator.get_page(current_page)
    content = page_obj.object_list
    if page_obj.has_next():
        next_page_url = f'?page={page_obj.next_page_number()}'
    if page_obj.has_previous():
        prev_page_url = f'?page={page_obj.previous_page_number()}'


    return render(request, 'index.html', context={
        'bus_stations': content,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

