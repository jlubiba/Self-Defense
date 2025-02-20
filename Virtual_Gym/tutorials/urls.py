from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "tutorials"

urlpatterns = [
    path("", views.index, name="home"),
    path("home1", views.index00, name="home1"),
    path("written", views.WelcomeTTutorial.as_view(), name="tttutorial"),
    path("videos", views.WelcomeVTutorial.as_view(), name="vtutorial"),
    path("written/category/<int:pk>", views.SingleCategoryTTutorial.as_view(), name="tttutorial_single_category"),
    path("videos/category/<int:pk>", views.SingleCategoryVTutorial.as_view(), name="vtutorial_single_category"),
    path("categories", views.AllCategoryTTutorial.as_view(), name="ttutorial_all_category"),
    path("written/category/subcategory/<int:pk>", views.SingleSubCategoryTTutorial.as_view(), name="tttutorial_single_subcategory"),
    path("videos/category/subcategory/<int:pk>", views.SingleSubCategoryVTutorial.as_view(), name="vtutorial_single_subcategory"),
    path('combo/edit/<int:pk>/', views.UpdateComboView.as_view(), name='update_combo'),
    path('technique/edit/<int:pk>/', views.UpdateTechniqueView.as_view(), name='update_technique'),
    path('category/edit/<int:pk>/', views.UpdateCategoryView.as_view(), name='update_category'),
    path('category/subcategory/edit/<int:pk>/', views.UpdateSubCategoryView.as_view(), name='update_subcategory'),
    path('category/subcategory/remove/<int:pk>/', views.DeleteCategoryView.as_view(), name='delete_category'),
    path('combo/remove/<int:pk>/', views.DeleteSubCategoryView.as_view(), name='delete_subcategory'),
    path('technique/remove/<int:pk>/', views.DeleteComboView.as_view(), name='delete_combo'),
    path('category/remove/<int:pk>/', views.DeleteTechniqueView.as_view(), name='delete_technique'),
    path("technique/<int:pk>", views.SingleTechniqueTTutorial.as_view(), name="tttutorial_technique"),
    path('videos/add-category', views.AddCategoryView.as_view(), name='add_category'),
    path("videos/combo/<int:pk>", views.SingleComboTTutorial.as_view(), name="tttutorial_combo"),
    path("combo/<int:combo_pk>/technique/<int:pk>", views.SingleTechniqueComboTTutorial.as_view(), name="tttutorial_combo_technique"),
    path('combos', views.AllComboTTutorial.as_view(), name='ttutorial_all_combo'),
    path('category/subcategory/add-subcategory', views.AddSubategoryView.as_view(), name='add_subcategory'),
    path('technique/add-technique', views.AddTechniqueView.as_view(), name='add_technique'),
    path('combo/add-combo', views.AddComboView.as_view(), name='add_combo'),
    path('like/<int:pk>', views.LikedVideoTT, name='video_like'),
    path('video/<int:pk>/comment/', views.AddCommentPostView.as_view(), name='video_comment'),
    path("test", views.test, name="test"),
    path("ttest", views.ttest, name="ttest"),
    path("videos/category/subcategory/<int:sub_pk>/vtest/<int:pk>", views.vtest.as_view(), name="vtest"),
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