# Generated by Django 2.0.5 on 2018-06-08 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('阅读统计', '0002_auto_20180604_2127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='计数信息类',
            options={'ordering': ['-日期信息方法']},
        ),
        migrations.AlterModelOptions(
            name='计数类',
            options={'ordering': ['id']},
        ),
    ]
