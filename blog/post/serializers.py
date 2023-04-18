from rest_framework.serializers import ModelSerializer
from .models import Post
from review.serializers import CommentSerializer

class PostSerializer(ModelSerializer):
    class Meta: #нужен класс мету чисто для логики и дальнейшего удобства
        model = Post
        fields = '__all__'
    
    #показывает отображение нашего поста. 
    def to_representation(self, instance):
        rep = super().to_representation(instance) #он возвращает его в виде словаря. для этого нужен super
        rep['likes'] = instance.likes.all().count()
        # print('REP', rep)
        comments = instance.comments.all() #все комменты данного поста
        rep['comments'] = CommentSerializer(comments, many=True).data
        #когда у нас много комментраиев к посту, то нужно указывать many=True
        #data - пишем его, так как хотим вытащить не просто обект, а именно данные обекта???
        return rep