from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from microservice import models
from microservice import serializers
from microservice import auth
from microservice.const import authorization_views

class BaseView(viewsets.GenericViewSet):
    queryset = None
    input_serializer = None
    output_serializer = None

    def get_serializer_class(self):
        return self.input_serializer

    def create(self, request):
        data = request.data
        serializer = self.input_serializer(data=data)
        if request._request.path in authorization_views:
            if 'HTTP_AUTHORIZATION' not in request.META or \
             not auth.authenticate_user(request.META["HTTP_AUTHORIZATION"]):
                return Response({'message': "Authorization is required"}, 401)
        if serializer.is_valid():
            return Response(*serializer.save())
        return Response(serializer.errors, 500)

    def list(self, request):
        return Response(self.output_serializer(many=True).data, 200)

    def retrieve(self, request, id=None):
        return Response(self.output_serializer(self.queryset(id=id).first()).data, 200)

class ArticleView(BaseView):
    queryset = models.Article.objects
    input_serializer = serializers.ArticleInput
    output_serializer = serializers.ArticleOutput

class UserView(BaseView):
    queryset = models.User.objects
    input_serializer = serializers.UserInput
    output_serializer = serializers.UserOutput

class UserAuthView(BaseView):
    queryset = models.UserAuth.objects
    input_serializer = serializers.UserAuthInput
    output_serializer = serializers.UserAuthOutput

class UserLogoutView(BaseView):
    queryset = models.UserAuth.objects
    input_serializer = 'None'
    output_serializer = 'None'

    def list(self, request):
        if 'HTTP_AUTHORIZATION' in request.META:
            return Response({'logged_off': auth.logout(request.META['HTTP_AUTHORIZATION'])}, 200)
        return Response({'message': "Authorization is required"}, 401)
