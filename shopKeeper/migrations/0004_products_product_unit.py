# Generated by Django 3.1.7 on 2021-03-14 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopKeeper', '0003_auto_20210310_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_unit',
            field=models.CharField(default='N', max_length=100),
            preserve_default=False,
        ),
    ]
