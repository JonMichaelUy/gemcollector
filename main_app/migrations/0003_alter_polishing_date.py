# Generated by Django 4.0.6 on 2022-07-08 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_polishing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polishing',
            name='date',
            field=models.DateField(verbose_name='date polished'),
        ),
    ]
