# Generated by Django 3.2.8 on 2021-11-26 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0002_auto_20211020_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogs',
            name='breed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rest_api_app.breed'),
        ),
    ]
