# Generated by Django 2.2.7 on 2019-11-28 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.IntegerField(null=True, verbose_name='Картинко'),
        ),
        migrations.AddField(
            model_name='service',
            name='tab1',
            field=models.CharField(max_length=255, null=True, verbose_name='TAB1 название'),
        ),
        migrations.AddField(
            model_name='service',
            name='tab1text',
            field=models.CharField(max_length=255, null=True, verbose_name='TAB1 текст'),
        ),
        migrations.AddField(
            model_name='service',
            name='tab2',
            field=models.CharField(max_length=255, null=True, verbose_name='TAB2 название'),
        ),
        migrations.AddField(
            model_name='service',
            name='tab2text',
            field=models.CharField(max_length=255, null=True, verbose_name='TAB2 текст'),
        ),
        migrations.AddField(
            model_name='service',
            name='tab3',
            field=models.CharField(max_length=255, null=True, verbose_name='TAB3 название'),
        ),
        migrations.AddField(
            model_name='service',
            name='tab3text',
            field=models.CharField(max_length=255, null=True, verbose_name='TAB3 текст'),
        ),
    ]
