from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiles.models import Profile,ProfileStatus
from profiles.api.serializers import ProfileSerializer,ProfileStatusSerializer,ProfileAvatarSerializer

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets
from rest_framework import mixins
from profiles.api.permissions import IsOwnerProfileOrReadOnly,IsOwnerOrReadOnly


from rest_framework.viewsets import ModelViewSet
############FOR AVATAR########################
class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object

#baseline viewset
class ProfileListView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


##ReadonlyViewset
class ProfileReadOnlyView(ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


###with mixins
class ProfileViewSet(mixins.UpdateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly]


## Model Viewset/ Recommend
class ProfileStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self,serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile = user_profile)