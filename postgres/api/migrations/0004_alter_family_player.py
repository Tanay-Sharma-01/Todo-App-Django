# Generated by Django 4.1.2 on 2022-10-10 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_family'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='Player',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.player'),
        ),
    ]
