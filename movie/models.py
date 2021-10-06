from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Categories"

class movie(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='pics')
    relyear=models.CharField(max_length=5)
    price=models.IntegerField()
    ratings=models.CharField(max_length=5)
    category=models.ManyToManyField(Category)
    def __str__(self):
        return self.name