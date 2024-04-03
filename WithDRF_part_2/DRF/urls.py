from django.urls import path , include
from DRF.views import TestAPIView ,TestViewSet

# importing defalut router fro drf 
from rest_framework.routers import DefaultRouter


# creating object of DefaultRouter
router = DefaultRouter()

# registering our viewset to the router object



# (drf-view-set ) is our url if any one hits this url TestViewSet will start performing all the activities 

router.register('drf-view-set', TestViewSet, basename='drf-view-set')
urlpatterns = [
    # path('api/' , TestAPIView.as_view()),
    path('' , include(router.urls)),    # registration of defalut router 
]