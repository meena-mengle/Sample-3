# Generated by Django 3.2.24 on 2024-02-28 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='Product', max_length=100),
        ),
    ]
