# Generated by Django 3.0.8 on 2020-07-13 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SkewCorrector', '0002_auto_20200713_0648'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rotate_angle',
            field=models.FloatField(blank=True, null=True),
        ),
    ]