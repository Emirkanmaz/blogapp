from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    Objects = models.Manager()
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Blog(models.Model):
    Objects = models.Manager()
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    is_active = models.BooleanField()
    is_home = models.BooleanField()
    description = RichTextField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    categories = models.ManyToManyField(Category, blank=True)
    # category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# class CategoryTest(models.Model):
#     Objects = models.Manager()
#     name = models.CharField(max_length=50)
#     slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
#
#     def __str__(self):
#         return self.name
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super().save(*args, **kwargs)
#
#
# class BlogTest(models.Model):
#     Objects = models.Manager()
#     title = models.CharField(max_length=200)
#     image = models.ImageField(upload_to="blogs")
#     is_active = models.BooleanField()
#     is_home = models.BooleanField()
#     description = RichTextField()
#     slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
#     category = models.ManyToManyField(CategoryTest, through='BlogCategoryTest')
#
#     def __str__(self):
#         return self.title
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         super().save(*args, **kwargs)
#
#
# class BlogCategoryTest(models.Model):
#     Objects = models.Manager()
#     blogtest = models.ForeignKey(BlogTest, on_delete=models.CASCADE)
#     categorytest = models.ForeignKey(CategoryTest, on_delete=models.CASCADE)
#     mmrelationship = models.BooleanField(default=False)


