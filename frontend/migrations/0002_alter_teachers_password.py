# Generated by Django 3.2.12 on 2023-07-14 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='password',
            field=models.CharField(max_length=250),
        ),
    ]
