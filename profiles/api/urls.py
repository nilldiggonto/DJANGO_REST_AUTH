from django.urls import path,include
from profiles.api.views import (ProfileListView,ProfileReadOnlyView,ProfileViewSet,
                                                    ProfileStatusViewSet,AvatarUpdateView)
from rest_framework.routers import DefaultRouter




# profile_list = ProfileReadOnlyView.as_view({'get':'list'})
# profile_detail = ProfileReadOnlyView.as_view({'get':'retrieve'})


router = DefaultRouter()
router.register(r'profiles',ProfileViewSet)
router.register(r'status',ProfileStatusViewSet)

app_name = 'profiles'
urlpatterns = [
    path('',include(router.urls)),
    path('avatar/',AvatarUpdateView.as_view(),name='avatar'),
#     path('profile/',ProfileListView.as_view(),name='profile'),
#     path('profile/read/',profile_list,name='profile-read'),
#     path('profile/read/<int:pk>/',profile_detail,name='profile-detail'),
]