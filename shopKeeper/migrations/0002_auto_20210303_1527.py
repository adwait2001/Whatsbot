# Generated by Django 3.1.7 on 2021-03-03 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopKeeper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_pics'),
        ),
    ]
