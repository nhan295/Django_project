from django.shortcuts import render
from django.http import HttpResponse

def caculate():
   x = 1
   y = 2
   return x+y

def say_hello(request):
    x = caculate()
    
    return render(request, 'hello.html',{'name':'nhan'})
   # return HttpResponse('hello iamnhan')


