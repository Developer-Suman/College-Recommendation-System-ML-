# Generated by Django 3.2.13 on 2022-04-26 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recommendation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
