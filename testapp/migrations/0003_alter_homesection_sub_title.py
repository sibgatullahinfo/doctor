# Generated by Django 5.0.8 on 2024-08-18 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_homesection_type_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homesection',
            name='sub_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
