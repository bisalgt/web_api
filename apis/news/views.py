from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404

from helpers.permissions import IsNewsCreator
from apis.news.serializers import CreateNewsSerializers, UpdateNewsSerializers
from apis.news.models import News


class CreateNewsAPIView(CreateAPIView):
    permission_classes = [IsNewsCreator]
    serializer_class = CreateNewsSerializers

class UpdateNewsAPIView(UpdateAPIView):

    def get_queryset(self):
        print(self.kwargs)
        return News.objects.filter(pk=self.kwargs['pk'])


    # def get_queryset(self, *args, **kwargs):
    #     print('-------------------------------------')
    #     print(self)
    #     print('-------------------------------------')
    #     print(args)
    #     print('-------------------------------------')
    #     print(kwargs)
    #     print('-------------------------------------')
    #     print(self.request)
    #     print('-------------------------------------')
    #     print(self.request.user)
    #     print(self.get_object())
    #     print(self.request.news)
    #     print('-------------------------------------')
    #     super().get_queryset(*args, **kwargs)
    #     return self.get_object()
    # queryset = News.objects.get(pk=1)
    permission_classes = [IsNewsCreator]
    serializer_class = UpdateNewsSerializers