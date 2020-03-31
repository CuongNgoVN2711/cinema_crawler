from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    rating = models.CharField(max_length=4)
    review_number = models.CharField(max_length=20)

    def __str__(self):
        price = str(self.price)
        return "{} - {}VND - {} stars".format(self.name, price[:-3] + '.' + price[-3:], int(self.rating[0:-1])//20)