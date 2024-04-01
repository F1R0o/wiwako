from django.db import models
from categories.models import Category
from PIL import Image


# Create your models here.
class Wiwako(models.Model):
    saxeli_qartulad = models.CharField(max_length=50)
    saxeli_inglisurad = models.CharField(max_length=50)
    agwera = models.TextField(null=True)
    maragshia = models.BooleanField(default=True)
    fasi = models.FloatField()
    photo  = models.ImageField(upload_to="wiwakebi/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.saxeli_qartulad
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 500 or img.width > 500:
                output_size = (500, 500)
                img.thumbnail(output_size)
                img.save(self.photo.path)
