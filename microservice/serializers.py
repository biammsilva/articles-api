from rest_framework_mongoengine.serializers import serializers, DocumentSerializer
from microservice import models
from datetime import datetime

class ArticleInput(serializers.Serializer):
    a = serializers.CharField()
    b = serializers.CharField()
    c = serializers.IntegerField()

    def save(self):
        data = self.validated_data
        article = models.Article()
        article.save()
        return ArticleOutput(article).data


class ArticleOutput(DocumentSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'


class UserInput(serializers.Serializer):
    a = serializers.CharField()
    b = serializers.CharField()
    c = serializers.IntegerField()

    def save(self):
        data = self.validated_data
        user = models.User()
        user.save()
        return UserOutput(user).data


class UserOutput(DocumentSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
