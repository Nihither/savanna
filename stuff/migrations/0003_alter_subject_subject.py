# Generated by Django 4.1.7 on 2023-07-07 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0002_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject',
            field=models.CharField(blank=True, choices=[('Английский', 'Английский'), ('Китайский', 'Китайский'), ('Подготовка к школе', 'Подготовка к школе')], max_length=20, null=True),
        ),
    ]
