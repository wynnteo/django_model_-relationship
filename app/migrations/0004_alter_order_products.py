# Generated by Django 4.1.1 on 2022-10-26 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='products', to='app.product'),
        ),
    ]
