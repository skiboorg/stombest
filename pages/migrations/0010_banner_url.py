# Generated by Django 2.2.7 on 2020-01-15 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20200107_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка'),
        ),
    ]