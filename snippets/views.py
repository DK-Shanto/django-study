from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets

'''Function based view is here'''


@api_view(['GET', 'POST', 'PUT'])
def snippet(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data
        # data = JSONParser().parse(request)
        print(type(data))
        serializer = SnippetSerializer(data=data)
        print(serializer)

        if serializer.is_valid():
            announce=serializer.save(owner=request.user)
            another=serializer.data
            print(another)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def snippets(request, pk):
    sni = Snippet.objects.get(pk=pk)
    if request.method == 'PUT':
        serializer = SnippetSerializer(sni, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        sni.delete()
        return Response(status=status.HTTP_200_OK)


'''Class based view is here'''

# class Snippets(APIView):
#     def get(self, request):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         data = request.data
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class SnippetDetail(APIView):
#     def get_object(self, pk):
#         return Snippet.objects.get(pk=pk)
#
#     def get(self, request, pk):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_200_OK)


'''Mixins and Generics together'''

# class Snippets(mixins.ListModelMixin,
#                mixins.CreateModelMixin,
#                generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class SnippetsDetail(mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


'''class based generic views'''

# @permission_classes([permissions.IsAuthenticatedOrReadOnly,
#                      IsOwnerOrReadOnly])
# class Snippets(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def perform_create(self, serializer):
#         print(self.request.user)
#         serializer.save(owner=self.request.user)
#
#
# @permission_classes([permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly])
# class SnippetsDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer


'''User added view generic view class based'''

#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


'''viewsets'''

# class UserList(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class Snippets(viewsets.ModelViewSet):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
