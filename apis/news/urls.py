from django.urls import path

from apis.news.views \
    import CreateNewsAPIView, UpdateNewsAPIView, ListNewsAPIView, RetrieveNewsAPIView,DestroyNewsAPIView

urlpatterns = [
    path("create/", CreateNewsAPIView.as_view(), name="create_news"),
    path("update/<int:pk>/", UpdateNewsAPIView.as_view(), name="update_news"),
    path("retrieve/<int:pk>/", RetrieveNewsAPIView.as_view(), name="retrieve_news"),
    path("destroy/<int:pk>/", DestroyNewsAPIView.as_view(), name="destroy_news"),
    path("list/", ListNewsAPIView.as_view(), name="list_news"),
]
