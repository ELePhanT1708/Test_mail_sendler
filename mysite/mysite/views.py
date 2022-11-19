from django.shortcuts import render


def home_page(request):
    return render(request, 'home_page.html')


def user_data(request):

    return