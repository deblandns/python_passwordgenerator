from django.db import models

# Create your models here.


class passgenerator(models.Model) :
    number = models.IntegerField()
    lowercase = models.CharField(max_length=40)
    lettercase = models.CharField(max_length=40)
    symbols = models.CharField(max_length=30 , null=True)

    def __index__(self):
       return self.number


