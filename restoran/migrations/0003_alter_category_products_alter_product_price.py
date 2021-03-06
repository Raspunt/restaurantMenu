# Generated by Django 4.0.6 on 2022-07-14 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restoran', '0002_remove_product_category_category_products_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(blank=True, to='restoran.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
