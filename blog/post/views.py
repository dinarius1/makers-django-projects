from django.shortcuts import render #он соединяет 2 файла?
from .models import Post

# Create your views here.

def posts_list(request):
    queryset = Post.objects.all()  #objects - в ней содержится все данные в бд
    return render(request, 'listing.html', {'posts' : queryset})
    # posts - при обращении по этому ключи мы переходим в queryset