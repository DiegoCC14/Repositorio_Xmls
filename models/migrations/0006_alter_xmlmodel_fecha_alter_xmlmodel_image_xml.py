# Generated by Django 4.1.5 on 2023-01-22 06:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_alter_xmlmodel_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xmlmodel',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 22, 3, 3, 37, 166849)),
        ),
        migrations.AlterField(
            model_name='xmlmodel',
            name='image_xml',
            field=models.ImageField(blank=True, default='app/static/img/image_xml.webp', upload_to=''),
        ),
    ]
