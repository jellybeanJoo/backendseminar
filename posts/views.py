from django.shortcuts import render
from django.http import JsonResponse,HttpResponse 

# Create your views here.

def index(request):
    if request.method=='GET':
        return JsonResponse({"req_method":"get"})
    elif request.method=='POST':
        return JsonResponse({"req_method":"post"})
    else: return JsonResponse({"error":"request method not allowed"},status=405)
'''
JsonResponse({"req_method":"get"})
JsonResponse({"req_method":"post"})
JsonResponse({"error":"request method not allowed"})
HttpResponse(status=200)
'''