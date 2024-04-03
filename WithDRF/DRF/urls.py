from django.urls import path
from . import views
urlpatterns = [
    
    path('singleapi/', views.EmployeeCRUDCBV.as_view()),
    path('singleapi/<int:pk>', views.EmployeeCRUDCBV.as_view())
]