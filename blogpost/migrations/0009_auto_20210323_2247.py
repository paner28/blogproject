# Generated by Django 3.1.7 on 2021-03-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0008_animemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animemodel',
            name='image',
            field=models.ImageField(default='../static/img/header-1.png', upload_to='img/'),
        ),
    ]
