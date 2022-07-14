from main.models import VideoPost, UserData, Comment
from rest_framework import serializers as serializers
class VideoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPost
        fields = '__all__'
        read_only_fields = ('user', 'pub_date', 'count', 'video_views')


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'
        read_only_fields = ('user',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user',)
        depth = 1
