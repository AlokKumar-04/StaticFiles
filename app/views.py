from django.shortcuts import render

# Create your views here.
def staticfiles(request):
    return render(request, 'index.html')
