# Generated by Django 2.2.10 on 2020-11-10 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_info',
            name='email',
            field=models.CharField(max_length=255),
        ),
    ]
