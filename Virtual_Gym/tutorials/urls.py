from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "tutorials"

urlpatterns = [
    path("", views.index, name="home"),
    path("home1", views.index00, name="home1"),
    path("tttutorial", views.WelcomeTTutorial.as_view(), name="tttutorial"),
    path("tttutorial/category/<int:pk>", views.SingleCategoryTTutorial.as_view(), name="tttutorial_single_category"),
    path("tttutorial/categories", views.AllCategoryTTutorial.as_view(), name="ttutorial_all_category"),
    path("tttutorial/category/subcategory/<int:pk>", views.SingleSubCategoryTTutorial.as_view(), name="tttutorial_single_subcategory"),
    path("tttutorial/technique/<int:pk>", views.SingleTechniqueTTutorial.as_view(), name="tttutorial_technique"),
    path('tttutorial/add-category', views.AddCategoryView.as_view(), name='add_category'),
    path("tttutorial/combo/<int:pk>", views.SingleComboTTutorial.as_view(), name="tttutorial_combo"),
    path('tttutorial/combos', views.AllComboTTutorial.as_view(), name='ttutorial_all_combo'),
    path('tttutorial/add-subcategory', views.AddSubategoryView.as_view(), name='add_subcategory'),
    path('tttutorial/add-technique', views.AddTechniqueView.as_view(), name='add_technique'),
    path('tttutorial/add-combo', views.AddComboView.as_view(), name='add_combo'),
    path("test", views.test, name="test"),
    path("ttest", views.ttest, name="ttest"),
    path("vtest/<int:pk>", views.vtest.as_view(), name="vtest"),
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