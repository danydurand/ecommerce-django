# Generated by Django 3.2 on 2022-09-13 17:41

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_hidden', models.BooleanField(default=False)),
                ('is_trending', models.BooleanField(default=False)),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keywords', models.CharField(max_length=150)),
                ('meta_description', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=150)),
                ('image', models.ImageField(upload_to=store.models.get_file_path)),
                ('small_description', models.CharField(max_length=150)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('original_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('is_hidden', models.BooleanField(default=False)),
                ('is_trending', models.BooleanField(default=False)),
                ('tag', models.CharField(max_length=150)),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keywords', models.CharField(max_length=150)),
                ('meta_description', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
