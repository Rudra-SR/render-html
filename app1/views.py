from django.shortcuts import render

# Create your views here.
def money(request):
    return render(request, 'money.html')

def f1(request):
    return render(request, 'f1.html')
def f2(request):
    return render(request, 'f2.html')
def f3(request):
    return render(request, 'f3.html')