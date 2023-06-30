from django.shortcuts import render



def home(request):
    return render(request, 'dk_website.html')

    