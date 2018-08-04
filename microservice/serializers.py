from rest_framework_mongoengine.serializers import serializers, DocumentSerializer
from microservice import models
from datetime import datetime

class ArticleInput(serializers.Serializer):
    a = serializers.CharField()
    b = serializers.CharField()
    c = serializers.IntegerField()

    def save(self):
        data = self.validated_data
        article = models.Article(article)
        article.save()
        return ArticleOutput(article).data


class ArticleOutput(DocumentSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'


class UserInput(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    def save(self):
        data = self.validated_data
        if not models.User.objects(email = data['email']).all():
            user = models.User(**data)
            user.save()
            return UserOutput(user).data
        return {'message': 'User already exist'}


class UserOutput(DocumentSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
