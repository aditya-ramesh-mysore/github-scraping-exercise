# Generated by Django 5.1.3 on 2024-11-14 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RepoData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='description',
            field=models.CharField(max_length=600, null=True),
        ),
    ]
