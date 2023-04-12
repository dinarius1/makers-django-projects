from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta: #нужен класс мету чисто для логики и дальнейшего удобства
        model = Post
        fields = '__all__'