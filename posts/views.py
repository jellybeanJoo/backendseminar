from django.shortcuts import render
from django.http import JsonResponse,HttpResponse 
from .models import Post 

# Create your views here.

def index(request):
    if request.method=='GET':
        return JsonResponse({"req_method":"get"})
    elif request.method=='POST':
        return JsonResponse({"req_method":"post"})
    else: return JsonResponse({"error":"request method not allowed"},status=405)

def crud_get(request,el):
    try:
        info=Post.objects.get(id=el)
    except Post.DoesNotExist:
        raise Http404("The id does not eixst")
    return JsonResponse(info)

def crud_post(request,el):
    info=Post.objects.get(id=el)
    if Post.DoesNotExist: 
        Post.objects.create(
            id=request.POST['id']
            title=request.POST['title']
            contents=request.POST['contents']
        )
    else:
        return HttpResponse("the id already exists")

def crud_put(request,el):
    try:
        info=post.objects.get(id=el)
    except Post.DoesNotExist:
        raise Http404("The id does not eixst")
    info.title=request.PUT['title']
    info.contents=request.PUT['contents']

def crud_delete(request,el):
    try:
        info=post.objects.get(id=el)
    except Post.DoesNotExist:
        raise Http404("The id does not eixst")
    info.delete()