# Generated by Django 3.1.12 on 2021-06-20 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_auto_20210620_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kimetsu',
            name='gender',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], max_length=2),
        ),
    ]