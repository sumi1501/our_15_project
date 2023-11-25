from django.shortcuts import render

# Create your views here.
def bom(request):
    return render(request,'bom.html')