# Generated by Django 4.0.2 on 2022-02-24 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_question_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.IntegerField(blank=True, choices=[('Easy', 'Easy'), ('Hard', 'Hard'), ('Medium', 'Medium')], default='Easy', null=True, verbose_name='Difficulty Level'),
        ),
    ]
