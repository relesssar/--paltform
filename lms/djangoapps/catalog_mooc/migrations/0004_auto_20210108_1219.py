# Generated by Django 3.1.5 on 2021-01-08 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_mooc', '0003_auto_20210106_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogmoc',
            name='access',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='catalogmoc',
            name='weeks',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
