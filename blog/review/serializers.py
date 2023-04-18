from rest_framework.serializers import ModelSerializer
from .models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        # fields = '__all__' #__all__ берет все поля из Comment
        exclude = ['user'] #список, который вы передадите, не будет отображаться 
        #убираем его, так как все время требуется имя пользователя при создании коммента

    def validate(self, attrs):
        super().validate(attrs)  #проверит все данные
        request = self.context.get('request') #context позволяет вытащить request через сереализатор
        attrs['user'] = request.user
        return attrs