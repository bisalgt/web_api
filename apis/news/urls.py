from django.urls import path

from apis.news.views import CreateNewsAPIView, UpdateNewsAPIView

urlpatterns = [
    path("create/", CreateNewsAPIView.as_view(), name="create_news"),
    path("update/<int:pk>/", UpdateNewsAPIView.as_view(), name="update_news"),
]
