from mongoengine import Document, fields
from datetime import datetime

class User(Document):
    name = fields.StringField(required=True)
    email = fields.StringField(required=True)
    password = fields.StringField(require=True)
    created_at = fields.DateTimeField(default=datetime.now())

    def createArticle(**kwargs):
        return Article(**kwargs, likes = Like(user = [], counter = 0)).save()

class Like(Document):
    user = fields.ListField(fields.EmbeddedDocumentField('User'))
    counter = fields.IntField()

class Article(Document):
    title = fields.StringField(required=True)
    author = fields.EmbeddedDocumentField('User')
    likes = fields.EmbeddedDocumentField('Like')
    content = fields.IntField(required=True)
    created_at = fields.DateTimeField(default=datetime.now())

    def getLikesNumber():
        return likes.counter
