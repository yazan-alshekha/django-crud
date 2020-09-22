from django.urls import path
from .views import UserlistView,UserkDetailsView,UserAddView,UserUpdateView,UserDeleteView

urlpatterns=[
  path('users',UserlistView.as_view(),name='users'),
  path('users_details/<int:pk>',UserkDetailsView.as_view(),name='users_details'),
  path('users/new',UserAddView.as_view(),name='users_create'),
  path('users/<int:pk>/update',UserUpdateView.as_view(),name='users_create'),
  path('users/<int:pk>/delete',UserDeleteView.as_view(),name='user_delete'),
]
