from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    # return HttpResponse("hello world")
    return render(request,'home.html')

def result(request):
    # return HttpResponse("hello world")
    cls = joblib.load('data.csv')
    lis = []
    lis.append(request.GET['RI'])
    lis.append(request.GET['RI'])
    lis.append(request.GET['RI'])
    lis.append(request.GET['RI'])
    lis.append(request.GET['RI'])
    lis.append(request.GET['RI'])
    lis.append(request.GET['RI'])
    lis.append(request.GET['RI'])
    lis.append(request.GET['RI'])
    print(lis)


    return render(request,'result.html')
