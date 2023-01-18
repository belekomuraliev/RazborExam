from rest_framework import serializers

from .models import News, Comment, Status, CommentStatus, NewsStatus, Count


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ['author']

    def create(self, validated_data):
            news = News.objects.create(
                title=validated_data['title'],
                content=validated_data['content'],
                author=validated_data['author']
            )
            return news


class CommentSrializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', 'news']


class StatusSrializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class NewsStatusSrializer(serializers.ModelSerializer):
    class Meta:
        model = NewsStatus
        fields = '__all__'


class CommentStatusSrializer(serializers.ModelSerializer):
    class Meta:
        model = CommentStatus
        fields = '__all__'







