# Generated by Django 5.0.1 on 2024-01-10 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
