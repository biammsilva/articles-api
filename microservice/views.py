from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from microservice import models
from microservice import serializers

class BaseView(viewsets.GenericViewSet):
    queryset = None
    input_serializer = None
    output_serializer = None

    def get_serializer_class(self):
        return self.input_serializer

    def create(self, request):
        data = request.data
        serializer = self.input_serializer(data=data)
        if serializer.is_valid():
            return Response(serializer.save(), 200)
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
