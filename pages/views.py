from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def pages(request):
    return render(request, 'pages.html')