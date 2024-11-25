from django.urls import path
from .views import RegisterView, LoginView,AddLinkView,UserLinksView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('add-link/', AddLinkView.as_view(), name='add-link'),
    path('user-links/', UserLinksView.as_view(), name='user-links'),
]
