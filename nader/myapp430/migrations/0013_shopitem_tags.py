# Generated by Django 3.2.12 on 2022-03-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp430', '0012_remove_shopitem_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopitem',
            name='tags',
            field=models.ManyToManyField(to='myapp430.Tag'),
        ),
    ]
