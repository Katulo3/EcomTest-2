# Generated by Django 4.2.3 on 2023-07-20 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmemodel',
            name='titulo',
            field=models.CharField(default='titulo', max_length=50),
        ),
    ]
