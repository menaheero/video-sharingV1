from main.models import VideoPost, UserData, Comment
from rest_framework import viewsets, permissions 
from .serializers import VideoPostSerializer, UserDataSerializer, CommentSerializer
# Create your views here.

class VideoPostViewSet(viewsets.ModelViewSet):
    queryset = VideoPost.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VideoPostSerializer
    http_method_names: list[str] = ['get', 'post', 'put', 'delete']
    


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserDataSerializer
    


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CommentSerializer
    

# class PwaViewSet(viewsets.ModelViewSet):
#     queryset = Pwa.objects.all()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = PwaSerializer
#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)
# class PwaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pwa
#         fields = '__all__'
#         read_only_fields = ('user',)
# class PwaViewSet(viewsets.ModelViewSet):
#     queryset = Pwa.objects.all()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = PwaSerializer
#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)
