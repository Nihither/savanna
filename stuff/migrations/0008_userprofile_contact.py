# Generated by Django 4.1.7 on 2023-08-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0007_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='contact',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]