# Generated by Django 3.2.8 on 2021-10-25 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_auto_20211026_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]