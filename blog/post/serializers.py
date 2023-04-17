from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta: #нужен класс мету чисто для логики и дальнейшего удобства
        model = Post
        fields = '__all__'
    
    #показывает отображение нашего поста. 
    def to_representation(self, instance):
        rep = super().to_representation(instance) #он возвращает его в виде словаря. для этого нужен super
        rep['likes'] = instance.likes.all().count()
        # print('REP', rep)
        return rep