# Generated by Django 4.2.3 on 2023-07-21 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0008_remove_subcategorias_nombre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorias',
            old_name='nombre',
            new_name='categoria_name',
        ),
    ]
