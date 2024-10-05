from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/', blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.name
