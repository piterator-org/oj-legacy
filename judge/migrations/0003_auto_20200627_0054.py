# Generated by Django 2.2.13 on 2020-06-27 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0002_auto_20200626_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='score',
            field=models.FloatField(verbose_name='score'),
        ),
    ]
