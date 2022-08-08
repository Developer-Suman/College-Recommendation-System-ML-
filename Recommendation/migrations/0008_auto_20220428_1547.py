# Generated by Django 3.2.13 on 2022-04-28 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recommendation', '0007_rename_schoollocaton_review_schoollocation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='user',
        ),
        migrations.AddField(
            model_name='register',
            name='school_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Recommendation.oldschool'),
        ),
    ]
