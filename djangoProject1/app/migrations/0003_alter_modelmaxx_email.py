# Generated by Django 5.0.3 on 2024-03-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_modelmaxx_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelmaxx',
            name='email',
            field=models.CharField(max_length=80),
        ),
    ]