from django.urls import path 
from . import views
from .views import EndpointsView, AdvocateListView, AdvocateDetailsView, CompanyListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)






urlpatterns = [
    
    
    
    
 
    path('', EndpointsView.as_view()),
    path('advocates/', AdvocateListView.as_view()),
    path('advocates/<str:username>/', AdvocateDetailsView.as_view()),
    path('companies/', CompanyListView.as_view()),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
