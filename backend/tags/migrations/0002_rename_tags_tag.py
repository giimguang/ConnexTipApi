# Generated by Django 4.1.7 on 2023-02-28 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_category_article_category'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]
