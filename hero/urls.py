from rest_framework import routers
from .views import VideoPostViewSet, UserDataViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('videos', VideoPostViewSet , basename='videos') # basename='videos' is optional
router.register('userdata', UserDataViewSet , basename='userdata')
router.register('comments', CommentViewSet , basename='comments')
urlpatterns = router.urls