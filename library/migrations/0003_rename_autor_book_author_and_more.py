# Generated by Django 4.2.2 on 2023-06-18 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_summary_alter_book_autor_alter_book_genre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='number_pags',
            new_name='number_pages',
        ),
    ]
