# Generated by Django 4.2.7 on 2023-11-21 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0023_book_link_dowload_buy_book_link_dowload_free'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='release_date',
            field=models.DateField(verbose_name=''),
        ),
    ]