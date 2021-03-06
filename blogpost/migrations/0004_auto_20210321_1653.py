# Generated by Django 3.1.7 on 2021-03-21 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0003_blogmodel_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='editdate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='category',
            field=models.CharField(choices=[('math', '数学'), ('program', 'プログラミング'), ('game', 'ゲーム'), ('sports', 'スポーツ'), ('anime', 'アニメ'), ('prime', '素数大富豪'), ('life', '日常'), ('other', 'その他')], max_length=50),
        ),
    ]
