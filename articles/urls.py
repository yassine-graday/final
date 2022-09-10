from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ArticleViewSet,TagListAPIView
)


article_detail = ArticleViewSet.as_view({
    'get': 'retrieve'
})


article_list = ArticleViewSet.as_view({
    'get': 'list'
})

router = DefaultRouter(trailing_slash=False)
router.register(r'articles', ArticleViewSet)

app_name = 'articles'
urlpatterns = [
    path('', include(router.urls)),
    path('articles/', article_list, name='article-list'),
    path('articles/<str:slug>/', article_detail, name='article-detail'),
    path('tags', TagListAPIView.as_view()),
]
