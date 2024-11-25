from django.http import HttpResponse

def homepage(request):#
  return HttpResponse("Hello world! I'm Home")

def about(request):#
  return HttpResponse("My About Page")

