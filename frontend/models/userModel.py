from mongoengine import StringField, EmailField, IntField, Document

class Users(Document):
    userName = StringField(required=True)
    email = EmailField(required=True)
    password = StringField(required=True)
    
    