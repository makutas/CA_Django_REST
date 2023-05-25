from django.urls import path
from .views import PostList, PostDetail, CommentList, CommentDetail, PostLikeCreate

urlpatterns = [
    path('posts', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('posts/<int:pk>/comments', CommentList.as_view()),
    path('comments/<int:pk>', CommentDetail.as_view()),
    path('posts/<int:pk>/likes', PostLikeCreate.as_view()),
]