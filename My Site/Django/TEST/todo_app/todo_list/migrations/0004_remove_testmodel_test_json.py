# Generated by Django 4.1.5 on 2023-01-25 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_testmodel_awesome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testmodel',
            name='test_json',
        ),
    ]
