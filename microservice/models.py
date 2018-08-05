from mongoengine import Document, fields

class User(Document):
    name = fields.StringField(required=True)
    email = fields.StringField(required=True)
    password = fields.StringField(require=True)
    created_at = fields.DateTimeField()

    def createArticle(self, **kwargs):
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
