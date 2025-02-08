from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "tutorials"

urlpatterns = [
    path("", views.index, name="home"),
    path("home1", views.index00, name="home1"),
    path("test", views.test, name="test"),
    path("ttest", views.ttest, name="ttest"),
    path("technique", views.TechniqueGenerator, name="technique"),
]

router = DefaultRouter(trailing_slash = False)
router.register(r"tags", views.tag,basename="tags")
router.register(r"categories", views.category, basename="categories")
router.register(r"subcategories", views.subCategory, basename="sub-categories")
router.register(r"videos", views.videoTutotial,basename="videos")
router.register(r"texts", views.textTutorial,basename="texts")
router.register(r"targets", views.target,basename="targets")
router.register(r"combos", views.combo,basename="combos")
router.register(r"techniques", views.technique,basename="techniques")

urlpatterns += router.urls