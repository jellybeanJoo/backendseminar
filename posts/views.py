from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse,HttpResponse 
from .models import Post 

# Create your views here.

def index(request):
    qs=Post.objects.all()
    show=[{
        "id" : q.id,
        "title" : q.title,
        "contents" : q.contents
    } for q in qs]
    return JsonResponse(show,safe=False)

def detail(request,pk):
    try:
        q=Post.objects.get(id=pk)
        return JsonResponse({"title":q.title,"contents":q.contents})
    except Post.DoesNotExist:
        return JsonResponse({},status=404)
    
def update(request,pk):
    q=Post.objects.get(id=pk)
    if q is None: return JsonResponse({},status=404)
    title=QueryDict(request.body).get("title")
    contents=QueryDict(request.body).get("contents")
    q.title=title if title is not None else q.title
    q.contents=contents if contents is not None else q.contents
    q.save()
    return JsonResponse({"success":True})

def delete(request,pk):
    q=Post.objects.get(id=pk)
    if q is None: return JsonResponse({},status=404)
    q.delete()
    return JsonResponse({"success":True})

def create(request):
    if request.method=='POST':
        title=request.POST.get("title")
        contents=request.POST.get("contents")
        q=Post(title=title,contents=contents)
        q.save()
        return JsonResponse({"success":True})
    # if request.method=='POST':
    #     title=QueryDict(request.body).get("title")
    #     contents=QueryDict(request.body).get("contents")
    #     q=Post(title=title,contents=contents)
    #     q.save()
    #     return JsonResponse({"success":True})

def post(request,pk):
    if request.method=='GET':
        return detail(request,pk)
    if request.method=='PATCH':
        return update(request,pk)
    if request.method=='DELETE': 
        return delete(request,pk)

# def index(request):
#     if request.method=='GET':
#         return JsonResponse({"req_method":"get"})
#     elif request.method=='POST':
#         return JsonResponse({"req_method":"post"})
#     else: return JsonResponse({"error":"request method not allowed"},status=405)

# def crud_get(request,el):
#     try:
#         info=Post.objects.get(id=el)
#     except Post.DoesNotExist:
#         raise Http404("The id does not eixst")
#     return JsonResponse(info)

# def crud_post(request,el):
#     info=Post.objects.get(id=el)
#     if Post.DoesNotExist: 
#         Post.objects.create(
#             id=request.POST['id']
#             title=request.POST['title']
#             contents=request.POST['contents']
#         )
#     else:
#         return HttpResponse("the id already exists")

# def crud_put(request,el):
#     try:
#         info=post.objects.get(id=el)
#     except Post.DoesNotExist:
#         raise Http404("The id does not eixst")
#     info.title=request.PUT['title']
#     info.contents=request.PUT['contents']

# def crud_delete(request,el):
#     try:
#         info=post.objects.get(id=el)
#     except Post.DoesNotExist:
#         raise Http404("The id does not eixst")
#     info.delete()