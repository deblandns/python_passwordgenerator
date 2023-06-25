from django.db import models

# Create your models here.

class contactus(models.Model):
    name = models.CharField(max_length=300 , verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    message = models.TextField(max_length=300 , verbose_name="متن پیام")

    class Meta :
        verbose_name = "پیام "
        verbose_name_plural = "پیام ها"


    def __str__(self):
        return self.name