from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "blog"

router = DefaultRouter(trailing_slash=False)
router.register(r"blogs", views.allBlogs,basename="blogs")
# router.register(r"tags", views.xyz,basename="tags")
# router.register(r"tags/<int:tagId>", views.xyz,basename="tag")
router.register(r"categories", views.Category,basename="categories")
router.register(r"authors", views.author,basename="authors")
# router.register(r"categories/<int:categoryId>", views.xyz,basename="category")
# router.register(r"favorite", views.xyz,basename="favorite-blogs")
# router.register(r"favorite/<int:blogId>", views.xyz,basename="favorite-blog")
# router.register(r"blogs/<int:blogId>", views.xyz,basename="blog")
# -------  Need to add the comment ones ------- 

urlpatterns = [
    path("", views.index, name="home"),
    path("testblog", views.blogs.as_view(), name="testblog"),
    path("", include(router.urls)),
]