# Generated by Django 4.2.5 on 2023-10-08 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_blogpost_is_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='url-метка'),
        ),
    ]
