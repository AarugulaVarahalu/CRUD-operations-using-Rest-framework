from django.db import models

# Create your models here.



class Detail(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Detail'
        verbose_name_plural = 'Details'

