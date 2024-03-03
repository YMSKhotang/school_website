from django.urls import path
from blog import views 

urlpatterns = [
    path('', views.home, name='home' ),
    path('gallery/', views.gallery, name='gallery' ),
    path('contact/', views.contact, name='contact' ),
    path('search/', views.search, name='search' ),
    path("news/", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
]