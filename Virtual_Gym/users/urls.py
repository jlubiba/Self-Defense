from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "users"

urlpatterns = [
    path("", views.index, name="home")
]

router = DefaultRouter(trailing_slash = False)
# router.register("groups/general-manager/users", views.managers, basename = "general-managers") # List and create new people from this group
# router.register("groups/general-manager/users/<int:userId>", views.singleManagerRemoval, basename = "general-manager") # Remove from general-manager groups user with this Id
# router.register("groups/deliver-crew/users", views.deliveryCrew, basename = "delivery-crew") # List and create new people from the delivery-crew group
# router.register("groups/deliver-crew/users/<int:userId>", views.singleDeliveryCrewRemoval, basename = "deliverer") # Remove from delivery-crew groups user with this Id
# router.register("groups/blog-manager-crew/users", views.blogManagers, basename = "blog-managers") # List and create new people from the blog-manager group
# router.register("groups/blog-manager/users/<int:userId>", views.singleBlogManagerRemoval, basename = "blog-manager") # Remove from blog-manager groups user with this Id
# router.register("groups/tutorial-manager-crew/users", views.TutorialManagers, basename = "tutorial-managers") # List and create new people from the tutorial-manager group
# router.register("groups/tutorial-manager/users/<int:userId>", views.singleTutorialManagerRemoval, basename = "tutorial-manager") # Remove from tutorial-manager groups user with this Id
# router.register("groups/store-manager-crew/users", views.storeManagers, basename = "store-managers") # List and create new people from the store-manager group
# router.register("groups/store-manager/users/<int:userId>", views.singleStoreManagerRemoval, basename = "store-manager") # Remove from store-manager groups user with this Id
# router.register("groups/written-tutorial-supervisor/users", views.videoTutorialSupervisor, basename = "video-tutorial-supervisors") # List and create new people from the written-tutorial-supervisor group
# router.register("groups/written-tutorial-supervisor/users/<int:userId>", views.singleVideoTutorialSupervisorRemoval, basename = "video-tutorial-supervisor") # Remove from written-tutorial-supervisor groups user with this Id
# router.register("groups/video-tutorial-supervisor/users", views.writtenTutorialSupervisor, basename = "video-tutorial-supervisors") # List and create new people from the video-tutorial-supervisor group
# router.register("groups/video-tutorial-supervisor/users/<int:userId>", views.singleWrittenTutorialSupervisorRemoval, basename = "video-tutorial-supervisor") # Remove from video-tutorial-supervisor groups user with this Id
# router.register("groups/authors/users", views.authors, basename = "authors") # List and create new people from the author group
# router.register("groups/authors/users/<int:userId>", views.singleAuthorRemoval, basename = "author") # Remove from author groups user with this Id
# ----- add user info edit -----

urlpatterns += router.urls