# Generated by Django 5.1 on 2024-08-18 10:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_alter_homesection_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, default='image', null=True, upload_to='item/image')),
                ('icon_class', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('type', models.CharField(choices=[('SERVICE', 'service'), ('PROJECT', 'project'), ('BLOG', 'blog')], default='SERVICE', max_length=20)),
            ],
        ),
    ]
