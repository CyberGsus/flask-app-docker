from mongoengine import Document, StringField, IntField


class Person(Document):
    name = StringField(required=True)
    age = IntField(min_value=1, required=True)