from mongoengine import Document, fields

class User(Document):
    name = fields.StringField(required=True)
    email = fields.StringField(required=True)
    birth_date = fields.DateTimeField()
    password = fields.StringField(require=True)
    created_at = fields.DateTimeField()

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
    created_at = fields.DateTimeField()

    def getLikesNumber():
        return likes.counter
