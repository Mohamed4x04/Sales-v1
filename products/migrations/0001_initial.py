# Generated by Django 3.2 on 2022-11-26 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category Name')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Storage')),
            ],
        ),
        migrations.CreateModel(
            name='AddProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcode', models.IntegerField(default=0, verbose_name='Parcode')),
                ('name', models.CharField(max_length=50, verbose_name='Product Name')),
                ('purchasing_price', models.FloatField(default=0, verbose_name='Purchasing Price')),
                ('order_limit', models.IntegerField(default=0, verbose_name='Order Limit')),
                ('sell_price', models.FloatField(default=0, verbose_name='Sell Price')),
                ('date_add', models.DateTimeField(blank=True, null=True, verbose_name='Date Add')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Product Image')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_category', to='products.category', verbose_name='Category')),
                ('storage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_storage', to='products.storage', verbose_name='Storage')),
            ],
        ),
    ]