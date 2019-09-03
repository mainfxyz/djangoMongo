import mongoengine

class ShopDB(mongoengine.Document):
    name = mongoengine.StringField(max_length=40)
    price = mongoengine.FloatField(default=0)
    shop = mongoengine.StringField(max_length=40)
    img = mongoengine.StringField(max_length=200)
    comment = mongoengine.ListField(default="")

class User(mongoengine.Document):
    username=mongoengine.StringField(max_length=20)
    password=mongoengine.StringField(max_length=20)