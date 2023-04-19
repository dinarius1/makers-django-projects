"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from post.views import posts_list, posts_list_api_view, posts_details, create_post, delete_post, update_post, partial_update_post
from review.views import toggle_like, CreateCommentAPIView, UpdateCommentAPIView, DeleteCommentAPIView
from account.views import RegisterUserAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Python 27 API",
        description="makers bootcamp",
        default_version="v1",
    ),
    public=True
)

# сохраянет юрл и показывает что она возвращает
urlpatterns = [
    path('admin/', admin.site.urls),
    path('listing/', posts_list),
    path('api/listing/', posts_list_api_view),
    path('api/details/<int:id>/', posts_details),  #<int:id>/ - пишем это, так как указываем также id
    path('api/create/', create_post),
    path('api/delete/<int:id>/', delete_post),
    path('api/update/<int:id>/', update_post),
    path('api/partial_update/<int:id>/', partial_update_post),
    path('api/like/<int:id>/', toggle_like),
    path('api/register/', RegisterUserAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/comment/create/', CreateCommentAPIView.as_view()), 
    #as_view - делает из класса функцию, так как после пути нужно указать путь
    path('api/comment/update/<int:pk>/', UpdateCommentAPIView.as_view()),
    #<int:pk> - pk, так как в Generic там не id, а pk в look up field
    path('api/comment/delete/<int:pk>/', DeleteCommentAPIView.as_view()),
    path('docs/', schema_view.with_ui('swagger')), #чтобы подключить swagger 
]

#НЕ ЗАБЫВАЙ ЗАКРЫВАТЬ ПУТЬ ССЫЛКИ СЛЕШОМ "/"!!!!!!! Часто ошибки из за этого
