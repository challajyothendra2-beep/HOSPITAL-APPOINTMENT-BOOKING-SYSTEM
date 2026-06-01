from django.shortcuts import render

# Create your views here.
def historys(request):
    return render(request,"history.html")