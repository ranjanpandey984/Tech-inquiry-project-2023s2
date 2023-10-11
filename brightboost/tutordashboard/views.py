from django.shortcuts import render

# Create your views here.


def tutordashboard(request):
    return render(request, 'tutordashboard/index.html')
