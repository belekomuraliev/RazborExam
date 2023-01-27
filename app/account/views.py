
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import CreateAPIView
from .models import Author, User
from .serializers import AuthorSerializer


class AuthorRegisterAPIView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

