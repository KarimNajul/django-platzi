# Generated by Django 4.2.8 on 2024-09-30 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='create_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
