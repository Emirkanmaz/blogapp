from django.urls import path
from . import views

# http://127.0.0.1:8000/                    => homepage
# http://127.0.0.1:8000/index               => homepage
# http://127.0.0.1:8000/blogs               => blogs
# http://127.0.0.1:8000/blogs/3             => blog-details
# http://127.0.0.1:8000/categorylist/       => categorylist
# http://127.0.0.1:8000/categorylist/3      => categorylist-details

urlpatterns = [
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name="logout"),

]
