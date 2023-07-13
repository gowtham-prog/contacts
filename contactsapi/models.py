from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 150, null = False, blank = False)
    mobile = models.IntegerField(null = False, blank = False)
    email = models.EmailField(blank = True , null = True)
    spam = models.BooleanField(default = False)
    def __str___(self):
        return f'{self.id}--{self.name}--{self.mobile}'
class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= "owner", null = False)
    mobile = models.IntegerField(null = False, blank = False,unique=True)
    email = models.EmailField(blank=True, null = True )
    spam = models.BooleanField(default = False)
    def __str___(self):
        return f'{self.id}--{self.user.name}'
class Mapper(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = False)
    contact = models.ForeignKey(Contact, on_delete = models.CASCADE, null = False)
    def __str___(self):
        return f'{self.id}--{self.user.name}'