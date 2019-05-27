from django.urls import path
from . import views

# urls for specific views
urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("blog_index/", views.project_index, name="blog_index"),
]
