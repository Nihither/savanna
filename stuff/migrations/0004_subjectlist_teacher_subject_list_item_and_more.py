# Generated by Django 4.1.7 on 2023-07-08 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0003_alter_subject_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_list_item', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject_list_item',
            field=models.ManyToManyField(to='stuff.subjectlist'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stuff.subjectlist'),
        ),
    ]
