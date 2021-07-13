# from django_react.api.views import ArticleViewSet
from django.urls import path, include
# from .views import article_list, article_detail_view
# from api.views import ArticleList, ArticleDetails
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, UserViewSet
routers = DefaultRouter()
routers.register('articles', ArticleViewSet, basename = 'articles')
routers.register('users', UserViewSet, basename = 'users')

urlpatterns = [
    # path('articles/', ArticleList.as_view(), name="articles"),
    # path('articles/<int:id>', ArticleDetails.as_view()),
    path('api/', include(routers.urls)), 
]