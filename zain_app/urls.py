from django.urls import path
from .views import UserlistView,UserkDetailsView,UserUpdateView,UserDeleteView,UserAddView

urlpatterns=[
  path('',UserlistView.as_view(),name='users'),
  path('users_details/<int:pk>',UserkDetailsView.as_view(),name='users_details'),
  path('users/new',UserAddView.as_view(),name='users_create'),
  path('users/<int:pk>/edit',UserUpdateView.as_view(),name='users_edit'),
  path('users/<int:pk>/delete',UserDeleteView.as_view(),name='user_delete'),
]
