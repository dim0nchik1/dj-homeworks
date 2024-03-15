from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open('data-398-2018-08-30.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        list_reader = []
        for line in reader:
            dict_reader = {'Name': line['Name'],
                         'Street': line['Street'],
                         'District': line['District']

                             }
            list_reader.append(dict_reader)
        page_number = int(request.GET.get('page', 1))
        paginator = Paginator(list_reader, 10)
        page = paginator.get_page(page_number)


    context = {
        'bus_stations': page,

         'page': page,
    }

    return render(request, 'stations/index.html', context)
