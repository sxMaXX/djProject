from django.db import models
from django.db.models import CharField, EmailField, ImageField



# Create your models here.
class ModelMaXX(models.Model):
    login = CharField(max_length=30)
    password = CharField(max_length=30)
    email = EmailField(max_length=80)
    user_image = ImageField(upload_to='app/static', null=True)

class ProfileImg(models.Model):
    user_image = models.ImageField(upload_to='app/static', verbose_name=u'Ваше фото')



