# Generated by Django 4.0.2 on 2022-02-24 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_question_difficulty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='date_created',
        ),
    ]
