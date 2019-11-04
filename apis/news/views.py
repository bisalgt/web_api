from django.shortcuts import render
from rest_framework.generics \
        import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

from helpers.permissions import IsNewsCreator, IsNewsAuthor
from apis.news.serializers \
        import CreateNewsSerializers, UpdateNewsSerializers, ListNewsSerializers, RetrieveNewsSerializers, DestroyNewsSerializers
from apis.news.models import News


class CreateNewsAPIView(CreateAPIView):
    authentication_class = [JWTAuthentication]
    permission_classes = [IsNewsCreator]
    serializer_class = CreateNewsSerializers

class UpdateNewsAPIView(UpdateAPIView):
    authentication_class = [JWTAuthentication]
    permission_classes = [IsNewsCreator, IsNewsAuthor]
    serializer_class = UpdateNewsSerializers
    # queryset = News.objects.all()

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



class RetrieveNewsAPIView(RetrieveAPIView): # we should return list of object// filter gives list of object
    permission_classes = [AllowAny]
    serializer_class = RetrieveNewsSerializers
    # queryset = News.objects.all() # also works as the present instance is authomatically taken from the queries list
    def get_queryset(self):
        return News.objects.filter(pk=self.kwargs['pk'])
    
    # def get_object(self): # before using get_object detail was not found, 404 error
    #     obj = self.get_queryset()
    #     return obj



class DestroyNewsAPIView(DestroyAPIView):
    authentication_class = [JWTAuthentication] # not mandatory
    permission_classes = [IsNewsCreator, IsNewsAuthor] # mandatory field
    serializer_class = DestroyNewsSerializers
    queryset = News.objects.all()
    # def get_queryset(self):
    #     return [News.objects.filter(pk=self.kwargs['pk'])]

    # def get_object(self): # before using get_object detail was not found, 404 error
    #     obj = self.get_queryset()
    #     return obj