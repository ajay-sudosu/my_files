# Generated by Django 4.0.2 on 2022-02-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_quiz_options_quiz_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
