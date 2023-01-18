
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from account import views as account
from news import views as news

schema_view = get_schema_view(
    openapi.Info(
        title="exam API",
        default_version='v0.1',
        description="API для новостного сайта",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/register/', account.AuthorRegisterAPIView.as_view()),
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/token/', obtain_auth_token),
    path('api/news/', news.NewsCreateListAPIView.as_view()),
    path('api/news/<int:news_id>/', news.NewsUpdateDestroyAPIView.as_view()),
    path('api/news/<int:news_id>/comments/', news.CommentListCreateAPIView.as_view()),
    path('api/news/<int:news_id>/comments/<int:comment_id>/', news.CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('api/statuses/', news.StatusListCreateAPIView.as_view()),
    path('api/statuses/<int:pk>/', news.StatusRetrieveUpdateDestroyAPIView.as_view()),
    path('api/news/<news_id>/<str:slug>/', news.NewsStatusCreateAPIV.as_view()),
    path('api/news/<news_id>/comments/<comment_id>/<slug>/', news.CommentStatusCreateAPIV.as_view()),

    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_ui'),
    # path('json_doc/', schema_view.without_ui(cache_timeout=0), name='json_doc'),

]
