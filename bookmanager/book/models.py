from django.db import models

# Create your models here.
#自动生成主键 --id
class BookInFo(models.Model):

    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
class PropleInFo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()

    def __str__(self):
        return self.name, self.gender

    book = models.ForeignKey(BookInFo, on_delete=models.CASCADE)
