# Generated by Django 3.2.3 on 2021-06-18 07:20

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('browse_url', models.URLField(max_length=2000)),
                ('image', models.ImageField(upload_to='carousel/')),
                ('text_color', colorfield.fields.ColorField(default='#000000FF', max_length=18)),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'db_table': 'home_carousel',
                'ordering': ['display_order'],
            },
        ),
    ]