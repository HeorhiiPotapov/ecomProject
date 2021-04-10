# Generated by Django 3.2 on 2021-04-10 23:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='category_img/defoult.png', upload_to='category_img', verbose_name='Лого категории')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('slug', models.SlugField(max_length=300, unique=True, verbose_name='Url')),
                ('is_active', models.BooleanField(default=True, verbose_name='Статус')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=600, verbose_name='Текст')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_img', verbose_name='Изображение')),
                ('is_active', models.BooleanField(default=True, verbose_name='Статус')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Дополнительное фото',
                'verbose_name_plural': 'Дополнительные фото',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='slider')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдеры',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена')),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Дисконт')),
                ('main_image', models.ImageField(upload_to='product_img', verbose_name='Изображение')),
                ('video', models.URLField(blank=True, null=True, verbose_name='Ссылка на видео')),
                ('overview', models.TextField(max_length=2000, verbose_name='Описание')),
                ('is_active', models.BooleanField(default=False, verbose_name='Статус')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата добавления')),
                ('city', models.CharField(choices=[('0', 'Все'), ('1', 'Харьков'), ('2', 'Киев'), ('3', 'Днепр')], default=0, max_length=20, verbose_name='Город')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар/Акция',
                'verbose_name_plural': 'Товары/Акции',
                'ordering': ('-timestamp',),
            },
        ),
    ]
