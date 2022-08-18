from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Blog, Category


# data = {
#     "blogs": [
#         {
#             "id": 1,
#             "title": "komple web geliştirme",
#             "image": "1.jpeg",
#             "is_active": True,
#             "is_home": False,
#             "description": "çok iyi bir kurs"
#         },
#         {
#             "id": 2,
#             "title": "python kursu",
#             "image": "2.jpeg",
#             "is_active": True,
#             "is_home": True,
#             "description": "çok iyi bir kurs"
#         },
#         {
#             "id": 3,
#             "title": "django kursu",
#             "image": "3.jpeg",
#             "is_active": True,
#             "is_home": True,
#             "description": "çok iyi bir kurs"
#         }
#     ]
# }


# Create your views here.
def index(request):
    context = {
        "blogs": Blog.Objects.filter(is_active=True, is_home=True),
        "categories": Category.Objects.all(),
        "navbar": Category.Objects.all()
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": Blog.Objects.filter(is_active=True),
        "categories": Category.Objects.all(),
        "navbar": Category.Objects.all()
    }
    return render(request, "blog/blogs.html", context)


def blog_details(request, slug):
    # blogs = data["blogs"]
    # selectedBlog = [blog for blog in blogs if blog["id"] == id][0]
    blog = Blog.Objects.get(slug=slug)
    return render(request, "blog/blog-details.html", {
        "blog": blog
    })


def categorylist(request):
    return render(request, "blog/categorylist.html")


def categorydetail(request, slug):
    context = {
        # "blogs": Blog.Objects.filter(is_active=True, categories__slug=slug),
        "blogs": Category.Objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories": Category.Objects.all(),
        "navbar": Category.Objects.all(),
        "selected_category": slug
    }
    return render(request, "blog/blogs.html", context)

# def blogs_by_category(request, slug):
#     context = {
#         "blogs": Blog.Objects.filter(is_active=True, category__slug=slug),
#         "categories": Category.Objects.all(),
#         "navbar": Category.Objects.all()
#     }
#     return render(request, "blog/blogs_by_category.html", context)
