from django.urls import path
# from .views import article_list, article_detail_view
from api.views import ArticleList, ArticleDetails

urlpatterns = [
    path('articles/', ArticleList.as_view(), name="articles"),
    path('articles/<int:id>', ArticleDetails.as_view()),
]