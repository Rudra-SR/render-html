from django.shortcuts import render

# Create your views here.
def money(request):
    return render(request, 'money.html')