from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register(r'snippets', views.Snippets, basename="snippet")
# router.register(r'user', views.UserList, basename="user")

urlpatterns = [
    path('snippet/', views.snippet),
    path('snippets/<int:pk>', views.snippets),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
    # path('snippets/', views.Snippets.as_view()),
    # path('snippets/<int:pk>/', views.SnippetsDetail.as_view())
    # path('', include(router.urls)),
]
