from django.core.validators import MinValueValidator
from django.db import models


class Collection(models.Model):
    title = models.CharField(max_length=255)  

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']

class Post(models.Model):
    title=models.CharField(max_length=100)
    detail=models.TextField()
    unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(1)])
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, null=True)