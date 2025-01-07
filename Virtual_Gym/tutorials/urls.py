from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "tutorials"

urlpatterns = [
    path("", views.index, name="home")
]

router = DefaultRouter(trailing_slash = False)
# router.register(r"tutorials", views.xyz,basename="tutorials")
# router.register(r"tutorials/tags", views.xyz,basename="tags")
# router.register(r"tutorials/tags/<int:tagId>", views.xyz,basename="tag")
router.register(r"tutorials/categories", views.category, basename="categories")
# router.register(r"tutorials/categories/<int:categoryId>", views.xyz,basename="category")
# router.register(r"tutorials/videos", views.xyz,basename="videos")
# router.register(r"tutorials/videos/<int:videoId>", views.xyz,basename="video")
# router.register(r"tutorials/authors", views.xyz,basename="categories")
# router.register(r"tutorials/authors/<int:authorId>", views.xyz,basename="author")
# router.register(r"tutorials/favorite", views.xyz,basename="favorite-tutorials")
# router.register(r"tutorials/favorite/<int:tutorialId>", views.xyz,basename="favorite-tutorial")
# router.register(r"tutorials/<int:tutorialId>", views.xyz,basename="tutorial")

urlpatterns += router.urls