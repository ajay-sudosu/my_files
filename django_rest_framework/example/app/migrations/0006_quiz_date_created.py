# Generated by Django 4.0.2 on 2022-02-22 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_quiz_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
