# Generated by Django 3.2.12 on 2022-03-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp430', '0003_trainees'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('T-shirt', 'T-shirt'), ('Ball', 'Ball'), ('Shoes', 'Shoes')], max_length=200)),
                ('descirption', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
