# Generated by Django 3.1.7 on 2021-03-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0011_auto_20210323_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animemodel',
            name='image',
            field=models.TextField(default='https://i.gzn.jp/img/2019/12/14/anime-2020winter/00.png'),
        ),
    ]
