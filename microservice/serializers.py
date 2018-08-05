from rest_framework_mongoengine.serializers import serializers, DocumentSerializer
from microservice import models
from microservice import auth
from datetime import datetime
import hashlib

class ArticleInput(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()

    def save(self):
        data = self.validated_data
        article = models.Article(article)
        article.save()
        return ArticleOutput(article).data


class ArticleOutput(DocumentSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'


class UserAuthInput(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def save(self):
        data = self.validated_data
        user = models.User.objects(email = data['email'],
                                   password = hashlib.sha224(data['password'].encode('utf-8')).hexdigest()).first()
        if user:
            user_hash = auth.new_user_authentication(user)
            if user_hash:
                return {"hash": user_hash}, 200
            return {'message': 'Already logged in'}, 200
        return {'message': 'not authorized'}, 401


class UserAuthOutput(DocumentSerializer):
    class Meta:
        model = models.UserAuth
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
            return UserOutput(user).data, 200
        return {'message': 'User already exist'}, 400


class UserOutput(DocumentSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
