# Generated by Django 5.0.3 on 2024-04-03 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_modelmaxx_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelmaxx',
            name='file',
            field=models.ImageField(null=True, upload_to='{% static %}'),
        ),
    ]