from django.urls import path
from .views import HomeView, PostDetailsView, PostesView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('<int:pk>', PostDetailsView.as_view(), name = 'post_detail'),
    path('postes', PostesView.as_view(), name = 'postes'),
]