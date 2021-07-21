from django.urls import path
from quickstart import views

urlpatterns = [
    path('Hello-view/', views.HelloApiView.as_view()),
]
