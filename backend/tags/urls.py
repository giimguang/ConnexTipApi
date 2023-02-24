from django.urls import path
from . import views

urlpatterns = [
    path('', views.TagList.as_view()),
    path('create/', views.TagCreate.as_view()),
    path('update/<int:pk>', views.TagUpdate.as_view()),
    path('delete/<int:pk>', views.TagDelete.as_view()),
]
