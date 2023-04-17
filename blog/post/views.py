from django.shortcuts import render #он соединяет 2 файла?
from .models import Post

# Create your views here.

def posts_list(request):
    queryset = Post.objects.all()  #objects - в ней содержится все данные в бд
    return render(request, 'listing.html', {'posts' : queryset})
    # posts - при обращении по этому ключи мы переходим в queryset

"REST"
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def posts_list_api_view(request):
    queryset = Post.objects.all()
    serializer =  PostSerializer(queryset, many= True)  #many= True пишем, если хотим работать со списком с различными значениями
    return Response(serializer.data)

@api_view(['GET'])
def posts_details(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['POST'])
def create_post(request):
    # print(request.data)
    # return Response(status=200)
    serializer = PostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201) 

@api_view(['DELETE'])
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return Response(status=204)

@api_view(["PUT"])
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializer(post, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201) 

@api_view(["PATCH"])
def partial_update_post(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializer(post, data=request.data, partial=True) 
    # partial=True нужно если хотим частично обновить
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201) 

# @api_view(["PUT", "PATCH"])
# def update_post(request, id):
#     post = get_object_or_404(Post, id=id)
#     partial = True if request.method == "PATCH" else False
#     serializer = PostSerializer(post, data=request.data, partial=partial) 
#     # partial=True нужно если хотим частично обновить
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=201) 

from rest_framework.viewsets import ModelViewSet

# class PostViewSet(ModelViewSet):
