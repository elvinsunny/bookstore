# Generated by Django 4.2.5 on 2023-11-25 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_category_description_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]
