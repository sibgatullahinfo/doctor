# Generated by Django 5.1 on 2024-08-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0010_item_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='blog_tag',
            field=models.ManyToManyField(blank=True, null=True, to='testapp.blogtag'),
        ),
    ]
