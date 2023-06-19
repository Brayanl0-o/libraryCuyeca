# Generated by Django 4.2.2 on 2023-06-18 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.TextField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='autor',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='book',
            name='number_pags',
            field=models.IntegerField(default=0),
        ),
    ]
