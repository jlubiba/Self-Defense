from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "store"

urlpatterns = [
    path("", views.index, name="home")
]

router = DefaultRouter(trailing_slash = False)
# router.register("products", views.products, basename = "products")
# router.register("product/{int:productId}", views.product, basename = "product")
# router.register("cart/products", views.cart, basename = "cart")
# router.register("orders", views.orders, basename = "orders")
# router.register("orders/<int:orderId>", views.order, basename = "order")
# ----- add the payment apis -----

urlpatterns += router.urls

# router = DefaultRouter(trailing_slash = False)
# router.register("xyz", views.xyz, basename = "xyz")

# urlpatterns += router.urls