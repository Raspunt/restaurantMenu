from django.db import models



class Product(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField()
    price = models.IntegerField()
    price_valuta = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField()
    products = models.ManyToManyField(Product,blank=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    table_name = models.CharField(max_length=150)
    price = models.FloatField()

    def __str__(self):
        return self.table_name
