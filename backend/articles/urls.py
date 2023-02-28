from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleList.as_view()),
    path('trending/', views.ArticleTrending.as_view()),
    path('create/', views.ArticleCreate.as_view()),
    path('<str:slug>/', views.ArticleDetail.as_view()),
    path('update/<str:slug>/', views.ArticleUpdate.as_view()),
    path('delete/<str:slug>/', views.ArticleDelete.as_view()),
    path('tag/<str:tag>/', views.ArticleTag.as_view()),
    path('category/<str:category>/', views.ArticleCategory.as_view())
]