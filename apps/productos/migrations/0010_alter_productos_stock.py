# Generated by Django 4.2.3 on 2023-07-23 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_rename_nombre_categorias_categoria_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='stock',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Stock'),
        ),
    ]
