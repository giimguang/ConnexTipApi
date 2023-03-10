# Generated by Django 4.1.7 on 2023-02-22 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('banner', models.ImageField(blank=True, null=True, upload_to='banners/')),
                ('slug', models.CharField(max_length=20, null=True, unique=True)),
                ('viewer', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('tags', models.ManyToManyField(related_name='tagged', to='tags.tags')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
