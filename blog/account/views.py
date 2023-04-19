from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterUserSerializer

class RegisterUserAPIView(APIView):

    @swagger_auto_schema(request_body=RegisterUserSerializer()) #позволяет отобразить поля строк в swagger в разделе register
    def post(self, request): #request - содержит в себе данные в виде словаря, который выводит значения по ключам. Данные же он получает из файла urls из ссылок и функций, где расписаны поля, которые заполенены
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=201)
