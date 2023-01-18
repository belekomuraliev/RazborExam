from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import News, Comment, Status, CommentStatus, NewsStatus
from .permissions import IsAuthorPermission
from .serializers import NewsSerializer, CommentSrializer, StatusSrializer, NewsStatusSrializer


class NewsNumberPagination(PageNumberPagination):
    page_size = 1


class NewsCreateListAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthorPermission]
    pagination_class = NewsNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['created']
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user.author
        )


class NewsUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthorPermission, ]

    def get_object(self):
        return get_object_or_404(News, pk=self.kwargs.get('news_id'))


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSrializer
    permission_classes = [IsAuthorPermission, ]

    def get_queryset(self):
        return super().get_queryset().filter(news_id=self.kwargs.get('news_id'))

    def perform_create(self, serializer):
        serializer.save(
            news_id=self.kwargs.get('news_id'),
            author=self.request.user.author
        )


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSrializer
    permission_classes = [IsAuthorPermission, ]

    def get_object(self):
        return get_object_or_404(Comment, pk=self.kwargs.get('comment_id'))

    def get_queryset(self):
        return super().get_queryset().filter(news_id=self.kwargs.get('news_id'))


class StatusListCreateAPIView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSrializer
    permission_classes = [IsAdminUser]


class StatusRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSrializer
    permission_classes = [IsAdminUser]


class NewsStatusCreateAPIV(APIView):

    def get(self, request, *args, **kwargs):
        status = Status.objects.get(slug=kwargs.get('slug'))
        news = News.objects.get(id=kwargs.get('news_id'))
        try:
            NewsStatus.objects.create(
                status=status,
                news=news,
                author=self.request.user.author
            )
            return Response("Status added", status=201)
        except:
            return Response(f'You already added status', status=204)


class CommentStatusCreateAPIV(APIView):

    def get(self, request, *args, **kwargs):
        status = Status.objects.get(slug=kwargs.get('slug'))
        comment = Comment.objects.get(id=kwargs.get('comment_id'))
        try:
            CommentStatus.objects.create(
                status= status,
                comment= comment,
                author= self.request.user.author
            )
            return Response("Status added", status=201)
        except:
            return Response("You already added status", status=204)



