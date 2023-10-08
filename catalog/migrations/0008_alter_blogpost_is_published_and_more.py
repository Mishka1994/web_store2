# Generated by Django 4.2.5 on 2023-10-07 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='публикуется'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='number_of_views',
            field=models.IntegerField(default=0, verbose_name='счетчик просмотров'),
        ),
    ]
