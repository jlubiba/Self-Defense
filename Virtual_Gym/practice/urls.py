from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "practice"

urlpatterns = [
    path("", views.index, name="home")
]

router = DefaultRouter(trailing_slash = False)
# router.register("techniques-form", views.xyz, basename = "techniques")
# router.register("combos-form", views.xyz, basename = "combos")
# router.register("techniques", views.xyz, basename = "techniques")
# router.register("combos", views.xyz, basename = "combos")
# router.register("combos", views.xyz, basename = "combos")

urlpatterns += router.urls