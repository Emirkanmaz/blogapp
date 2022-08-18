from django.urls import path
from . import views

# http://127.0.0.1:8000/                    => homepage
# http://127.0.0.1:8000/index               => homepage
# http://127.0.0.1:8000/blogs               => blogs
# http://127.0.0.1:8000/blogs/3             => blog-details
# http://127.0.0.1:8000/categorylist/       => categorylist
# http://127.0.0.1:8000/categorylist/3      => categorylist-details

urlpatterns = [
    path("", views.index, name="home"),
    path("index/", views.index, name="home"),
    path("blogs/", views.blogs, name="blogs"),
    path("blogs/<slug:slug>", views.blog_details, name="blog-details"),
    # path("blogs/<slug:slug>", views.blogs_by_category, name="blogs_by_category"),
    path("categorylist/", views.categorylist, name="category-list"),
    path("categorylist/<slug:slug>", views.categorydetail, name="category-detail"),
]
