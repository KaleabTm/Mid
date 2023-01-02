from django.urls import path

from . import views


urlpatterns = [
    path('studList/', views.StudentList.as_view()),
    path('studCreate/', views.StudentCreate.as_view()),
    path('studUpdate/<pk>/', views.StudentList.as_view()),
    path('studDelete/<pk>/', views.StudentList.as_view()),
]
 