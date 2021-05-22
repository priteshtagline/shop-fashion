# Generated by Django 3.2.3 on 2021-05-22 06:27

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'brand',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('redirect_url', models.URLField()),
                ('price', models.FloatField(blank=True, null=True)),
                ('color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('description', models.TextField()),
                ('image1', models.ImageField(upload_to='product/')),
                ('image2', models.ImageField(upload_to='product/')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.department')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='VtovProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('vtov_products', models.ManyToManyField(related_name='vtov_products', to='products.Product', verbose_name='Vtov Products')),
            ],
            options={
                'verbose_name': 'Vtov Products',
                'verbose_name_plural': 'Vtov Products',
                'db_table': 'vtov_products',
            },
        ),
        migrations.CreateModel(
            name='SimilarProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('similar_products', models.ManyToManyField(related_name='similar_products', to='products.Product', verbose_name='Similar Products')),
            ],
            options={
                'verbose_name': 'Similar Products',
                'verbose_name_plural': 'Similar Products',
                'db_table': 'similar_products',
            },
        ),
        migrations.CreateModel(
            name='ShopLook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='shoplook/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.department')),
                ('products', models.ManyToManyField(to='products.Product')),
            ],
            options={
                'verbose_name': 'Shop Looks',
                'verbose_name_plural': 'Shop Looks',
                'db_table': 'shop_looks',
            },
        ),
        migrations.CreateModel(
            name='RecommendedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('recommended_products', models.ManyToManyField(related_name='recommended_products', to='products.Product', verbose_name='Recommended Products')),
            ],
            options={
                'verbose_name': 'Recommended Products',
                'verbose_name_plural': 'Recommended Products',
                'db_table': 'recommended_products',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.department'),
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('products', models.ManyToManyField(to='products.Product')),
            ],
            options={
                'db_table': 'campaign',
            },
        ),
    ]
