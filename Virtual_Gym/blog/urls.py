from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "blog"

router = DefaultRouter(trailing_slash=False)
# router.register(r"blogs", views.xyz,basename="blogs")
# router.register(r"blogs/tags", views.xyz,basename="tags")
# router.register(r"blogs/tags/<int:tagId>", views.xyz,basename="tag")
# router.register(r"blogs/categories", views.xyz,basename="categories")
# router.register(r"blogs/categories/<int:categoryId>", views.xyz,basename="category")
# router.register(r"blogs/favorite", views.xyz,basename="favorite-blogs")
# router.register(r"blogs/favorite/<int:blogId>", views.xyz,basename="favorite-blog")
# router.register(r"blogs/<int:blogId>", views.xyz,basename="blog")
# -------  Need to add the comment ones ------- 

urlpatterns = [
    path("", views.index, name="home"),
    path("", include(router.urls)),
]