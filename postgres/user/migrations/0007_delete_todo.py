# Generated by Django 4.1.2 on 2022-10-13 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_todo_delete_todolist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Todo',
        ),
    ]