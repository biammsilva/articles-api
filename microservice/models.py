from mongoengine import Document, fields
from datetime import datetime

class User(Document):
    name = fields.StringField(required=True)
    email = fields.StringField(required=True)
    password = fields.StringField(require=True)
    created_at = fields.DateTimeField()

    def createArticle(self, **kwargs):
        return Article(**kwargs,
                       author=self,
                       created_at=datetime.now(),
                       likes = Like(users = [], counter = 0).save()).save()

class Like(Document):
    users = fields.ListField(fields.EmbeddedDocumentField('User'))
    counter = fields.IntField()

class Article(Document):
    title = fields.StringField(required=True)
    author = fields.EmbeddedDocumentField('User')
    likes = fields.EmbeddedDocumentField('Like')
    content = fields.StringField(required=True)
    created_at = fields.DateTimeField()

    def getLikesNumber(self):
        return likes.counter

class UserAuth(Document):
    user = fields.EmbeddedDocumentField('User')
    date = fields.DateTimeField()
    logged_in = fields.IntField()
    hash = fields.StringField(required=True)

    def logout(self):
        self.logged_in = 0
        self.save()
