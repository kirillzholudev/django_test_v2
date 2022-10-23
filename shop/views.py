from django.shortcuts import render


def fill_database(request):
    return render(request, 'fill-products.html')
