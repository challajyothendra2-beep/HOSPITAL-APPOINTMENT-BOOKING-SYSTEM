from django.shortcuts import render

# Create your views here.
def push(request):
    return render(request,"text.html")