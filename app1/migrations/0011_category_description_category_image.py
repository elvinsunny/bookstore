# Generated by Django 4.2.5 on 2023-11-25 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images/'),
        ),
    ]
