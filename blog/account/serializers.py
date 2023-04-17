from rest_framework.serializers import ModelSerializer, CharField, ValidationError #ValidationError - ощибка, которая вызыввется, если что то неправильно указали
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterUserSerializer(ModelSerializer):
    password_confirm = CharField(min_length=7, required=True, write_only=True) #write_only=True - он нужен для проверки пороля, но нам не нужно чтобы оно сохранялось в бд или отображалось

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password_confirm')

    def validate(self, attrs): 
        #мы переопределяем метод validate у класса RegisterUserSerializer
        #attrs - содержит в себе словарь из атрибутов из fields
        super().validate(attrs)
        p1 = attrs.get('password')
        p2 = attrs.pop('password_confirm')
        if p1 != p2:
            raise ValidationError("Password don't match")
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data) 
        # validated_data - сожержит в себе attrs в виде словаря так как kwargs
        