from django.shortcuts import render
from rest_framework.generics \
        import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404

from helpers.permissions import IsNewsCreator
from apis.news.serializers \
        import CreateNewsSerializers, UpdateNewsSerializers, ListNewsSerializers, RetrieveNewsSerializers, DestroyNewsSerializers
from apis.news.models import News


class CreateNewsAPIView(CreateAPIView):
    permission_classes = [IsNewsCreator]
    serializer_class = CreateNewsSerializers

class UpdateNewsAPIView(UpdateAPIView):
    permission_classes = [IsNewsCreator]
    serializer_class = UpdateNewsSerializers

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


class ListNewsAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListNewsSerializers
    def get_queryset(self):
        return News.objects.all()



class RetrieveNewsAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = RetrieveNewsSerializers
    def get_queryset(self):
        return News.objects.get(pk=self.kwargs['pk'])
    
    def get_object(self): # before using get_object detail was not found, 404 error
        obj = self.get_queryset()
        return obj



class DestroyNewsAPIView(DestroyAPIView):
    permission_classes = [IsNewsCreator]
    serializer_class = DestroyNewsSerializers
    def get_queryset(self):
        return News.objects.get(pk=self.kwargs['pk'])

    def get_object(self): # before using get_object detail was not found, 404 error
        obj = self.get_queryset()
        return obj