from rest_framework_mongoengine.serializers import serializers, DocumentSerializer
from microservice import models
from datetime import datetime
import hashlib

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
        passw = data.pop('password')
        if not models.User.objects(email = data['email']).all():
            user = models.User(**data,
                               password = hashlib.sha224(passw.encode('utf-8')).hexdigest())\
                               .save()
            return UserOutput(user).data
        return {'message': 'User already exist'}


class UserOutput(DocumentSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
