from django.urls import path

from . import views


urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("home/", views.home, name="home"),
    path('create_post/', views.create_post, name='create_post'),
    path("<int:post_id>/", views.post_detail, name="post_detail"),
    path('delete/<int:id>', views.delete, name='delete'),
]
