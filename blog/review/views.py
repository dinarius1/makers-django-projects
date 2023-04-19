from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
#нихуя не понялa
from rest_framework.permissions import IsAuthenticated

from .models import Like, Comment
from .serializers import CommentSerializer
from post.models import Post, User


@api_view(['POST'])
def toggle_like(request, id):
    user = request.user #в request попадает словарь из данных, и вытаскиваем данные из user
    if not user.is_authenticated:
        return Response(status=401)
    # user_id = request.data.get('user') #request.data. - оттуда выходит json данные
    # if not user_id:
    #     return Response({'user':['this field is required']}, status=400)
    # user = get_object_or_404(User, id = user_id)
    post = get_object_or_404(Post, id = id)
    if Like.objects.filter(user=user,post=post).exists():
        # если лайк есть, то удаляем его
        Like.objects.filter(user=user,post=post).delete()
    else:
        #если нет, то создаем
        Like.objects.create(user=user,post=post)
    return Response(status=201)

class CreateCommentAPIView(CreateAPIView):
    """
    CRUD для комментариев
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated] #чтобы добавлять какие то ограничения

class UpdateCommentAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class DeleteCommentAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]