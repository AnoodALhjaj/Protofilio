# Generated by Django 2.2.13 on 2021-01-13 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20210113_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='jobs'),
        ),
    ]
